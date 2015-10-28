<!--
Include Base: /Users/jtsm/Chukong-Inc/en/src/facebook/v3-cpp
-->

#Facebook

##Prerequisites
* __For Android__, Facebook requires a minimum version of __API 15: Android 4.0.3__. This version is newer than what the other SDKBOX plugins require.

##Integration
Open a terminal and use the following command to install the SDKBOX Facebook plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import facebook
```

<<[../../shared/notice.md]
Follow [this link](https://developers.facebook.com/docs/ios/ios9)

##Extra steps
The following step assuming you already registered as a Facebook Developer
And created a new __APP__ on Facebook

###Setup iOS
* Configure your __APP__ following [iOS Quick Start Guide](https://developers.facebook.com/quickstarts/?platform=ios)
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

Here is an example of the Facebook configuration you can enable/disable debug mode for Facebook here
```json
"Facebook":
{
    "debug":true
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

##Manual Integration For Android and Android Studio
Both __Android__ development using a command-line and using __Android Studio__ are supported. `proj.android` will be used as our `<project_root>` for __command-line__ development, while `proj.android-studio` will be used as our `<project_root>` for __Android Studio__.
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
