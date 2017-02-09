[&#8249; PhunwareMessaging Doc Home](./)

<h1>Phunware Integration Guide（Messaging）</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX [Phunware Messaging](http://maas.phunware.com/) plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import phunwaremessaging
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app.

Here is an example of the PhunwareMessaging configuration.
```json
{
    "ios": {
        "PhunwareMessaging":{
            "debug":true,
            "api_id":"1569",
            "access_key":"b49ea8dc7bdc4a056d51e8b72a8f3a575047a4aa",
            "signature_key":"b3f090e90cefe5b9535b0703d94a89a10f8a934b"
        }
    },
    "android": {
        "PhunwareMessaging":{
            "debug":true,
            "api_id":"1527",
            "access_key":"c11a65cb3deeca49aac6f8c0e794b7bc68e1481a",
            "signature_key":"1580b669f2edb1c810c29e52e9a754f443f6215a",
            "env":"dev"
        }
    }
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

##Notice

SDKBox PhunwareAds v3.5.1+ android Required:

1. Build SDK Version - 23
2. Compile SDK Version - 23

if you get `miss HttpClient` error when set build sdk to 23:

1. if use eclipse, copy `$ANDROID_SDK_ROOT/platforms/android-23/optional/org.apache.http.legacy.jar` to your project `libs` folder
2. if use android studio, add this to your gradle:

``` groovy
android {
    useLibrary 'org.apache.http.legacy'
}
```
