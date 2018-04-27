[&#8249; Share Doc Home](./)

<h1>Share Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Overview
SDKBOX Share plugin provide an one stop solution for developers to share to all social platforms.

Currently SDKBOX Share supports share via **twitter**, **facebook** and **SMS**

Please make sure you create developer account on the following platforms

* [Facebook](http://developers.facebook.com/)
* [Twitter](http://apps.twitter.com/)

##Integration
Open a terminal and use the following command to install the SDKBOX Share plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import share
```

You will also need to import SDKBOX facebook plugin if you want enable facebook share support
```bash
$ sdkbox import facebook
```
Facebook plugin have some extra integration steps, please click [here](http://docs.sdkbox.com/en/plugins/facebook/v3-cpp/#extra-steps)

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Share configuration
```json
    "android": {
        "Facebook": {
            "debug": false
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "0mxHbmO8QFHSLnfJVVbGTStjaW6IlcRC6xofSWeFecLcj4jsLn",
                        "key": "s5xddoPxy4xIbzAhqrecESSlW"
                    }
                },
                "Facebook": {},     //support facebook share
                "SMS": {},          //support sms share
                "EMail": {}         //support email share
            }
        }
    },
    "ios": {
        "Facebook": {
            "debug": true
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "0mxHbmO8QFHSLnfJVVbGTStjaW6IlcRC6xofSWeFecLcj4jsLn",
                        "key": "s5xddoPxy4xIbzAhqrecESSlW"
                    }
                },
                "Facebook": {},     //support facebook share
                "SMS": {},          //support sms share
                "EMail": {}         //support email share
            }
        }
    }
```

**Twitte configuration**

you need to replace `<key>`, `<secret>` item with your specific [Twitter](http://apps.twitter.com/) account.

**Facebook configuration**

you need to add a `Facebook` entry in the config

###Setup iOS
* `Twitter` support iOS 9.0+
* Apply the code change to `AppController.mm`

```object-c
#import <TwitterKit/TWTRKit.h>

- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
    return [[Twitter sharedInstance] application:app openURL:url options:options];
}
```

* Apply follow change to `Info.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>

    ...

    <key>CFBundleURLTypes</key>
    <array>

        ...

        <dict>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>twitterkit-(your-appkey)</string>
            </array>
        </dict>

        ...

    </array>

    <key>LSApplicationQueriesSchemes</key>
    <array>

        ...

        <string>twitter</string>
        <string>twitterauth</string>

        ...

    </array>

    ...

</dict>
</plist>

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

email share is not support on simulator
