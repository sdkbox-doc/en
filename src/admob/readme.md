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


##FAQ
1. webthread JSC::executableAllocator::allocate , Javascript crash

   ```c++
   #To solve this you can set the following environment variable to disable the buggy JIT in iOS 11:
   setenv("JSC_useJIT", "false", 0);
   // https://forums.developer.apple.com/thread/90411
   ```

##Notice

For reward video on Android, you need to check your project sdk configuation:

* target sdk: set target sdk 24+ in project.properties. e.g. `target=android-24`
* min sdk: set minSdkVersion 14+ in AndroidManifest.xml, e.g. `<uses-sdk android:minSdkVersion="14" />`

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

type:

    - "banner"
    - "interstitial"
    - "rewarded_video"

alignment:

    - "top"
    - "bottom"
    - "left"
    - "right"
    - "center"
    - "top_left"
    - "top_right"
    - "bottom_left"
    - "bottom_right"

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

#### Apps targeted for Children
Apps that target for children can specify `"is_designed_for_families": true`

#### Auto cache

The plugin will auto cache the first Ad of one Ad type. It also will cache the interstitial/Reward Ad after it close.

#### Test ID (Google)

[Android](https://developers.google.com/admob/ios/test-ads)

| type               | id                                     |
| ------------------ | -------------------------------------- |
| Banner             | ca-app-pub-3940256099942544/6300978111 |
| Interstitial       | ca-app-pub-3940256099942544/1033173712 |
| Interstitial Video | ca-app-pub-3940256099942544/8691691433 |
| Rewarded Video     | ca-app-pub-3940256099942544/5224354917 |

[iOS](https://developers.google.com/admob/android/test-ads)

| type               | id                                     |
| ------------------ | -------------------------------------- |
| Banner             | ca-app-pub-3940256099942544/2934735716 |
| Interstitial       | ca-app-pub-3940256099942544/4411468910 |
| Interstitial Video | ca-app-pub-3940256099942544/5135589807 |
| Rewarded Video     | ca-app-pub-3940256099942544/1712485313 |

#### Example:
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
                    "height":50,
                    "is_designed_for_families": false
                },
                "gameover":{
                    "id":"ca-app-pub-1329374026572143/4185543717",
                    "type":"interstitial",
                    "is_designed_for_families": true
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
                    "height":100,
                    "is_designed_for_families": false
                },
                "gameover":{
                    "id":"ca-app-pub-1329374026572143/1092476511",
                    "type":"interstitial",
                    "is_designed_for_families": true
                }
            }
        }
    }
}

```

##Usage
<<[usage.md]

<<[sdkboxads.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]
