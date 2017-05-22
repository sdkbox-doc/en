[&#8249; Google Analytics Doc Home](./)

<h1>Google Analytics Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX Google Analytics plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import googleanalytics
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Google Analytics configuration, you need to replace `<TRACKING_CODE>`  with your specific [__Google Analytics Tracking Code__](https://support.google.com/analytics/answer/1008080?hl=en) account information.
```json
"GoogleAnalytics" : {
    "trackingCode" : "<TRACKING_CODE>",
    "anonymizeIp": true
}
```

## Notice

* If your account is new, it might take up to 24 hours to show tracking data.

* Once you see some historical activity on the tracker, you can see realtime data as well.

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
