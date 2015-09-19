<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/googleanalytics/v3-cpp
-->

#Google Analytics

##Integration
Open a terminal and use the following command to install the SDKBOX Google Analytics plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import googleanalytics
```

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Google Analytics configuration, you need to replace `<TRACKING_CODE>`  with your specific [__Google Analytics Tracking Code__](https://support.google.com/analytics/answer/1008080?hl=en) account information.
```json
"GoogleAnalytics" : {
    "trackingCode" : "<TRACKING_CODE>"
}
```

## Tracker
A __tracker__ is used to aggregate the tracked events. There are some considerations that the developer must review:

* You must create a mobile tracker or reuse a previously created one.

* If the tracker is new, it will take up to 24 hours to show tracking data.

* Once you see some historical activity on the tracker, you can see realtime data as well, not before.

* You can create as many trackers as you wish, but the plugin configuration only allows to define one (the base use case).

* If no tracker is set in the configuration, there will be no tracking session. This means that at a later time, a new (or more) tracker can be created. In this case, a explicit call to `startSession()` should be performed.

* Whether the tracker is set in the plugin configuration or manually created, all tracking events will be sent to the server automatically. The implementation buffers tracking events and sends them to the server it batches.

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[manual_integration_google_play_step.md]

<<[extra-step.md]

<<[proguard.md]


