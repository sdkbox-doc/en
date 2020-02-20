#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import json
import hashlib
import platform
import zipfile
import shutil
import stat

# update sdkbox creator gui command
# python -c """import urllib; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/install/updateguiforcreator.py').read(); exec(s)"""



class Utils:

    """ platforms """
    PLATFORM_MAC = 1
    PLATFORM_WINDOWS = 2
    PLATFORM_LINUX = 3

    @staticmethod
    def curl(url, destination=None, chunk_size=None, callback=None):
        try:
            response = urllib2.urlopen(url)
            if None == chunk_size:
                data = response.read()
            else:
                data = ''
                size = 0
                total_size = response.headers['content-length']
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    size += len(chunk)
                    if None != callback:
                        callback(size, total_size)
                    data += chunk
        except Exception as e:
            print('ERROR! url:' + url)
            return None
        if None != destination:
            Utils.create_dir_if(destination)
            f = open(destination, 'wb')
            if not f:
                print('ERROR! can not open file:' + destination)
                return None
            f.write(data)
            f.close()
        if None != callback:  # the cursor flyback needs a blank line after
            print ''
        return data

    @staticmethod
    def progress_bar(amount, total, width=35):
        perc = 100 * int(amount) / int(total)
        on = width * perc / 100
        off = width - on
        s = '[' + on * '#' + off * ' ' + '] ' + str(perc) + '%'
        if Utils.platform() == Utils.PLATFORM_WINDOWS:
            print s + '\r',
        else:
            print s + '\033[1A'

    @staticmethod
    def create_dir_if(path):
        if os.path.exists(path):
            return
        if path.endswith('/'):
            os.makedirs(path)
            return
        else:
            dir_name = os.path.dirname(path)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

    @staticmethod
    def calculate_sha1(data):
        hasher = hashlib.sha1()
        hasher.update(data)
        sha1 = hasher.hexdigest()
        return sha1

    @staticmethod
    def platform():
        p = platform.system()
        if p == 'Windows':
            return Utils.PLATFORM_WINDOWS
        elif p.startswith('Linux'):
            return Utils.PLATFORM_LINUX
        elif p == 'Darwin':
            return Utils.PLATFORM_MAC
        raise RuntimeError('unsupported platform ' + p)

    @staticmethod
    def unzip_file(path, dir = None):
        if path.endswith('.zip'):
            dir_name = dir
            if not dir_name:
                dir_name = os.path.dirname(path)

            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(dir_name)

    @staticmethod
    def remove_folder(path):
        if os.path.exists(path):
            shutil.rmtree(path)

    @staticmethod
    def move_folder(src, dst):
        if os.path.exists(src):
            shutil.move(src, dst)


def check_installer(sdkbox_dir):
    sdkbox_file = os.path.join(sdkbox_dir, 'bin', 'sdkbox')
    return os.path.isfile(sdkbox_file)

def load_local_gui_info(sdkbox_dir):
    info_file = os.path.join(sdkbox_dir, 'creator', 'data', 'info.json')
    try:
        with open(info_file) as json_data:
            info = json.load(json_data)
            tJson = info

            # make sure info['version']['gui']['local'] have default value
            key = 'version'
            if key not in tJson:
                tJson[key] = {}
            tJson = tJson[key]

            key = 'gui'
            if key not in tJson:
                tJson[key] = {}
            tJson = tJson[key]

            key = 'local'
            if key not in tJson:
                tJson[key] = ''

            key = 'remote'
            if key not in tJson:
                tJson[key] = ''

            return info
    except:
        return json.loads('{"version":{"gui":{"local":"","remote":""} } }')

def save_local_gui_info(sdkbox_dir, info):
    info_file = os.path.join(sdkbox_dir, 'creator', 'data')
    if not os.path.exists(info_file):
        os.makedirs(info_file)
    info_file = os.path.join(info_file, 'info.json')
    with open(info_file, 'w') as outfile:
        json.dump(info, outfile)

