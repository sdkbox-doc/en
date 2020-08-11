# SDKBOX for Cocos Creator

## SDKBox Helper

this command can help you to install `SDKBox` and `SDKBox GUI For Creator` (of course, you can install SDKBox manually, without SDKBox Helper).


Download [SDKBoxHelper Windows](https://github.com/hugohuang1111/sdkboxhelper/releases/download/v0.0.5/sdkboxhelper.exe) or [SDKBoxHelper Mac](https://github.com/hugohuang1111/sdkboxhelper/releases/download/v0.0.5/sdkboxhelper)

## SDKBox Installer

* run command `sdkboxhelper` in terminal to install `SDKBox Installer`
* or run python2 script `python -c """import urllib; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/install/install.py').read(); exec(s)"""` to install `SDKBox Installer`
* or Manually, Download [SDKBox Installer](http://download.sdkbox.com/installer/v1/sdkbox_installer.zip), and unzip to `~/.sdkbox/bin` (`C:\Users\${UserName}\.sdkbox\bin` on Windows), add `~/.sdkbox/bin` to environment PATH

__Note__:
open a new terminal and run command `sdkbox -h` to check if `SDKBox Installer` have installed. maybe need restart when you got `command not find` error.

## SDKBox GUI For Creator

* run command `sdkboxhelper -t creator -p path/to/creator_project` in terminal to install `SDKBox GUI For Creator`
* or Manually, Download `SDKBox GUI For Creator` [package](http://sdkbox.anysdk.com/gui/creator/sdkbox-1.4.1.zip)
    - Global Install: unzip `SDKBox GUI For Creator` package to path `~/.CocosCreator/packages` (`C:\Users\${UserName}\.CocosCreator\packages` on windows)
    - locally Install: unzip `SDKBox GUI For Creator` package to path `${CocosCreator Project}/packages`

__Note__:

* Cocos Creator 2.4.1- need't install `SDKBox GUI For Creator` manually. `SDKBox GUI For Creator` is built in.

* if `SDKBox` item doesn't show in `Expand` Menu, maybe you need restart Cocos Creator.

* packages file tree should be like follow:
```
packages
|--sdkbox
    |--app
    |--main.js
    |--package.json
```

