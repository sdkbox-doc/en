# use SDKBox to import local plugin

## Introduction

Some projects may need to continue using SDKBox for various reasons. Here's how to install plugins locally using SDKBox.

## Steps

### Download plugin
    - All installed plugins will be stored in `~/.sdkbox/plugins` (personal directory `%HOME%/.sdkbox/plugins` for Windows).
    - Also, you can download plugin by yourself.

        1. Browse URL `http://download.sdkbox.com/installer/v1/manifest.json`
        2. Replace `BUNDLE_NAME` in `http://download.sdkbox.com/installer/v1/BUNDLE_NAME` with the value of `bundle`. and then you can get the download URL of plugin(iap as an example), `http://download.sdkbox.com/installer/v1/sdkbox-iap_v2.7.7.0.tar.gz`.
        3. Download and backup

### Install plugin.
    - import plugin in terminal with command: `sdkbox import /local/path/to/plugin -p /project/path`.

### Use cases of import local plugin 

- Install local plugin into creator2.

`sdkbox import ~/.sdkbox/plugins/sdkbox-iap_v2.7.7.0 -p ./build/jsb-link`

```bash
hugo@hugodeMacBook-Pro creatorTest % sdkbox import ~/.sdkbox/plugins/sdkbox-iap_v2.7.7.0 -p ./build/jsb-link
  _______ ______  _     _ ______   _____  _     _
  |______ |     \ |____/  |_____] |     |  \___/
  ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright (c) 2016-2020 SDKBOX Inc. v1.4.6.1
 Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/iap/v3-js/
 Installation Successful :)
 > Log file = /Users/hugo/.sdkbox/log/sdkbox-log-2021-12-06.sdkbox.temp
```

- Install local plugin into creator3.

`sdkbox import /Users/hugo/Downloads/sdkbox-iap_v2.7.7.0.tar.gz -p /Users/hugo/Documents/work/t/creator3Test --nohelp`

```bash
hugo@hugodeMacBook-Pro cocos2dxTest % sdkbox import /Users/hugo/Downloads/sdkbox-iap_v2.7.7.0.tar.gz -p /Users/hugo/Documents/work/t/creator3Test --nohelp
  _______ ______  _     _ ______   _____  _     _
  |______ |     \ |____/  |_____] |     |  \___/
  ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright (c) 2016-2020 SDKBOX Inc. v1.4.6.1
 > Log file = /Users/hugo/.sdkbox/log/sdkbox-log-2021-12-06-4.sdkbox.temp
```

- Install local plugin into Cocos2dx.

`sdkbox import ~/.sdkbox/plugins/sdkbox-admob_v2.7.6.1 -p .`

```bash
hugo@hugodeMacBook-Pro cocos2dxTest % sdkbox import ~/.sdkbox/plugins/sdkbox-admob_v2.7.6.1 -p .
  _______ ______  _     _ ______   _____  _     _
  |______ |     \ |____/  |_____] |     |  \___/
  ______| |_____/ |    \_ |_____] |_____| _/   \_
 Copyright (c) 2016-2020 SDKBOX Inc. v1.4.6.1
 Please reference the online documentation to finish the integration:
http://sdkbox-doc.github.io/en/plugins/admob/v3-cpp/

  1. iOS:
  > Replace `ca-app-pub-3940256099942544~1458002511` with `proj.ios_mac/ios/Info.plist` file;
  > Replace `ca-app-pub-3940256099942544~1458002511` with your publish id with `sdkbox_config.json` file;

  2. Android:
  > Replace `ca-app-pub-3940256099942544~3347511713` with your publish id with `AndroidManifest.xml` file;
  > Replace `ca-app-pub-3940256099942544~3347511713` with your publish id with `sdkbox_config.json` file;

 Installation Successful :)
 > Log file = /Users/hugo/.sdkbox/log/sdkbox-log-2021-12-06-3.sdkbox.temp
```

