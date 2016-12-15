#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# pip install CppHeaderParser ply
#

#
# how to use api_reference.py
#
# 1. run `./tools/api_reference.py`
#
# 2. check documents
#     - documentation/PluginXX/api-reference-cpp.md
#     - documentation/PluginXX/api-reference-lua.md
#     - documentation/PluginXX/api-reference-js.md
#
# how to config
# 1. manual binding function
#   - edit `plugins/pluginx/lua/config/binding.ini`
#   - add section `manual_binding_function = PluginXX::[setListener,otherFunction]`
#
# 2. rename callback function name (optional)
#   - edit `plugins/pluginx/lua/config/binding.ini`
#   - add section `rename_script_callback = PluginXX::[onCallbackLongFunction=onCallbackFunction]`
#     before `[headers]`
#

import ConfigParser
import os
import sys
import CppHeaderParser

from argparse import ArgumentParser
from sets import Set


CURR_DIR = os.path.split(os.path.realpath(__file__))[0]
OUT_DIR = os.path.realpath(CURR_DIR + "./..")

PLUGIN_PREFIX = "Plugin"


def get_doxygen(comment):
    if '\r\n' in comment:
        cs = comment.split('\r\n')
    else:
        cs = comment.split('\n')

    ret = ""
    for line in cs:
        if line.startswith("/*") or line.endswith("*/"):
            continue
        elif line == "*":  # brief end with empty line
            break
        else:
            if line.startswith("* "):
                line = line[2:]
            ret += line + '\n'

    ret = ret.replace("@brief ", "")
    return ret


def format_function(function_string):
    """
    static void some_function(int param1, int param2);
    =>
    static void some_function(int param1,
                              int param2)
    """
    ret = function_string
    if len(ret) <= 80:
        return ret

    ret = ret.split(',')
    index = ret[0].rfind('(')
    for x in xrange(1, len(ret)):
        ret[x] = " %s%s" % (index * " ", ret[x])

    ret = ',\n'.join(ret)
    return ret


class APIRefGenerator(object):
    """APIRefGenerator("/path/to/PluginTune.h", "Tune")"""

    def __init__(self, header, plugin_name, ini_config):
        self.header = header
        self.pluginName = plugin_name

        section = plugin_name.lower()
        self.target_namespace = ini_config.get(section, "target_namespace")
        self.className = ini_config.get(section, "classes")
        self.skipFunction = []
        if "skip" in ini_config.options(section) and ini_config.get(section, "skip") != '':
            self.skipFunction = ini_config.get(section, "skip").split("::")[1].replace("[", "").replace("]", "").replace("^", "").replace("$", "").split(" ")

        self.manual_binding_function = []
        if "manual_binding_function" in ini_config.options(section) and ini_config.get(section, "manual_binding_function") != '':
            self.manual_binding_function = ini_config.get(section, "manual_binding_function").split("::")[1].replace("[", "").replace("]", "").split(",")

        self.skipFunction = Set(self.skipFunction) - (Set(self.skipFunction) & Set(self.manual_binding_function))
        print plugin_name, self.skipFunction
        self.renameCallBackName = {}

        if "rename_script_callback" in ini_config.options(section):
            callback_names = ini_config.get(section, "rename_script_callback").split("::")[1].replace("[", "").replace("]", "").split(",")
            for name in callback_names:
                v = name.split("=")
                self.renameCallBackName[v[0]] = v[1]

    def run(self):
        try:
            cppHeader = CppHeaderParser.CppHeader(self.header)
        except CppHeaderParser.CppParseError as e:
            print(e)
            sys.exit(1)

        #
        # Generate plugin api reference
        #
        cpp_ref = ""

        lua_fef = ""

        js_ref = ""

        classes = cppHeader.classes
        plugin_name = self.className
        plugin_class = classes[plugin_name]
        methods = plugin_class["methods"]["public"]

        for m in methods:
            if m["debug"][0] == "~":
                continue

            cpp_ref += "```cpp\n%s\n```\n" % format_function(m["debug"])
            doxygen = ""
            if "doxygen" in m.keys():
                doxygen = "> " + get_doxygen(m["doxygen"])

            if len(doxygen):
                cpp_ref += doxygen

            cpp_ref += '\n'

            function_name = m["name"]
            if function_name in self.skipFunction:
                continue

            pa = "("
            i = 0
            for p in m["parameters"]:
                if i > 0:
                    pa += ", "
                pa += p["name"]
                i += 1

            pa += ")"

            f = "%s.%s." % (self.target_namespace, plugin_name) + function_name + pa
            js_ref += "```javascript\n%s;\n```\n" % (format_function(f))
            if len(doxygen):
                js_ref += doxygen
            js_ref += '\n'

            f = "%s.%s:" % (self.target_namespace, plugin_name) + function_name + pa
            lua_fef += "```lua\n%s\n```\n" % (format_function(f))
            if len(doxygen):
                lua_fef += doxygen
            lua_fef += '\n'

        #
        # Generate listener api reference
        #
        listener_class = None
        if self.pluginName + "Listener" in classes.keys():
            listener_class = classes[self.pluginName + "Listener"]
        elif self.pluginName.upper() + "Listener" in classes.keys():
            listener_class = classes[self.pluginName.upper() + "Listener"]

        cpp_l_ref = lua_l_ref = js_l_ref = ""
        if listener_class:
            methods = listener_class["methods"]["public"]

            for m in methods:
                if m["debug"][0] == "~":
                    continue

                cpp_l_ref += "```cpp\n%s;\n```\n" % format_function(m["debug"].replace("virtual ", "").replace(" = 0 ", "").replace("{", ""))
                doxygen = ""
                if "doxygen" in m.keys():
                    doxygen = "> " + get_doxygen(m["doxygen"])

                if len(doxygen):
                    cpp_l_ref += doxygen

                cpp_l_ref += '\n'

                function_name = m["name"]
                if function_name in self.renameCallBackName.keys():
                    function_name = self.renameCallBackName[function_name]

                pa = "("
                i = 0
                for p in m["parameters"]:
                    if i > 0:
                        pa += ", "
                    pa += p["name"]
                    i += 1

                pa += ")"

                f = function_name + pa
                js_l_ref += "```javascript\n%s;\n```\n" % (format_function(f))
                if len(doxygen):
                    js_l_ref += doxygen
                js_l_ref += '\n'

                f = function_name + pa
                lua_l_ref += "```lua\n%s\n```\n" % (format_function(f))
                if len(doxygen):
                    lua_l_ref += doxygen
                lua_l_ref += '\n'

        return True, cpp_ref, cpp_l_ref, lua_fef, lua_l_ref, js_ref, js_l_ref


