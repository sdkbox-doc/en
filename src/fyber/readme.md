[&#8249; Fyber Doc Home](./)

<h1>Fyber Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites
* __For Android, Fyber requires a minimum version of 4.0.3. This version is newer than what the other SDKBOX plugins require.__
* Certain SDKBOX plugins do not work together. If you use __Fyber__, then you cannot also use the __SOOMLA GROW__ services, in the same project.

##Integration
Open a terminal and use the following command to install the SDKBOX Fyber plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import fyber
```

<<[../../shared/notice.md]

##Extra steps
The following step assuming you already registered as a Fyber Developer
And created a new __APP__ on Fyber

###Setup iOS
* Configure your __APP__ following [iOS Quick Start Guide](http://developer.fyber.com/content/ios/)

###Setup Android
* Make sure `java -version` >= 1.7
* Configure your __APP__ on Fyber follow [Android Quick Start Guide](http://developer.fyber.com/content/android/basics/)

###Setup Mediation
If you want to setup fyber to use certain mediation network, please follow fyber's official integration guide

* [iOS Supported networks](http://developer.fyber.com/content/current/ios/rewarded-video/adding-networks/)
* [Android Supported networks](http://developer.fyber.com/content/current/android/rewarded-video/adding-networks/)

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the Fyber configuration you can enable/disable debug mode for Fyber here
```json
"Fyber":
{
    "debug":true,
    "appid":"12345",
    "token":"34a9643edf4d3052d2bc1928b2e34d00"
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

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]
