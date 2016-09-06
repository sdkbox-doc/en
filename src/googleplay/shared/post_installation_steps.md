
### Android

#### AndroidManifest.xml

Add this meta to the manifest file:

```
<meta-data android:name="com.google.android.gms.games.APP_ID" 
    android:value="@string/google_app_id" />
```

Make sure to add an entry to the file `res/values/string.xml` of the form: `<string name="google_app_id">777734739048</string>`
Change that value for your own generated play games App Id.

### iOS

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