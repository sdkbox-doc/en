[&#8249; SdkboxAds Doc Home](./)

<h1>SdkboxPlay Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites

###Google play
 + Follow [this instructions](https://developers.google.com/games/services/console/enabling#step_2_add_your_game_to_the_dev_console) to enable game services for your game and create a linked application. Otherwise, the app won’t be able to make connections to google play. It's recommended to follow the instruction rigorously to avoid any issues.

 + Use developer console to configure leaderboards and achievements.

 + Find your app id and you'll need to replace replace it in the `AndroidManifest.xml` later
   ![](../../imgs/gps_app_id.jpg)

###Google Play check list

1. Application id (string.xml)
2. App Release mode
3. Cloud save enalbe
4. Publish to Alpha/Bete test
5. Add your test account to tester list
6. SHA-1 keys


###Game Center
 + Enable Game Center on XCode.
 + Use itunes connect to configure [leaderboards](https://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Leaderboards/Leaderboards.html#//apple_ref/doc/uid/TP40013726-CH2-SW47) and [achievements](https://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Achievements/Achievements.html#//apple_ref/doc/uid/TP40013726-CH3-SW3).
 + Make sure Leaderboard and Achievements are live before testing

###Cloud Save
 + Enable iCloud on Xcode. ![](../../imgs/cloud_save_ios.png)
 + Enable `Saved Games` on [Google Play Console](https://play.google.com/apps/publish/signup/) ![](../../imgs/cloud_save_android.png)

 **NOTE**: In 2.3.14 cloud save is enable as default, it cause user can't sign-in on android if you do not enable `Save Games` on Google Play Console.

##Integration
Open a terminal and use the following command to install the SDKBOX SdkboxPlay plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import sdkboxplay
```

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration

#### Replace App ID
You should replace your app_id in `AndroidManifest.xml`

1. replace following line

```
<meta-data android:name="com.google.android.gms.games.APP_ID" android:value="_your_app_id_" />
```
with
```
<meta-data android:name="com.google.android.gms.games.APP_ID" android:value="@string/app_id" />
```

2. add following line to `<Your Project>\proj.android\res\values\strings.xml`

```
<string name="app_id">_your_app_id_</string>
```

#### Update sdkbox_config.json
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the SdkboxAds configuration:
```json
    "sdkboxplay" : {
      "leaderboards" : [
        {
          "id" : "CgkI0sux8sMWEAIQAA",
          "name" : "ldb1"
        }
      ],
      "achievements" : [
        {
          "id" : "CgkI0sux8sMWEAIQAg",
          "name" : "ten-games",
          "incremental" : false
        },
        {
          "id" : "CgkI0sux8sMWEAIQAw",
          "name" : "hunter",
          "incremental" : false
        },
        ...
      ],
      "debug" : true,
      "show_achievement_notification": true,
      "connect_on_start" : false
    }

```


As it can be seen, leaderboards and achievements have a human readable name, and a machine generated id. This is on purpose so that the same API can be used between platforms. While Google play generated random ids like the ones shown, iOS Game Center will be more human friendly.
In either case, the developer will reference leaderboards and achievements by a name of his choice, like in the example shown.

if you don't want popup show when unlock achievement, you can set 'show_achievement_notification' false.

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]

<<[../shared/qa.md]

<<[../shared/cloud_save.md]
