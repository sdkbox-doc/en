[&#8249; OneSignal Doc Home](./)

<h1>OneSignal Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
First, you must sign up for [OneSignal](https://www.google.com/onesignal/).

Second, Open a terminal and use the following command to install the SDKBOX OneSignal plugin.
```bash
$ sdkbox import onesignal
```

For Android, you need more steps:

  1. Replace all 3 of instances __manifestApplicationId__ with your package name in AndroidManifest.xml.


Third,

### iOS precondition
- [iOS Configuration](https://documentation.onesignal.com/docs/generating-an-ios-push-certificate)
- [iOS FAQ](https://documentation.onesignal.com/docs/frequently-asked-questions-1)

### Android precondition
- [Android Configuration](https://documentation.onesignal.com/docs/android-generating-a-gcm-push-notification-key)
- [Android FAQ](https://documentation.onesignal.com/docs/frequently-asked-questions-2)

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

"id": [string] App Id

"project_number": [string] Google Project Number (Android only)

# Optional

"auto_register": [bool] Enable auto register (iOS only)

"vibrate": [bool] Enable vibrate (Android only)

"sound": [bool] Enable sound (Android only)

"notifications_when_active": [bool] Enable notifications when active (Android only)

Example:
```json

{
    "ios": {
        "OneSignal":{
            "debug":false,
            "id":"9a4c9936-62e8-4473-9456-77c50d551870",
            "auto_register":true
        }
    },
    "android": {
        "OneSignal":{
            "debug":false,
            "id":"9a4c9936-62e8-4473-9456-77c50d551870",
            "project_number":"517386718969",
            "vibrate":true,
            "sound":true,
            "notifications_when_active":false
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

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]
