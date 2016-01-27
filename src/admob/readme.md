[&#8249; AdMob Doc Home](./)

<h1>AdMob Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX AdMob plugin.
```bash
$ sdkbox import admob
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

```json

{
    "ios": {
        "AdMob":{
            "ads":{
                "home":{
                    "id":"ca-app-pub-3940256099942544/2934735716",
                    "type":"banner",
                    "alignment":"bottom",
                    "width":300,
                    "height":50
                },
                "gameover":{
                    "id":"ca-app-pub-1329374026572143/4185543717",
                    "type":"interstitial"
                }
            }
        }
    },
    "android": {
        "AdMob":{
            "ads":{
                "home":{
                    "id":"ca-app-pub-1329374026572143/2685130917",
                    "type":"banner",
                    "alignment":"bottom",
                    "width":300,
                    "height":100
                },
                "gameover":{
                    "id":"ca-app-pub-1329374026572143/1092476511",
                    "type":"interstitial"
                }
            }
        }
    }
}

```

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
