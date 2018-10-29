[&#8249; Google Play Games Services Doc Home](./)

<h1>Google Play Games Services Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX Google Play Games Services plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import gpg
```

> Warning: Account creation within iOS is no longer supported, please read [this blog post](https://android-developers.googleblog.com/2016/12/games-authentication-adopting-google.html) for details

##After Installation

### Android

#### Update AndroidManifest.xml

Add this meta-data tag to your `AndroidManifest.xml`

```
<meta-data android:name="com.google.android.gms.games.APP_ID"
    android:value="@string/google_app_id" />
```

#### Update string.xml

Add this entry to `proj.android/res/values/string.xml`

```
<string name="google_app_id">777734739048</string>
```

Replace `google_app_id` value with your own App Id.

### iOS

#### Set a rootview controller for GPG:

Update `proj.ios_mac/ios/RootViewController.h`
Add this:

```
#import <GoogleSignIn/GoogleSignIn.h>

// Change RootViewController class definition to:
@interface RootViewController : UIViewController<GIDSignInUIDelegate>
```

#### Set Google Play signin listeners

Update `proj.ios_mac/ios/AppController.mm`

1. Add this method:

```
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options {
    return [[GIDSignIn sharedInstance] handleURL:url
                               sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey]
                                      annotation:options[UIApplicationOpenURLOptionsAnnotationKey]];
}
```

2. In this method:
```
(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
```

add a call to (before return YES):

```
    // _viewController could also be named
    //  viewController, depending of the project type.
    [GIDSignIn sharedInstance].uiDelegate = _viewController;
```

#### Add URL types

Add the following URL types under **your project > Info > URL Types**

+ URL 1:

    + Identifier: `com.google.ReverseClientId`
    + Url schemes: `com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni`
    > (use this as sample, or put your very own application's url scheme)

+ URL 2:

    + Identifier: `com.google.BundleId`
    + URL schemes: `com.sdkbox.gpg`
    > (use this as sample or put your own application's bundle id)

#### Further info

For more information check out the [official documentation](https://developers.google.com/games/services/cpp/gettingStartedIOS)

<<[../../shared/notice.md]

##Usage

### Pre-requisites

Your must create your app on [Google Play Developer console](https://play.google.com/apps/publish) and all the services must be explicitly enabled and configured in the console.

* Please follow [setup guide](https://developers.google.com/games/services/console/enabling) to setup Google Play Games Services for your game.
* After the setup, please follow [config guide](https://developers.google.com/games/services/console/configuring) to enable different Games Services for your game.

> Note: Google Play Games Services will use your release keystore by default, if you want to test your game in debug settings, please link an additional app with [debug keystore](http://stackoverflow.com/questions/17612928/should-i-use-debug-keystore-with-google-play-game-services-during-development)

<<[usage.md]

<<[api-reference.md]

##Manual Integration
If the *SDKBOX Installer* __fails__ to complete successfully, it is possible to integrate SDKBOX manually. If the installer complete successfully, please __do not__ complete anymore of this document. It is not necessary.

These steps are listed last in this document on purpose as they are seldom needed. If you find yourself using these steps, please, after completing, double back and re-read the steps above for other integration items.


## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of
the`GooglePlay` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginGPG.framework

> GoogleAppUtilities.framework

> GoogleAuthUtilities.framework

> GoogleNetworkingUtilities.framework

> GoogleOpenSource.framework

> GooglePlus.bundle

> GooglePlus.framework

> GoogleSignIn.bundle

> GoogleSignIn.framework

> GoogleSymbolUtilities.framework

> GoogleUtilities.framework

> gpg.bundle

> gpg.framework


The above frameworks depend upon other frameworks. You also need to add the
following system frameworks, if you don't already have them:

> AddressBook.framework

> AssetsLibrary.framework

> CoreData.framework

> CoreLocation.framework

> CoreMotion.framework

> CoreTelephony.framework

> CoreText.framework

> Foundation.framework

> MediaPlayer.framework

> QuartzCore.framework

> SafariServices

> Security.framework

> StoreKit

> Security.framework

> SystemConfiguration.framework

> libc++.dylib

> libz.dylib

Add a linker flag, if your setup requires it, to:
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -ObjC

### Code changes

#### Set a rootview controller for GPG:

Update `proj.ios_mac/ios/RootViewController.h`
Add this:

```
#import <GoogleSignIn/GoogleSignIn.h>

// Change RootViewController class definition to:
@interface RootViewController : UIViewController<GIDSignInUIDelegate>
```

#### Set Google Play signin listeners

Update `proj.ios_mac/ios/AppController.mm`

1. Add this method:

```
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options {
    return [[GIDSignIn sharedInstance] handleURL:url
                               sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey]
                                      annotation:options[UIApplicationOpenURLOptionsAnnotationKey]];
}
```

2. In this method:
```
(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
```

add a call to (before return YES):

```
    // _viewController could also be named
    //  viewController, depending of the project type.
    [GIDSignIn sharedInstance].uiDelegate = _viewController;
```

#### Add URL types

Add the following URL types under **your project > Info > URL Types**

+ URL 1:

    + Identifier: `com.google.ReverseClientId`
    + Url schemes: `com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni`
    > (use this as sample, or put your very own application's url scheme)

+ URL 2:

    + Identifier: `com.google.BundleId`
    + URL schemes: `com.sdkbox.gpg`
    > (use this as sample or put your own application's bundle id)

#### Further info

For more information check out the [official documentation](https://developers.google.com/games/services/cpp/gettingStartedIOS)

<<[../../shared/manual_integration_android_and_android_studio.md]

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project's __<project_root>/libs__ folder.

> Plugingpg.jar

> sdkbox.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

    Android command-line:
    ```
    cocos2d/cocos/platform/android/java/libs
    ```

    Android Studio:
    ```
    cocos2d/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using cocos2d-js or lua copy the __jar__ files to:

    Android command-line:
    ```
    frameworks/cocos2d-x/cocos/platform/android/java/libs
    ```

    Android Studio:
    ```
    frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using prebuilt cocos2d-x copy the __jar__ files to:

    Android command-line:
    ```
    <project_root>/libs
    ```

<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`

Add following meta-data tags:
```xml
<meta-data android:name="com.google.android.gms.version"
    android:value="@integer/google_play_services_version" />
<meta-data android:name="com.google.android.gms.games.APP_ID"
    android:value="@string/google_app_id" />
```

Make sure to add an entry to the file `res/values/string.xml` of the form: `<string name="google_app_id">777734739048</string>`
Change that value for your own generated play games App Id.

### Edit `Android.mk`

Edit `<project_root>/jni/Android.mk` to:

Install in a folder named `gpg` inside your `proj.android\jni` directory

Add this to your `android.mk` file

#### Add include path
```
LOCAL_C_INCLUDES += ./gpg/include/
```

#### Add static libraries

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += gpg-1
LOCAL_WHOLE_STATIC_LIBRARIES += PluginGPG
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

Add a call to:
```
$(call import-add-path,$(LOCAL_PATH))
```
before any __import-module__ statements.

Add additional __import-module__ statements at the end:
```
$(call import-module, ./gpg)
$(call import-module, ./sdkbox)
$(call import-module, ./plugingpg)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]


