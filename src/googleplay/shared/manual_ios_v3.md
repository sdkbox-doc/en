## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of
the`GooglePlay` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginSdkboxGooglePlay.framework

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

#### Other frameworks

+ Get `gpg.framework` and `gpg.bundle` from Play Games C++ SDK: https://developers.google.com/games/services/downloads/gpg-cpp-sdk.v2.1.zip
+ Get `GoogleOpenSource.framework` from Google+ iOS SDK: https://developers.google.com/+/mobile/ios/getting-started
+ get `GoogleSignIn.framework` and `GoogleSignIn.bundle` from Sign iOS SDK: https://developers.google.com/identity/sign-in/ios/sdk

### Code changes

#### Set a rootview controller for GPG UI:

Update proj.ios_mac/ios/RootViewController.h
Add this:

```
import <GoogleSignIn/GoogleSignIn.h>

// Change RootViewController class definition to:
@interface RootViewController : UIViewController<GIDSignInUIDelegate> 
```

#### Set Google Play signin listeners

Update proj.ios_mac/ios/AppController.mm

1. Add this method:

```
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary *)options {
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

    Identifier: com.google.ReverseClientId
    Url schemes: com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni
    (use this as sample, or put your very own application’s url scheme) 

+ URL 2:

    Identifier: com.google.BundleId
    URL schemes: com.sdkbox.gpg
    (use this as sample or put your own application’s bundle id)
    
### Further info

For further info, have a look at: https://developers.google.com/games/services/cpp/gettingStartedIOS