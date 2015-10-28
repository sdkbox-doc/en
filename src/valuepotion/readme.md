<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/valuepotion/v3-cpp
-->

#Valuepotion

##Integration
Open a terminal and use the following command to install the SDKBOX Valuepotion plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import valuepotion
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

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
