[&#8249; Appnext Doc Home](./)

<h1>Appnext Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
First, you must sign up for [Appnext](https://www.appnext.com/) and setup your app.

Second, Open a terminal and use the following command to install the SDKBOX Appnext plugin.
```bash
$ sdkbox import appnext
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

- id

- cache:

    - true  : cache ad when app start, only support cache one ad for a type
    - false [default]: dont cache ad

- type:

    - "interstitial"
    - "fullscreen"
    - "reward"

#### options

- creative_type:

    - "managed"
    - "video"
    - "static"

- progress_type:

    - "clock"
    - "bar"
    - "none"

- video_lenght:

    - "short"
    - "long"

- button_text
- button_color
- categories
- postback
- can_close

- skip_text
- mute
- autoplay

- progress_color
- show_close_button

more information:

- [https://selfservice.appnext.com/Apps/Tools.aspx#android/interstitial-sdk/native-app/advanced_settings](https://selfservice.appnext.com/Apps/Tools.aspx#android/interstitial-sdk/native-app/advanced_settings)
- [https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/advanced_settings](https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/advanced_settings)
- [https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/app_categories](https://selfservice.appnext.com/Apps/Tools.aspx#android/full-screen/rewarded-sdk-beta/app_categories)

Example:
```json

{
    "ios": {
        "Appnext":{
            "debug":true,
            "ads": {
                "default": {
                    "cache":true,
                    "id":"6d596bc5-b4c1-48ca-be95-3758fd29a3a5",
                    "type":"interstitial"
                }
            }
        }
    },
    "android": {
        "Appnext":{
            "debug":true,
            "ads": {
                "default": {
                    "cache":true,
                    "id":"2f6850dd-190a-499d-aa50-1f4a3dd1ed5f",
                    "type":"interstitial",

                    "button_text":"Button Text",
                    "button_color":"#6AB344",
                    "categories":"Action,Puzzle",
                    "postback":"postback",
                    "can_close":false,

                    "skip_text":"Skip Text",
                    "mute":false,
                    "autoplay":true,
                    "creative_type":"managed"
                },
                "fullscreen": {
                    "cache":true,
                    "id": "17322152-1ef3-4e72-9677-eaf7c09f1054",
                    "type": "fullscreen",

                    "button_text":"Button Text",
                    "button_color":"#6AB344",
                    "categories":"Action,Puzzle",
                    "postback":"postback",
                    "can_close":false,

                    "progress_type":"clock",
                    "progress_color":"#ffffff",
                    "show_close_button":true,
                    "video_lenght":"short"
                },
                "reward": {
                    "cache":true,
                    "id": "8d653a16-129b-4c14-bd22-fae625f70cf4",
                    "type": "reward",

                    "button_text":"Button Text",
                    "button_color":"#6AB344",
                    "categories":"Action,Puzzle",
                    "postback":"postback",
                    "can_close":false,

                    "progress_type":"bar",
                    "progress_color":"#ffff00",
                    "show_close_button":false,
                    "video_lenght":"long"
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
