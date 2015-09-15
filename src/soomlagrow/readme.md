<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/soomlagrow/v3-cpp
-->

#GROW
GROW is [SOOMLA](http://soom.la)'s flagship, community-driven, data network. Mobile game studios can take advantage of GROW's Anaytics, Whales Reports and Insights in order to gain valuable knowledge about users' behavior in other games.
Information about GROW can be found on the [Knowledge Base](http://know.soom.la/).

##Integration
If you still didn't sign up on the GROW Dashboard, go ahead and do it [here](http://dashboard.soom.la).

Open a terminal and use the following command to install GROW's SDKBOX plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import soomlagrow
```

## Configuration
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

<<[manual_android.md]

<<[extra-step.md]
<<[proguard.md]
