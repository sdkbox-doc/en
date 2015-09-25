<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/adcolony/v3-cpp
-->

#AdColony

##Integration
Open a terminal and use the following command to install the SDKBOX AdColony plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import adcolony
```

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the AdColony configuration, you need to replace `<app id>` and `<zone id>` items with your specific [AdColony](https://clients.adcolony.com/login) account information.
```json
"AdColony":{
    "id":"<app id>",
    "debug":true,
    "ads":{
        "video":{
            "zone": "<zone id>",
            "v4vc": false
        },
        "v4vc":{
            "zone": "<zone id>",
            "v4vc": true,
            "pre_popup" : true,
            "post_popup": true
        }
    }
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

##Manual Integration For Android and Android Studio
Both __Android__ development using a command-line and using __Android Studio__ are supported. `proj.android` will be used as our `<project_root>` for __command-line__ development, while `proj.android-studio` will be used as our `<project_root>` for __Android Studio__.

<<[manual_android.md]

<<[extra-step.md]
<<[proguard.md]
