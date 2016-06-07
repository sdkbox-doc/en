[&#8249; AdMob Doc Home](./)

<h1>AdMob Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
First, you must sign up for [AdMob](https://www.google.com/admob/).

Second, Open a terminal and use the following command to install the SDKBOX AdMob plugin.
```bash
$ sdkbox import admob
```

Third, please read the [iOS FAQ](https://developers.google.com/admob/ios/quick-start#faq) and [Android FAQ](https://developers.google.com/admob/android/quick-start#faq)

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

type:

    - "banner"
    - "interstitial"

alignment:

    - "top"
    - "bottom"
    - "left"
    - "right"
    - "center"
    - "top_left" or "left_top"
    - "top_right" or "right_top"
    - "bottom_left" or "left_bottom"
    - "bottom_right" or "right_bottom"

width x height:

    - 320x50
    - 468x60
    - 320x100
    - 728x90
    - 300x250
    - 160x600
    - 0x0    # 0x0 means auto size, smart banner.

#### Smart banner

```
    "width":0,
    "height":0
```

#### Auto cache

The plugin will auto cache the first Ad of one Ad type. It also will cache the interstitial Ad after
it close.

Example:
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