class Walker(object):
    """docstring for Walker"""

    def __init__(self, arg):
        super(Walker, self).__init__()
        self.plugin = arg.plugin
        self.out_dir = arg.out_dir
        self.src_dir = arg.src

    def run(self):
        join = os.path.join
        ret = ""
        document_output_dir = self.out_dir or OUT_DIR
        found_special_plugin = not self.plugin
        for d in os.listdir(self.src_dir):
            if d in ["core", "shared"] or not os.path.isdir(join(self.src_dir, d)):
                continue

            if self.plugin and d != self.plugin:
                continue
            if self.plugin and d == self.plugin:
                found_special_plugin = True

            name = ""
            header_file_path = ""
            header_dir = join(self.src_dir, d, "share")
            if not os.path.exists(header_dir):
                continue

            for f in os.listdir(header_dir):
                if f.startswith(PLUGIN_PREFIX) and f.endswith(".h"):
                    header_file_path = join(header_dir, f)
                    name = f.replace(PLUGIN_PREFIX, "").replace(".h", "")
                    break

            ini_file_path = join(self.src_dir, d, "lua/config", "binding.ini")
            config = ConfigParser.ConfigParser()
            config.read(ini_file_path)
            ok, cpp, cppl, lua, lual, js, jsl = APIRefGenerator(header_file_path, name, config).run()
            if ok:
                ret += "%s ok\n" % name

                if not os.path.exists(join(document_output_dir, d)):
                    os.makedirs(join(document_output_dir, d))

                template = "## API Reference\n\n### Methods\n%s\n### Listeners\n%s\n"
                data = template % (cpp, cppl)
                doc_path = join(document_output_dir, 'src', d, 'v3-cpp')
                if not os.path.exists(doc_path):
                    os.makedirs(doc_path)
                open(join(doc_path, 'api-reference.md'), 'w').write(data)

                data = template % (lua, lual)
                doc_path = join(document_output_dir, 'src', d, 'v3-lua')
                if not os.path.exists(doc_path):
                    os.makedirs(doc_path)
                open(join(doc_path, 'api-reference.md'), 'w').write(data)

                data = template % (js, jsl)
                doc_path = join(document_output_dir, 'src', d, 'v3-js')
                if not os.path.exists(doc_path):
                    os.makedirs(doc_path)
                open(join(doc_path, 'api-reference.md'), 'w').write(data)

            else:
                ret += "%s missing\n" % name

        if not found_special_plugin:
            ret = "\nNot found %s plugin\n" % self.plugin

        print ret


if __name__ == '__main__':
    parser = ArgumentParser(description="Generate API Reference for SDKBox. example usage: tools/api_reference.py -s ~/Projects/store/csc/plugins -o . -g sdkboxplay")
    parser.add_argument('-s', dest='src',
                        help='source code directory')
    parser.add_argument('-g', dest='plugin',
                        help='Plugin name.')
    parser.add_argument('-o', '--output', dest='out_dir',
                        help='Where to save Api Reference documentation. Default to src folder.')

    (args, unknown) = parser.parse_known_args()
    if len(unknown) > 0:
        print("unknown arguments: %s" % unknown)
        parser.print_help()
        sys.exit(1)

    if args.src is None:
        print 'Please specify source code directory with -s flag'
        parser.print_help()
        sys.exit(1)

    Walker(args).run()
