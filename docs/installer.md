# SDKBOX: Installing SDKBOX Plugins using the Installer

## Preparing to run the SDKBOX Installer
Before you can run the SDKBOX installer you need to do a few things.
* make sure you know the path to where you downloaded the SDKBOX installer. (you can always put it in `/usr/local/bin`)

## Installing a Plugin using the SDKBOX Installer
Now we are ready to install a plugin! There isn't much to it. Ready?

### Installing for OS X
* From a command-line, `cd` to your applications root directory. Example:
```sh
$ cd ~/MyGame
```

* Now, you can install your plugin using the SDKBOX installer. Example:
```sh
$ sdkbox import iap
```

### What Next?
The SDKBOX installer takes care of most of what you need. However, there are still a few manual steps that you must complete. After the installer runs it outputs a list of the remaining steps that you need to perform, referring to the plugin bundle PDF. Example output from running the above command:
```sh
$ sdkbox import iap
_______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.6.9
usage: sdkbox [-h] [-v] [-p [PROJECT]] [-s] [-b [PLUGIN]] [-D SYMBOL]
              [--china] [--dryrun] [--nohelp] [--forcedownload]
              {import,list,restore,symbols,update}

Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/iap/v3-cpp/
Installation Successful :)
```

### Other Installer switches.
The SDKBOX Installer has several switches that you can use. You can always see these by running `sdkbox` by itself or using the `-h` help switch:
```sh
$ <path>/sdkbox
_______ ______  _     _ ______   _____  _     _
|______ |     \ |____/  |_____] |     |  \___/
______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.6.9
usage: sdkbox [-h] [-v] [-p [PROJECT]] [-s] [-b [PLUGIN]] [-D SYMBOL]
              [--china] [--dryrun] [--nohelp] [--forcedownload]
              {import,list,restore,symbols,update}
```

| switch  | alternate switch  | what it does |
| :------------ |---------------:| :-----|
| -h      | --help          |show this help message and exit |
| -v      | --verbose       |specify verbosity level |
| -p PROJECT | --project PROJECT |path to project root (defaults to .) |
| -b PLUGIN | --plugin PLUGIN |specify path to plugin (defaults to .) |
| -q | --nohelp |don't open online documentation after installation. |

|         | --forcedownload |force download of package even if it is already downloaded. |
|         | --dryrun        |test install before performing. |
|         | --china        |use China based server instead of US |

Examples:
```
# Add 'In App Purchase' plugin to your game
$ sdkbox import -b iap -p /path/to/your/cocos2dx/game/
```

```
# The -b option may be omitted and -p too if you are in your project directory
$ sdkbox import iap
```

```
# List all available modules
$ sdkbox list
```

### Staying Up-to-date
The SDKBOX installer automatically checks for updates to itself. It will ask for your permission before updating. This will allow you to stay current and also automatically pull updates to your plugin bundles when they become available.
```sh
_______ ______  _     _ ______   _____  _     _
|______ |     \ |____/  |_____] |     |  \___/
______| |_____/ |    \_ |_____] |_____| _/   \_
Copyright (c) 2015 Chukong Technologies Inc. v0.5.6.9

A newer version of SDKBOX is available, would you like to update to v0.5.11?
Please type Yes, No or Quit Yes
updated SDKBOX v0.5.9 to v0.5.11 at sdkbox
```
