[&#8249; IAP Doc Home](./)

<h1>In-App Purchase Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX IAP plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import iap
```

<<[../../shared/notice.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the IAP configuration, you need to replace `<put the product id for ios here>` with the product id from your [iTunes Connect](http://itunesconnect.apple.com) or  replace `<put your googleplay key here>` from your [Google Play Console](https://play.google.com/apps/publish)
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
        "key":"<put your googleplay key here>",
        "items":{
          "remove_ads":{
              "id":"<put the product id for android here>"
          }
        }
    }
}
```

If you have IAP items that are __non-consumable__ or __subscription__, it is also necessary to supply this for each item in your `sdkbox_config.json`. Only __Android__ requires this step. Taking the same *json* above your config might now look like this example:
```json
"android":
{
    "iap":{
        "key":"<put your googleplay key here>",
        "items":{
          "remove_ads":{
              "id":"<put the product id for android here>",
              "type":"non_consumable"
          }
        }
    }
}
```


<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[../../shared/remote_application_config.md]

<<[../shared/receipts_verification.md]

<<[promoting_iap.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]


