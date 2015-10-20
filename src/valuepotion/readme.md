<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/valuepotion/v3-cpp
-->

#Valuepotion

##Integration
Open a terminal and use the following command to install the SDKBOX Valuepotion plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import valuepotion
```

<<[../../shared/notice.md]

## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the ValuePotion configuration, you need to replace `<client id>` and `<secret key>` items with your specific [__Valuepotion ID__](https://www.valuepotion.com/) account information.
`<sender id>` item valid on android, which is GCM(google cloud message) project number id
```json
"ValuePotion":{
    "clientId":"9666f9668a4db516c8aaea439464da44",
    "secretKey":"1c110ebcdeeda25d",
    "senderId":"111111"
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
