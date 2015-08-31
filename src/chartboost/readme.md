<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/chartboost/v3-cpp
-->

#Chartboost

##Integration
Open a terminal and use the following command to install the SDKBOX Chartboost plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import chartboost
```

## Changelog

version-x.y.z:
1. `register_PluginChartboostJS_helper` -> `register_all_PluginChartboostJS_helper`
2. `register_PluginChartboostLua_helper` -> `register_all_PluginChartboostLua_helper`
3. Update Chartboost iOS SDK to 5.5.3
4. Update Chartboost Android SDK to 5.5.3

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

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]