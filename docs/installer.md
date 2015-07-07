# SDKBOX: Installing SDKBOX Plugins using the Installer

## Step 1: Preparing to run the SDKBOX Installer
Before you can run the SDKBOX installer you need to do a few things.
* make sure you know the path to where you downloaded the SDKBOX installer. (you can always put it in `/usr/local/bin`)
* make sure you know the path to where you downloaded the SDKBOX plugin bundles.

## Step 2. Installing a Plugin using the SDKBOX Installer
Now we are ready to install a plugin! There isn't much to it. Ready?

### Installing for OS X
* From a command-line, `cd` to your applications root directory. Example:
```
cd ~/MyGame
```

* Now, you can install your plugin using the SDKBOX installer, noting the locations of where you placed the installer and the plugin bundles. Example:
```
<path>/sdkbox import -b ~/Downloads/sdkbox-iap_cpp_v1.1.tar.gz
```

### What Next?
The SDKBOX installer takes care of most of what you need. However, there are still a few manual steps that you must complete. After the installer runs it outputs a list of the remaining steps that you need to perform, referring to the plugin bundle PDF. Example output from running the above command:
```
$ sdkbox -b ../sdkbox-iap_cpp_v1.1/ import
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright © 2015 Chukong Technologies Inc. v0.1

 Remaining Manual Steps:
 Android Integration:
 Step 2.5 - modify Cocos2dxActivity.java
 Step 2.5 - modify YourGameName.java
 Cocos2d-JS specific
 Step 3.2 - add appropriate headers for this plugin to your class.
 Step 3.2 - add appropriate call to initialize the Javascript callbacks.
 Step 3.2 - call sdkbox.IAP.init(); where appropriate in your code. We recommend to do this in the app.js
 Installation Successful :)
```

### Other Installer switches.
The SDKBOX Installer has several switches that you can use. You can always see these by running `sdkbox` by itself or using the `-h` help switch:
```
$ <path>/sdkbox
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright © 2015 Chukong Technologies Inc. v0.1

usage: sdkbox [-h] [-v] [-p PROJECT] [-b PLUGIN] [--yes] [--dryrun]
              {import,restore,symbols,api}
```

| switch  | alternate switch  | what it does |
| :------------ |---------------:| :-----|
| -h      | --help          |show this help message and exit |
| -v      | --verbose       |specify verbosity level |
| -p PROJECT | --project PROJECT |path to project root (defaults to .) |
| -b PLUGIN | --plugin PLUGIN |specify path to plugin (defaults to .) |
|         | --dryrun        |test install before performing. |

### Staying Up-to-date
The SDKBOX installer automatically checks for updates to itself. It will ask for your permission before updating. This will allow you to stay current and also automatically pull updates to your plugin bundles when they become available.
```
 _______ ______  _     _ ______   _____  _     _
 |______ |     \ |____/  |_____] |     |  \___/
 ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright © 2015 Chukong Technologies Inc. v0.1

A newer version of SDKBOX is available, would you like to update to v0.5?
Please type Yes, No or Quit Yes
updated SDKBOX v0.1 to v0.5 at sdkbox
```
