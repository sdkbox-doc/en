#!/usr/bin/python
# -*- coding: utf-8 -*-

import traceback
import sys
import argparse
import os
import re
import shutil
import errno

def rmdir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def mkdir(src):
    try:
        os.makedirs(src)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # raises the error again

def get_curr_path():
    return os.path.dirname(os.path.realpath(__file__))

def read_file(path):
    with open(path, "r") as target_file:
        return target_file.read()

def write_file(path, data):
    with open(path, "w") as text_file:
        text_file.write(data)

class DocGen:
    def __init__(self, name, base_path, out_path):
        self.name = name
        self.base_path = base_path
        self.main_file = os.path.join(base_path, 'readme.md')
        self.out_path = os.path.abspath(out_path)
        # self.pre = re.compile(ur'Include Base:(.*)')
        self.pre = re.compile(ur'<<\[(.*)\]')
        self.folders = []
        self.search_folders()

    def search_folders(self):
        for f in os.listdir(self.base_path):
            folder_path = os.path.join(self.base_path, f)
            if os.path.isdir(folder_path):
                self.folders.append(f)
                # print "====> found " + f

    def generate(self):

        if os.path.exists(self.main_file):
            print '===> generate ' + self.name
            mkdir(self.out_path)
            origin_data = read_file(self.main_file)

            for f in self.folders:
                out_data = origin_data
                match = re.search(self.pre, out_data)

                while match:
                    section_path = match.group(1)
                    section_path = os.path.join(self.base_path, f, section_path)

                    section_file = read_file(section_path)
                    out_data = re.sub(self.pre, section_file, out_data, 1)

                    match = re.search(self.pre, out_data)

                out_file = os.path.join(self.out_path, f + '.md')
                write_file(out_file, out_data)
                print 'Write file: ' + out_file
        else:
            print '===> skip ' + self.name
            print '===> failed to find ' + self.main_file

    def get_name(self):
        return self.name

class DocManager:

    def __init__(self, base_path, out_path):
        self.base_path = base_path
        self.out_path = os.path.abspath(out_path)
        self.plugins = []
        self.search_plugin()

    def search_plugin(self):
        for f in os.listdir(self.base_path):
            bp = os.path.join(self.base_path, f)
            if os.path.isdir(bp) and f not in ['.git', '.idea']:
                op = os.path.join(self.out_path, f)
                d = DocGen(f, bp, op)
                self.plugins.append(d)

    def generate(self, name):
        if name == 'all':
            print '==> generate doc for all the plugins'
            for p in self.plugins:
                p.generate()
        else:
            result = self.find_plugin(name)
            if result:
                result.generate()
            else:
                print '==> invalid folder name ' + name
                sys.exit(1)

    def find_plugin(self, name):
        for p in self.plugins:
            if name == p.get_name():
                return p
        return None

def main():

    parser = argparse.ArgumentParser(description='The awesome document generator!')
    parser.add_argument('name', help='The name of the plugin, use "all" if you want to generate everything')
    args = parser.parse_args()

    curr_path = get_curr_path()
    out_path = os.path.join(curr_path, '..', 'docs', 'plugins')
    doc_mgr = DocManager(curr_path, out_path)
    doc_mgr.generate(args.name)

    sys.exit(0)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
