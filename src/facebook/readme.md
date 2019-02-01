[&#8249; Facebook Doc Home](./)

<h1>Facebook Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites
* __For Android__, Facebook requires a minimum version of __API 15: Android 4.0.3__. This version is newer than what the other SDKBOX plugins require.

##SDK Version
<<[../version]

##Integration
Open a terminal and use the following command to install the SDKBOX Facebook plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import facebook
```

<<[../../shared/notice.md]
Follow [this link](https://developers.facebook.com/docs/ios/ios9)

##FAQ
1. If you want to switch Facebook Login behavior (Facebook Native App / Web Dialog), [clear Safari Cookie](https://support.apple.com/en-us/HT201265)
2. If you want to switch Facebook Login Account, [clear Safari Cookie](https://support.apple.com/en-us/HT201265)

##Extra steps
The following step assuming you already registered as a Facebook Developer
And created a new __APP__ on Facebook, If not please follow up the __Setup Facebook App__ section below.

###Setup iOS
* Configure your __APP__ following [iOS Quick Start Guide](https://developers.facebook.com/quickstarts/?platform=ios)
* Special for iOS9 [https://developers.facebook.com/docs/ios/ios9](https://developers.facebook.com/docs/ios/ios9)
* Apply the code change to `AppController.mm` instead of `AppDelegate.cpp`

```
#import <FBSDKCoreKit/FBSDKCoreKit.h>

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  //
  // **************************
  // !! IMPORTANT !!
  // **************************
  //
  // call [[FBSDKApplicationDelegate sharedInstance] application:didFinishLaunchingWithOptions
  // before app->run()

  [[FBSDKApplicationDelegate sharedInstance] application:application
    didFinishLaunchingWithOptions:launchOptions];

  app->run();

  return YES;
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {

  BOOL handled = [[FBSDKApplicationDelegate sharedInstance] application:application
    openURL:url
    sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey]
    annotation:options[UIApplicationOpenURLOptionsAnnotationKey]
  ];
  // Add any custom logic here.
  return handled;
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication
         annotation:(id)annotation {

  BOOL handled = [[FBSDKApplicationDelegate sharedInstance] application:application
    openURL:url
    sourceApplication:sourceApplication
    annotation:annotation
  ];
  // Add any custom logic here.
  return handled;
}

```

login doesn't work on simulator on iOS 10, Xcode8

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
[Setup Facebook App for SDKBOX](http://blog.cocos2d-x.org/2016/07/setting-up-facebook-app-for-sdkbox-services/)
> With the release of the Facebook SDK version 4.28.0, App Links Hosting is deprecated. It will be supported until February 5, 2018.
> https://developers.facebook.com/docs/applinks/hosting-api/

### Facebook App Links Host

1. Get `APP_ACCESS_TOKEN` (App Token) in https://developers.facebook.com/tools/access_token/
2. Create links

```
curl https://graph.facebook.com/app/app_link_hosts \
-F access_token="APP_ACCESS_TOKEN" \
-F name="iOS App Link Object Example" \
-F ios=' [
    {
      "url" : "sharesample://story/1234",
      "app_store_id" : 12345,
      "app_name" : "ShareSample",
    },
  ]' \
-F web=' {
    "should_fallback" : false,
  }'
```

3. Query link

```
curl -G https://graph.facebook.com/{YOUR_LINK_ID} \
-d access_token="APP_ACCESS_TOKEN" \
-d fields=canonical_url \
-d pretty=true

# or
curl -G https://graph.facebook.com \
-d access_token="APP_ACCESS_TOKEN" \
-d fields=app_links \
-d ids=https://fb.me/{YOUR_LINK_ID} \
-d pretty=true
```

4. Update link

```
curl https://graph.facebook.com/{YOUR_LINK_ID} \
-F access_token="APP_ACCESS_TOKEN" \
-F name="FB App Link Object Example" \
-F ios=' [
    {
      "url" : "sharesample://story/1234",
      "app_store_id" : 12345,
      "app_name" : "ShareSample",
    },
  ]' \
-F web=' {
    "should_fallback" : false,
}'
```


### ~~Invite Friends~~
- http://discuss.cocos2d-x.org/t/solved-invite-friends-with-using-cocos2dx-layer/34450

https://developers.facebook.com/docs/ios/change-log-4x/

> The App Invites feature has been deprecated. (4.28.0 - November 7, 2017)


You need a canvas version of your game, but you can submit an empty/placeholder canvas version.

'Dashboard' -> 'Settings' -> 'Basic' -> 'Add Platform'

> Navigate to your app's [Facebook settings](https://developers.facebook.com/apps/). Go to the ‘Facebook Web Games' pane in the Basic tab of your app's ‘Settings' page and fill in the ‘Facebook Web Games URL (https)' field with the URL where you are serving your game. Now save your changes.

![preview](https://scontent-lax3-1.xx.fbcdn.net/v/t39.2178-6/16781471_393759444334692_3641607580918218752_n.PNG?_nc_cat=0&oh=2ac23410835c91da267971b1460f2d64&oe=5B74F3CE)

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
> another by incrementing the final digit as `android.library.reference.2`, etc.

<<[extra-step.md]

<<[proguard.md]
