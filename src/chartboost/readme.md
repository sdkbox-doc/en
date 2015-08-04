<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/chartboost/v3-cpp
-->

#Chartboost

##Integration
Open a terminal and use the following command to install the SDKBOX Chartboost plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import chartboost
```

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Chartboost configuration, you need to replace `<CHARTBOOST ID>` and `<CHARTBOOST SIGNATURE>` items with your specific [Chartboost](https://www.chartboost.com) account information.
```json
"Chartboost":{
    "id":"<CHARTBOOST ID>",
    "signature":"<CHARTBOOST SIGNATURE>",
    "ads":{
        "Default":{
            "type":"interstitial"
        },
        "Level Complete":{
            "type":"rewarded_video"
        },
        "MoreApp":{
            "type":"more_app"
        }
    }
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_ios.md]

<<[manual_android.md]
