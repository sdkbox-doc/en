<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/soomlagrow/v3-cpp
-->

#Soomla Grow
__Soomla Grow__ is a community-driven analytics dashboard. Developers using GROW can gain valuable insights about their games' performance and compare the data to benchmarks of other games in the GROW community.

##Integration
Open a terminal and use the following command to install the SDKBOX SoomlaGrow plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import soomlagrow
```

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the SoomlaGrow configuration, you need to replace `<game key>` and `<envkey id>` items with your specific [__Soomla ID__](http://soom.la/) account information. Even through you will use the same `<game key>` and `<envkey id>`, if you are targeting both iOS and Android you need to specify it, twice, once for each platform. Example:
```json
"ios" :
{
  "SoomlaGrow":{
              "GameKey":"0cbc07e3-0f0c-4b68-bb0c-061c1b5fb553",
              "EnvKey":"8b865add-4541-4db1-be18-f6c7e5e00564"
          }
}
"android" :
{
  "SoomlaGrow":{
              "GameKey":"0cbc07e3-0f0c-4b68-bb0c-061c1b5fb553",
              "EnvKey":"8b865add-4541-4db1-be18-f6c7e5e00564"
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
