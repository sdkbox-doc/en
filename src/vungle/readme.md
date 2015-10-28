<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/vungle/v3-cpp
-->

#Vungle

##Integration
Open a terminal and use the following command to install the SDKBOX Vungle plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import vungle
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Vungle configuration, you need to replace `<vungle id>`  with your specific [Vungle](http://vungle.com) Publisher account information.
Here is an example adding `Vungle` to iOS:
```json
"Vungle" :
{
    "id":"<vungle id>",
    "ads":{
        "video":{

        },
        "reward":{
            "incentivized" : true
        }
    }
}
```

<!--<<[sdkbox-config-encrypt.md]-->

Adding `Vungle` to Android is a bit different as it supports __sound__ and
__backbutton__ settings. Here is an example adding `Vungle` to Android:
```json
"Vungle" :
{
    "id":"<vungle id>",
    "ads":{
        "video":{
            "sound" : true,
            "backbutton" : true
        },
        "reward":{
            "sound" : false,
            "backbutton" : false,
            "incentivized" : true
        }
    }
}
```

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
