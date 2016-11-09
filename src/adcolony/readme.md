[&#8249; AdColony Doc Home](./)

<h1>AdColony Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites
Certain SDKBOX plugins do not work together. If you use __AdColony__, then you cannot also use the __Fyber__ and __SOOMLA GROW__ services, in the same project.

Start from AdColony 3.0 it requires you to config your app to support all orientations, please read the details [here](https://github.com/AdColony/AdColony-iOS-SDK-3/wiki/Xcode-Project-Setup#configuring-supported-orientations)

##Integration
Open a terminal and use the following command to install the SDKBOX AdColony plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import adcolony
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the AdColony configuration, you need to replace `<app id>` and `<zone id>` items with your specific [AdColony](https://clients.adcolony.com/login) account information.
```json
"AdColony":{
    "id":"<app id>",
    "debug":true,
    "ads":{
        "video":{
            "zone": "<zone id>",
            "v4vc": false
        },
        "v4vc":{
            "zone": "<zone id>",
            "v4vc": true,
            "pre_popup" : true,
            "post_popup": true
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
