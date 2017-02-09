[&#8249; PhunwareAds Doc Home](./)

<h1>Phunware（Ads）Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX [PhunwareAds](http://ads.tapit.com/publisher/dashboard) plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import phunwareads
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the PhunwareAds configuration.
```json
"PhunwareAds":{
    "debug":true,
    "ads": {
        "banner":{
            "id":"7268",
            "type":"banner",
            "test_mode":true
        },
        "interstitial":{
            "id":"7271",
            "type":"interstitial"
        },
        "video":{
            "id":"22219",
            "type":"video"
        },
        "reward":{
            "id":"78393",
            "type":"reward"
        },
        "page":{
            "id":"76663",
            "type":"page"
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
