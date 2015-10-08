<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/soomlagrow/v3-cpp
-->

#GROW
GROW is [SOOMLA](http://soom.la)'s flagship, community-driven, data network. Mobile game studios can take advantage of GROW's Analytics, Whales Reports and Insights in order to gain valuable knowledge about users' behavior in other games.
Information about GROW can be found on the [Knowledge Base](http://know.soom.la/).

##Integration
1. If you still didn't sign up on the GROW Dashboard, go ahead and do it [here](https://soom.la/signup/sdkbox).

2. Open a terminal and use the following command to install GROW's SDKBOX plugin. Make sure you setup SDKBOX installer correctly.

  ```bash
  $ sdkbox import soomlagrow
  ```

<<[../../shared/notice.md]

## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you will have to modify before you use in your own app.

Here is an example of the GROW configuration, you need to replace `<gameKey>` and `<envkey>` items with the ones you were given by the [GROW Dashboard](http://dashboard.soom.la). You will probably use the same `<gameKey>` and `<envKey>` for Android and iOS but you will still need to specify it twice, once for each platform. Example:

```json
"ios" :
{
  "soomlaGrow":{
              "gameKey":"0cbc07e3-0f0c-4b68-bb0c-061c1b5fb553",
              "envKey":"8b865add-4541-4db1-be18-f6c7e5e00564"
          }
}
"android" :
{
  "soomlaGrow":{
              "gameKey":"0cbc07e3-0f0c-4b68-bb0c-061c1b5fb553",
              "envKey":"8b865add-4541-4db1-be18-f6c7e5e00564"
          }
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
