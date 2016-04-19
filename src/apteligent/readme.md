[&#8249; Apteligent Doc Home](./)

<h1>Apteligent Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
First, you must sign up for [Apteligent](https://www.apteligent.com/) and setup your app.

Second, Open a terminal and use the following command to install the SDKBOX Apteligent plugin.
```bash
$ sdkbox import apteligent
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

- id: Apteligent App ID

#### options

---

- monitor_connection [bool]: (iOS only)

    - true [default]
    - false

> Determines whether Service Monitoring should capture network performance information for network calls made through NSURLConnection.

- monitor_session [bool]: (iOS only)

    - true [default]
    - false

> Determines whether Service Monitoring should capture network performance information for network calls made through NSURLSession.

- enable_service_monitoring [bool]:

    - true [default]
    - false

> This flag determines wither Crittercism service monitoring is enabled at all.

- delay_sending_appload [bool]:

    - true
    - false [default]

> Delay to reports an app load event.

- url_filters [array]:

    - ["http://www.gmail.com", "www.other.com"]

> These filters are used to make it so certain network performance information is not reported to Crittercism.

- version [string]: (Android only)

    - "version:2.0.4 build:4981 codeName:Cactus"

> Customizing the Version Reported to Crittercism.

- version_string_include_version_code [bool]: (Android only)

    - true
    - false [default]

> Whether versoin string include version code.

- logcat_reporting_enabled: (Android only) Include Logcat

    - true
    - false [default]

> Including system log data (Logcat) can be helpful for debugging crashes and handled exceptions,
> but it comes at the cost of slightly increasing disk and network usage, which is why this feature
> must be manually enabled. Crittercism collects the last 100 lines of logcat data.

more information:

- [https://docs.crittercism.com/ios/ios.html](https://docs.crittercism.com/ios/ios.html)
- [https://docs.crittercism.com/android/android.html](https://docs.crittercism.com/android/android.html)

Example:
```json
{
    "ios": {
        "Apteligent":{
            "debug":true,
            "id":"956194d922984692a3184816ec3a510300555300",
            "monitor_connection":true,
            "monitor_session":true,
            "enable_service_monitoring":true,
            "delay_sending_appload":false,
            "url_filters":[
                "https://metrics.sdkbox.com",
                "http://www.gmail.com"
            ]
        }
    },
    "android": {
        "Apteligent":{
            "debug":true,
            "id":"3f66168979494ce38374b4d32d637dcc00555300",
            "enable_service_monitoring":true,
            "delay_sending_appload":false,
            "url_filters":[
                "https://metrics.sdkbox.com",
                "http://www.gmail.com"
            ],
            "version":"version:2.0.4 build:4981 codeName:Cactus",
            "version_string_include_version_code":true,
            "logcat_reporting_enabled":true
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
