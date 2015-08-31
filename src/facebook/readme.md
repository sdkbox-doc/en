<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/facebook/v3-cpp
-->

#Facebook

##Integration
Open a terminal and use the following command to install the SDKBOX Facebook plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import facebook
```

## Changelog

version-x.y.z:
1. `register_PluginFacebookJS_helper` -> `register_all_PluginFacebookJS_helper`
2. `register_PluginFacebookLua_helper` -> `register_all_PluginFacebookLua_helper`
3. Update Facebook iOS SDK to 4.5.1
4. Update Facebook Android SDK to 4.5.1

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

## Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the Facebook configuration you can enable/disable debug mode for Facebook here
```json
"Facebook":
{
    "debug":true
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
