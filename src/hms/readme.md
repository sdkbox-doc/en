[&#8249; HMS Doc Home](./)

<h1>Huawei Mobile Services Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX HMS plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import hms
```

<<[../../shared/notice.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app.

Here is an example of the HMS configuration.

```json
"ios" :
{
    "hms":{
    }
},
"android":
{
    "hms":{
        "debug": false
    }
}
```

And you must download `agconnect-services.json` from HMS developer site, and put it in `proj.android/app`.

### HMS for iOS

-   HMS is not supported iOS, we implement empty on iOS.

### Test HMS for android

1. Create App in AppGallery
2. Enable Module you need(enable AccountKit if you need)
3. Configure app signature
4. download app info `agconnect-services.json`

HMS official [Document](https://developer.huawei.com/consumer/hms)

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[../../shared/remote_application_config.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]


