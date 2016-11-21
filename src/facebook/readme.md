[&#8249; Facebook Doc Home](./)

<h1>Facebook Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites
* __For Android__, Facebook requires a minimum version of __API 15: Android 4.0.3__. This version is newer than what the other SDKBOX plugins require.

##Integration
Open a terminal and use the following command to install the SDKBOX Facebook plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import facebook
```

<<[../../shared/notice.md]
Follow [this link](https://developers.facebook.com/docs/ios/ios9)

##Extra steps
The following step assuming you already registered as a Facebook Developer
And created a new __APP__ on Facebook, If not please follow up the __Setup Facebook App__ section below.

###Setup iOS
* Configure your __APP__ following [iOS Quick Start Guide](https://developers.facebook.com/quickstarts/?platform=ios)
* Special for iOS9 [https://developers.facebook.com/docs/ios/ios9](https://developers.facebook.com/docs/ios/ios9)
* Apply the code change to `AppController.mm` instead of `AppDelegate.cpp`

```
#import <FBSDKCoreKit/FBSDKCoreKit.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // ...

  //
  // **************************
  // !! IMPORTANT !!
  // **************************
  //
  // call [[FBSDKApplicationDelegate sharedInstance] application:didFinishLaunchingWithOptions
  // before app->run()

  BOOL ret = [[FBSDKApplicationDelegate sharedInstance] application:application
                                      didFinishLaunchingWithOptions:launchOptions];
  app->run();
  return ret;
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication
         annotation:(id)annotation {
  return [[FBSDKApplicationDelegate sharedInstance] application:application
                                                         openURL:url
                                               sourceApplication:sourceApplication
                                                      annotation:annotation];
}

- (void)applicationDidBecomeActive:(UIApplication *)application {
  [FBSDKAppEvents activateApp];
}

```

login doesnt work on simulator on iOS 10, Xcode8

~~~
Go to the Project Target and then Capabilities and switch Keychain Sharing ON.
~~~
http://stackoverflow.com/a/39788102/5443510


###Setup Android
* Make sure `java -version` >= 1.7
* Configure your __APP__ on Facebook follow [Android Quick Start Guide](https://developers.facebook.com/quickstarts/?platform=android)
* Open `res/values/strings.xml` and replace `facebook_app_id` with your `Facebook App ID`
* Open `AndroidManifest.xml` and replace `_replace_with_your_app_id_` with your `Facebook App ID`
* Open `project.properties` and change target to `target=android-15`

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

#### options

- app_id [string]:

> The Facebook App ID to be used by the SDK.

- url_scheme_suffix [string]: (iOS only)

> The url scheme suffix to be used by the SDK.

Here is an example of the Facebook configuration you can enable/disable debug mode for Facebook here
```json
"Facebook":
{
    "debug":true,
    "app_id":"",
    "url_scheme_suffix":""
}
```
### Setup Facebook App
In order to setup your Facebook app correctly to avail all services provided by SDKBOX, please go through the link mentioned below -
[Setup Facebook App for SDKBOX](http://blog.cocos2d-x.org/2016/02/setting-up-facebook-app-for-sdkbox-services/)


<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

###Modify `project.properties`
Add following line to your `project.properties`

```
android.library.reference.1=./libs/facebook_lib
```

> Note: if you already have an `android.library.reference.1` you can add
another by incrementing the final digit as `android.library.reference.2`, etc.

<<[extra-step.md]

<<[proguard.md]
