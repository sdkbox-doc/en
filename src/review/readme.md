<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/review/v3-cpp
-->

#Review
Review is a plugin that will help remind your users to review your app on the App Store.

##Integration
Open a terminal and use the following command to install the SDKBOX Review plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import review
```

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Review configuration.
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

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]