def load_remote_gui_version(server):
    url = server + 'gui/creator/version'
    data = Utils.curl(url, None, 1024, None)
    if not data or 0 == len(data):
        raise Exception('ERROR! load sdkbox creator gui fail')
    info = json.loads(data)

    key = 'version'
    if key not in info:
        raise Exception('ERROR! can not load sdkbox creator gui remote version')
    return info[key]

def download_gui_package(path, version, server):
    response = Utils.curl('{0}gui/creator/sdkbox-{1}.zip'.format(server , version), None, 1024, Utils.progress_bar)
    try:
        Utils.create_dir_if(path)
        f = open(path, 'wb')
        f.write(response)
        f.close()
    except:
        raise RuntimeError('ERROR! failed to save SDKBOX creator GUI package')

    return path

def upgrade_gui(path, sdkbox_dir):
    Utils.unzip_file(path)
    Utils.remove_folder(os.path.join(sdkbox_dir, 'temp', 'backup', 'app'))
    Utils.move_folder(os.path.join(sdkbox_dir, 'creator', 'app'), os.path.join(sdkbox_dir, 'temp', 'backup', 'app'))
    Utils.move_folder(os.path.join(sdkbox_dir, 'temp', 'sdkbox', 'app'), os.path.join(sdkbox_dir, 'creator', 'app'))

def load_country_code_by_file(file_path):
    content = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                content = json.load(f)
            except Exception as e:
                content = {}

    return content

def check_country_code_by_net():
    country_code = 'US'
    try:
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        url = 'http://ip-api.com/json/'
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        page = response.read()
        ret = json.loads(page)
        country_code = ret['countryCode'].upper()
    except RuntimeError as e:
        pass
    
    return country_code

def load_country_code():
    loc = os.path.join(os.path.expanduser('~'), '.sdkbox', 'conf', 'loc.json')
    j = load_country_code_by_file(loc)
    country_code_key = 'countryCode'
    if country_code_key in j:
        if j[country_code_key]:
            return j[country_code_key]
    country_code = check_country_code_by_net()
    j[country_code_key] = country_code

    with open(loc, 'w') as f:
        json.dump(j, f)

    return country_code

def main():
    SDKBOX_DIR = os.path.join(os.path.expanduser('~'), '.sdkbox')

    # make sure creator is closed
    print('Please make sure Cocos Creator is closed. please ENTER to countinue')
    raw_input()

    # 1. check instller if installed
    if not check_installer(SDKBOX_DIR):
        print('SDKBox installer is not installed')
        sys.exit(0)

    # 2. load sdkbox creator gui local info
    local_info = load_local_gui_info(SDKBOX_DIR)
    local_version = local_info['version']['gui']['local']

    # check country
    server = 'http://download.sdkbox.com/'
    country_code = load_country_code()
    if country_code and 'CN' == country_code.upper():
        server = 'http://sdkbox.anysdk.com/'

    # 3. load sdkbox creator gui remote version
    remote_version = load_remote_gui_version(server)
    if remote_version == local_version:
        print("SDKBox create gui need't upgrade, local version:" + local_version)
        sys.exit(0)

    # 4. download sdkbox creator gui
    # path = os.path.join(SDKBOX_DIR, 'temp', 'sdkboxguiforcreator.zip')
    path = download_gui_package(os.path.join(SDKBOX_DIR, 'temp', 'sdkboxguiforcreator.zip'), remote_version, server)
    if not path:
        print('ERROR, download SDKBox creator gui failed')
        sys.exit(0)

    # 5. upgrade sdkbox creator gui
    upgrade_gui(path, SDKBOX_DIR)

    # 6. save version info
    local_info['version']['gui']['local'] = remote_version
    local_info['version']['gui']['remote'] = remote_version
    save_local_gui_info(SDKBOX_DIR, local_info)

    print('SUCCESS! SDBOX creator GUI have been updated.')

if __name__ == '__main__':
    main()


