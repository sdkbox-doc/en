<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/adcolony/v3-cpp
-->

#AdColony

##Integration
Use the following command to install the SDKBOX AdColony plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import adcolony
```

##Extra steps
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the AdColony configuration, you need to replace `<app id>` and `<zone id>` items with your specific [AdColony](https://clients.adcolony.com/login) account information.
```json
"AdColony":{
    "id":"<app id>",
    "debug":true,
    "ads":{
        "video":{
            "zone": "<zone id>",
            "v4vc": false
        },
        "v4vc":{
            "zone": "<zone id>",
            "v4vc": true,
            "pre_popup" : true,
            "post_popup": true
        }
    }
}
```

##Usage
<<[usage.md]

<<[api-reference.md]
