# SDKBOX: Installing SDKBOX Plugins using the Installer

### Get the Installer

* Make sure your system have [python](https://www.python.org)

* Paste the script below into a terminal prompt. It will explain what it does and setup everything for you:
```
python -c "import urllib; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/install/install.py').read(); exec s"
```


### Install a plugin
* From a command-line, `cd` to your applications root directory. Example:
```sh
cd MyGame
```

* Now, you can install your plugin using the SDKBOX installer. Example:
```sh
sdkbox import facebook
```

### What Next?
The SDKBOX installer takes care of most of what you need. However, there are still a few manual steps that you must complete. After the installer runs it outputs a list of the remaining steps that you need to perform, referring to the plugin bundle PDF. Example output from running the above command:
```sh
$ sdkbox import facebook
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.7.1


  *****************************
  ******** Manual Step ********
  *****************************

1. Edit "project.properties"
   Set "target=android-15"

Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/facebook/v3-cpp/
Installation Successful :)
```

### Other Installer options.

#### Commands:
The SDKBOX Installer has several commands that you can use. You can always see these by running `sdkbox` by itself or using the `-h` help switch:

| Command            | Description  |
| :--------------------- | :----------- |
| list | list available and cached packages installed on your machine. The package repository is located in your home directory. |
|  import [name] |  imports the package 'name' into your project. For a list of names, see the list command. You can also specify local archived packages or a directory by specifying the -b option (see above). |
| update | re-imports all imported packages to update them to the latest version. If you have imported packages prior to SDKBOX v0.5.6.19 then you must manually import your packages again to add them to the package manifest. |
| info | displays the packages that have been imported into your project. If you have packages imported that are not in the package manifest, SDKBOX will alert you as to which packages it thinks are imported. |
| restore | restores your project to the latest backup that can be found. If you have made changes to your project files since importing, this will overwrite your changes, so use carefully. |
| clean [N] | removes all packages older than N days. |
| symbols | displays the symbols that are used to drive the import process. These symbols are very useful for debugging, so if you have issues, and post on the forums, please include the symbols if possible. |

#### Switches
The SDKBOX Installer has several switches that you can use. You can always see these by running `sdkbox` by itself or using the `-h` help switch:

| switch  | alternate switch  | what it does |
| :------------- | :------------------------| :-----|
| -h      | --help          |show this help message and exit |
| -v      | --verbose       |specify verbosity level of the log |
| -p PROJECT | --project PROJECT |path to project root (defaults to .) |
| -b PLUGIN | --plugin PLUGIN |specify path to plugin (defaults to .) |
| -D SYMBOL | --symbol SYMBOL |define a symbol for the package script |
| -q | --nohelp |don't open online documentation after installation. |
| -d [DAYS] | --days [DAYS] |specify number of days of logs and packages to keep |
|         | --china        |use China based server instead of US |
|         | --dryrun        |test install before performing. |
|         | --forcedownload |force download of package even if it is already downloaded. |
|         | --noupdate        |ignore available updates. |
|         | --alwaysupdate    |alwyas update to the latest version |
|         | --jsonapi        |treat commands as API calls and return JSON formatted output |
|         | --patcherrors        |patch failures are counted as errors instead of warnings. |
|         | --nopatching        |skip all patching commands when executing package script. |

Examples:
```sh
Add 'In App Purchase' plugin to your game
$ sdkbox import -b iap -p /path/to/your/cocos2dx/game/
```
```sh
#The -b option may be omitted and -p too if you are in your project directory
$ sdkbox import iap
```
```sh
#If you want to install a earlier version of the plugin
$ sdkbox import -b /path/to/your/package
```
```sh
#List all available packages on the server
$ sdkbox list
```
```sh
#Show all package imported into your project
$ sdkbox info
```
```sh
#clean logs and packages older than 5 days
$ sdkbox clean 5
```
```sh
#use playphone as your store for android
$ sdkbox set store playphone
```

### Staying Up-to-date
The SDKBOX installer automatically checks for updates to itself. It will ask for your permission before updating. This will allow you to stay current and also automatically pull updates to your plugin bundles when they become available.
```sh
$ sdkbox
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.6.24

A newer version of SDKBOX is available, would you like to update to v0.5.7.1?
Please type Yes, No or Quit Yes
updated SDKBOX v0.5.6.18 to v0.5.7.1 at sdkbox
```
