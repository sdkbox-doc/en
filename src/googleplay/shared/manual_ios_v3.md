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

#### Add URL types

Add the following URL types under **your project > Info > URL Types**

+ URL 1:

    + Identifier: `com.google.ReverseClientId`
    + Url schemes: `com.googleusercontent.apps.777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni`
    > (use this as sample, or put your very own application’s url scheme) 

+ URL 2:

    + Identifier: `com.google.BundleId`
    + URL schemes: `com.sdkbox.gpg`
    > (use this as sample or put your own application’s bundle id)
    
#### Further info

For more information check out the [official documentation](https://developers.google.com/games/services/cpp/gettingStartedIOS)