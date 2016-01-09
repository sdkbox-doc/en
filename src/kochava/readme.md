[&#8249; Kochava Doc Home](./)

<h1>Kochava Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX Kochava plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import kochava
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Kochava configuration, you need to replace
`<KOCHAVA_APP_ID>` with your specific [Kochava](https://kochava.com/) account information.
Here is an example adding `Kochava`:
```json
"kochava" :
{
    "kochavaAppId" : "<KOCHAVA_APP_ID>",
    "enableLogging" : 1,
    "retrieveAttribution" : 1
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