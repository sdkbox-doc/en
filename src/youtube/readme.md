<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/youtube/v3-cpp
-->

#Youtube

##Integration
Open a terminal and use the following command to install the SDKBOX Youtube plugin.
```bash
$ sdkbox import youtube
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

If you want to display youtube vidoe in your app, you have to register a new youtube API key [here](https://developers.google.com/youtube/android/player/register#Create_API_Keys) and put in `developer_key` section of the `sdkbox_config.json`
```json
{
    "ios" :
    {
        "Youtube":
        {
            "developer_key":"AIzaSyDMuDjrVSL3uj_QvlI3bbjKn5I4nNB1XZk"
        }
    },
    "android" :
    {
        "Youtube":
        {
            "developer_key":"AIzaSyDMuDjrVSL3uj_QvlI3bbjKn5I4nNB1XZk"
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
