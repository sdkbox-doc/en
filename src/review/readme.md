[&#8249; Reviews&Ratings Doc Home](./)

<h1>Reviews & Ratings Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]


##Integration
Open a terminal and use the following command to install the SDKBOX Ratings & Reviews plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import review
```

<<[../../shared/notice.md]

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the configuration.
```json
"Review":{
    "ios": {
        "Review":{
            "AppID":"587767923",            //appid, valid on ios
            "DayLimit": 0,                  //days before rate prompt show
            "LaunchLimit": 3,               //launch times before rate prompt show
            "UserEventLimit": 0,            //user event times before rate prompt show, user event increase by invoke userDidSignificantEvent
            "DayForReminding": 1,           //days after user selected reminding later button
            "LaunchForReminding": 2,        //launch times after user selected reminding later button
            "tryPromptWhenInit": true       //try to display prompt when plugin initialization
        }
    },
    "android": {
        "Review":{
            "DayLimit": 0,
            "LaunchLimit": 3,
            "UserEventLimit": 0,
            "DayForReminding": 1,
            "LaunchForReminding": 2,
            "tryPromptWhenInit": true
        }
    }
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

##Custom String
if you want to use custom string when prompt. there have two ways:

 - modify res in `plugin_review_res_project` project (Recommend)

 - set your custom string in sdkbox_config.json

```json
{
    "ios": {
        "Review":{
            ...
            "promptTitle":"cutom tile",
            "promptMessage":"this is custom message",
            "promptCancel":"取消",
            "promptRate":"rate打分",
            "promptRateLater":"稍后later"
            ...
        }
    }
}
```

this way will disable local language, if your app needn't localization, can use this way.

## Amazon Market

if your app is availavle in amazon market, please configure like follow:

```
"Review":{
    "android": {
        "Review":{

            ...

            "market": "amazon"
        }
    }
}
```

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]
