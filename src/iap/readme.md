<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/iap/v3-cpp
-->

#In-App Purchase, C++

##Integration
Use the following command to install the SDKBOX IAP plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import -b iap
```

##Extra steps
<<[extra-step.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of IAP configuration, you need to replace `<put the product id for ios here>` with the product id from your [iTunes Connect](http://itunesconnect.apple.com) or [Google Play Console](https://play.google.com/apps/publish)
```json
"ios" :
{
    "iap":{
        "items":{
            "remove_ads":{
                "id":"<put the product id for ios here>"
            }
        }
    }
},
"android":
{
    "iap":{
        "key":"put your googleplay key here",
        "items":{
          "remove_ads":{
              "id":"<put the product id for android here>"
          }
        }
    }
}
```

##Usage
<<[usage.md]

<<[api-reference.md]
