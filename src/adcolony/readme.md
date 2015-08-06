<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/adcolony/v3-cpp
-->

#AdColony

##Integration
Open a terminal and use the following command to install the SDKBOX AdColony plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import adcolony
```

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

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

##Manual Integration
If the *SDKBOX Installer* __fails__ to complete successfully, it is possible to integrate SDKBOX manually. If the installer complete successfully, please __do not__ complete anymore of this document. It is not necessary.

These steps are listed last in this document on purpose as they are seldom needed. If you find yourself using these steps, please, after completing, double back and re-read the steps above for other integration items.

<<[manual_ios.md]

<<[manual_android.md]
