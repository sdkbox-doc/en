<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/facebook/v3-cpp
-->

#Facebook

##Integration
Use the following command to install the SDKBOX Facebook plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import facebook
```

##Extra steps

The following step assuming you already registered as a Facebook Developer
And created a new __APP__ on Facebook

###Setup iOS
* Configure your __APP__ following [iOS Quick Start Guide](https://developers.facebook.com/quickstarts/?platform=ios)
* Apply the code change to `AppController.mm` instead of `AppDelegate.m`

###Setup Android
* Configure your __APP__ on Facebook follow [Android Quick Start Guide](https://developers.facebook.com/quickstarts/?platform=android)
* Open `res/values/strings.xml` and replace `facebook_app_id` with your `Facebook App ID`
* Open `AndroidManifest.xml` and replace `_replace_with_your_app_id_` with your `Facebook App ID`
* Open `project.properties` and change target to `target=android-15`

<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the Facebook configuration you can enable/disable debug mode for Facebook here
```json
"Facebook":
{
    "debug":true
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]
