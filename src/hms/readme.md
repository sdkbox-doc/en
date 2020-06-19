[&#8249; HMS Doc Home](./)

<h1>Huawei Mobile Services Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

## Integration
Open a terminal and use the following command to install the SDKBOX HMS plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import hms
```

<<[../../shared/notice.md]

## Extra steps

### Android Steps

you should add this code `com.sdkbox.plugin.PluginHMS.ApplicationInit(this);` to Application::onCreate. modification may like follow:

```java
public class YourApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        com.sdkbox.plugin.PluginHMS.ApplicationInit(this); // add this line
    }

    ...
}
```

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app.

Here is an example of the HMS configuration.

```json
"ios" :
{
    "hms":{
    }
},
"android":
{
    "hms":{
        "archive": true,
        "key": "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAn9U6yC1QI8cXGRkOQxO9QG/WV8dR4jZDCYt/GJBM4OTTtRZeAIEyVifGPutwMAkPBLgdUsJwHuA2t2jrBAi/nagYJvh8UIazKJv5C4Hykw5Z2iKTWMmiMK9rQ2tMtRTAMiY+LwfaOH2258bEyt8mDQxyG3aRSAH28mZki/nGEbNfx7ZY9By/SSkuaCEWRDNYdiWkGDuZLhf8D97DoJJc6tTnrDPmzf1QqkVDjjudkHJwgCMWpLVACzGGuo4YQYt98Pu9cqbiYWJqSHqEbPYN0AmGXdJw+tO5f1wPcZWnJhn4JqCFmD9i/dSENNJWXVDgJc0DG2PiWX5j+qUaT7WkZMs4/WFtL6VRdRUDzITqYwKUUBYENVvkfdKlhjh+6V4BFKPsipvjOsRdXDpZ7sC6MY/7yn0eMOH3RoIQoiWeGYkxRTkKhdm/QQ/Xv/dvMbiicsNmUIkBce3w4hQG9XlhgjNrl5rI4p9Ho3Stq48s7DJlhWuUE6pXcjo2TJUSJ9+nAgMBAAE=",
        "items": {
            "remove_ads": {
                "type": "non_consumable",
                "id": "com.sdkbox.test.app.sample.noad"
            },
            "coin": {
                "id": "com.sdkbox.test.app.sample.coin1"
            },
            "vip": {
                "type": "subs",
                "id": "com.sdkbox.test.app.sample.vip"
            }
        },
        "achievements": [{
            "name": "freshman",
            "id": "A7346279E90AB8910AAC0CB71E552BFA2505DFD7591C79457F84D6B95F50FFEC",
            "incremental": false
        }, {
            "name": "3shoot",
            "id": "BA8B1A486D422AEF28FF82F9BFF85C3F156824396E0BB62D92BECC63C3CAC46A",
            "incremental": true
        }, {
            "name": "5shoot",
            "id": "001D38EC9E1A80A52ED3F47BFBA35F4B5BDF3776180A2B9AD778800C45CD6540",
            "incremental": true
        }],
        "events": [{
            "name": "gencoin",
            "id": "912764D10F0988B9DCB041A4E6FE453BCBDEDC4E35708A60E33C2DEBF05F2D2E"
        }, {
            "name": "consumecoin",
            "id": "E8688F3D9625572F462F5999E7F83EB5628E0FC1F2044E84D026EC4AB33C09F5"
        }],
        "rankings": [{
            "name": "shooter",
            "id": "C8B96FA1EDFC2D87DFE9491409440E3F8B2E39AFB8BD7E95C3BE337FC207C253"
        }]
    }
}
```

And you must download `agconnect-services.json` from HMS developer site, and put it in `proj.android/app`.

### HMS for iOS

-   HMS is not supported iOS, we implement empty on iOS.

### Test HMS for android

1. Create App in AppGallery
2. Enable Module you need(enable AccountKit if you need)
3. Configure app signature
4. download app info `agconnect-services.json`

HMS official [Document](https://developer.huawei.com/consumer/hms)

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[../../shared/remote_application_config.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]


