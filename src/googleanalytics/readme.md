<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/googleanalytics/v3-cpp
-->

#Google Analytics

##Integration
Open a terminal and use the following command to install the SDKBOX Google Analytics plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import googleanalytics
```

##Extra steps for Android
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Google Analytics configuration, you need to replace `<TRACKING_CODE>`  with your specific [__Google Analytics Tracking Code__](https://support.google.com/analytics/answer/1008080?hl=en) account information.
```json
"GoogleAnalytics" : {
    "trackingCode" : "<TRACKING_CODE>"
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]
