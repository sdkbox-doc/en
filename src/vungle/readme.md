<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/vungle/v3-cpp
-->

#Vungle

##Integration
Use the following command to install the SDKBOX Vungle plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import -b vungle
```

##Extra steps
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Vungle configuration, you need to replace `<vungle id>`  with your specific [Vungle](http://vungle.com) Publisher account information.
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

##Usage
<<[usage.md]

<<[api-reference.md]
