<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/appodeal/v3-cpp
-->

#Appodeal

##Integration
Open a terminal and use the following command to install the SDKBOX Appodeal plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import appodeal
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Appodeal configuration, you need to replace `<app_key>` items with your specific [__Appodeal Key__](http://www.appodeal.com/) account information.
```json
"Appodeal":{
    "app_key":"2cfc9cc638980eb7f5ff35d6eb63dbe404503151ccc451ed"
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
