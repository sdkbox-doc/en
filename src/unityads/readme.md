[&#8249; UnityAds Doc Home](./)

<h1>UnityAds Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX UnityAds plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import unityads
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the UnityAds configuration, you need to replace `<gameId>` item with your specific [__UnityAds__](https://unityads.unity3d.com/admin/) account information.
```json
"UnityAds":{
    "gameId": "1493045",
    "testMode": true,
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
