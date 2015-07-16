<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/vungle/v3-cpp
-->

#Vungle

##Integration
Use the following command to install the SDKBOX Vungle plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import vungle
```

##Extra steps
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
