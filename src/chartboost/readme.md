[&#8249; Chartboost Doc Home](./)

<h1>Chartboost Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX Chartboost plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import chartboost
```

<<[../../shared/notice.md]
Follow [this link](https://www.chartboost.com/blog/2015/09/how-to-prepare-your-mobile-game-for-ios-9/)

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
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

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
