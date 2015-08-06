<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/vungle/v3-cpp
-->

#Vungle

##Integration
Open a terminal and use the following command to install the SDKBOX Vungle plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import vungle
```

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

## Configuration
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

<<[sdkbox-config-encrypt.md]

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

##Manual Integration
If the *SDKBOX Installer* __fails__ to complete successfully, it is possible to integrate SDKBOX manually. If the installer complete successfully, please __do not__ complete anymore of this document. It is not necessary.

These steps are listed last in this document on purpose as they are seldom needed. If you find yourself using these steps, please, after completing, double back and re-read the steps above for other integration items.

<<[manual_ios.md]

<<[manual_android.md]
