[&#8249; Google Play Games Services Doc Home](./)

<h1>Google Play Games Services Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX Google Play Games Services plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import googleplay 
```

##After Installation

### Android

#### Update AndroidManifest.xml

Add this meta-data tag to your `AndroidManifest.xml`

```
<meta-data android:name="com.google.android.gms.games.APP_ID" 
    android:value="@string/google_app_id" />
```

#### Update `string.xml`

Add this entry to `proj.android/res/values/string.xml`

```
<string name="google_app_id">777734739048</string>
```

Change that `google_app_id` value with your own App Id.

### iOS

#### Set a rootview controller for GPG:

Update `proj.ios_mac/ios/RootViewController.h`
Add this:

```
import <GoogleSignIn/GoogleSignIn.h>

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

#### URL types

+ URL 1:

    Identifier: `com.google.ReverseClientId`
    Url schemes: `com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni`
    (use this as sample, or put your very own application’s url scheme) 

+ URL 2:

    Identifier: `com.google.BundleId`
    URL schemes: `com.sdkbox.gpg`
    (use this as sample or put your own application’s bundle id)
    
#### Further info

For further info, have a look at: https://developers.google.com/games/services/cpp/gettingStartedIOS

<<[../../shared/notice.md]

##Usage

### Pre-requisites

Your must create your app on [Google Play Developer console](https://play.google.com/apps/publish) and have game services enabled.

Leaderboards, Achievements, Quests, Events, Realtime Multiplayer and Turn Based multiplayer support must be explicitly enabled and configured in the console.

Please follow [this guide](https://developers.google.com/games/services/console/enabling) to setup Google Play Games Services for your game. After the setup, you can follow [this guide](https://developers.google.com/games/services/console/configuring) to enable different Games Services for your game.

> Note: Your Games Services will use your release keystore by default, so if you want to test your game in debug settings, please link an additional app with [debug keystore](http://stackoverflow.com/questions/17612928/should-i-use-debug-keystore-with-google-play-game-services-during-development)

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]


