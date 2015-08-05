<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/flurryanalytics/v3-cpp
-->

#Flurry Analytics

##Integration
Open a terminal and use the following command to install the SDKBOX Flurry Analytics plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import flurryanalytics
```

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Google Analytics configuration, you need to replace `<API KEY>`  with your specific [__Flurry Analytics ID__](http://www.flurry.com/solutions/analytics) account information.
Here is an example adding `FlurryAnalytics` to iOS:
```json
"FlurryAnalytics":{
            "APIKey":"<API KEY>",
            "AppVersion":"V0.1",
            "Debug":false,
            "Level":2,
            "SessionTimeout":10,
            "CrashReport":true
}
```

Adding `FlurryAnalytics` to Android is a bit different as it supports __locations__, __pulse__ and __origin__ settings. Here is an example adding `FlurryAnalytics` to Android:
```json
"FlurryAnalytics":{
            "APIKey":"<API KEY>",
            "AppVersion":"V0.1",
            "Debug":false,
            "LogEvent":true,
            "Level":2,
            "SessionTimeout":10,
            "CrashReport":true,
            "LocationReport":true,
            "DefLocationLat":104.06,
            "DefLocationLon":30.67,
            "Pulse":true,
            "Origin":[
                {
                    "OriginName":"sdkbox",
                    "OriginVersion":"v0.1",
                    "OriginParams":{
                        "Key1":"Val1",
                        "Key2":"Val2",
                        "Key3":"Val3"
                    }
                },
                {
                    "OriginName":"sdkbox",
                    "OriginVersion":"v0.1"
                }
            ]
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_ios.md]

<<[manual_android.md]
