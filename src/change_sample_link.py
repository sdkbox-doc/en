import os
import re

for root, dirs, files in os.walk('./'):
    for fin in files:
        if fin.find('index.md') == 0:
            plugin = os.path.split(root)[1];
            if plugin == 'googleanalytics':
                plugin = 'ga'
            if plugin == 'flurryanalytics':
                plugin = 'flurry'
            if plugin == 'achievement':
                plugin = 'playphone'
            if plugin == 'leaderboard':
                plugin = 'playphone'
            print plugin
            new_sample_addr = 'https://github.com/sdkbox/sdkbox-sample-' + plugin + ')'
            sub_reg = re.compile('https://github\.com.*sample\)')
            path = os.path.join(root, fin)
            f = open(path, 'rb+')
            contents = f.read()
            contents = sub_reg.sub(new_sample_addr, contents);
            f.seek(0)
            f.write(contents)
            f.close()

