[&#171; SDKBOX Home](http://sdkbox.com)

<h1>FaceBook Share on Cocos</h1>

## How to integrate SDKBox Plugin to Cocos Creator project
---

### Environment

* `SDKBox Installer` [Install](http://docs.sdkbox.com/en/installer/)
* `Cocos2d-x` [Install](http://www.cocos.com/download)


### Create cocos2d-x project

* create cocos2d-x project by run `cocos new -l cpp -p com.sdkbox.sample.facebook.cpp facebook`

### Import facebook

* entry cocos2d-x project directory by run `cd facebook`
* import sdkbox facebook plugin by run `sdkbox import facebook`

### Facebook setting

* make sure you have been a [facebook developer](https://developers.facebook.com/)
* make sure you have create a new app on [facebook developer](https://developers.facebook.com/)
* configure your app

### IOS project setting

#### Modify Info.plist

modify info.plist, your change maybe like follow:

```xml
<plist>
<dict>

    ...

    <key>FacebookAppID</key>
    <string>280194012150923</string>
    <key>FacebookDisplayName</key>
    <string>hellworld - cpp</string>
    <key>CFBundleURLTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>fb280194012150923</string>
            </array>
        </dict>
    </array>
    <key>LSApplicationQueriesSchemes</key>
    <array>
        <string>fbapi</string>
        <string>fb-messenger-api</string>
        <string>fbauth2</string>
        <string>fbshareextension</string>
    </array>

    ...

</dict>
</plist>
```

`FacebookAppID`, `FacebookDisplayName`, `CFBundleURLSchemes` should use your fb app's info

#### Enable Keychain Shareing

`Project` -> `Capablities` -> `Keychain Sharing` -> `ON`

#### Modify AppController.mm

modify AppController.mm, your change maybe like follow:

```object-c
#import <FBSDKCoreKit/FBSDKCoreKit.h>

...

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    ...

    BOOL ret = [[FBSDKApplicationDelegate sharedInstance] application:application
                                        didFinishLaunchingWithOptions:launchOptions];

    //app->run() must be invoked after fb
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

### Android project setting

* make sure use java 1.7+ to compile this project
* open `res/values/strings.xml` and replace facebook_app_id with your Facebook App ID
* open `AndroidManifest.xml` and replace `_replace_with_your_app_id_` with your Facebook App ID
* open project.properties and make sure target is android-15 or newer


### Init Facebook Plugin

you can add follow code when app init
```c++
sdkbox::PluginFacebook::setListener(this);
sdkbox::PluginFacebook::init();
```

### Share Link

```c++
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = ""; //"Best Game Engine";
info.image = ""; //"http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::share(info);
```

### Share photo
```c++
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_PHOTO;
info.title = "capture screen";
info.image = _captureImg;
sdkbox::PluginFacebook::share(info);
```

### dialog link

the follow code can the app url on apple/google store

```c++
//http://itunes.apple.com/[country]/app/[App –Name]/id[App-ID]?mt=8
std::string appUrl;
#if CC_TARGET_PLATFORM == CC_PLATFORM_IOS
    //apple store
    //http://itunes.apple.com/[country]/app/[App –Name]/id[App-ID]?mt=8
    appUrl = "http://itunes.apple.com/";
    appUrl += "cn"; //country
    appUrl += "/app/";
    appUrl += "tan-chi-she-da-zuo-zhan-deng"; //app name
    appUrl += "/id";
    appUrl += "1120536875"; //app id
    appUrl += "?mt=8";
#else
    //google play
    //https://play.google.com/store/apps/details?id=<package_name>
    appUrl = "https://play.google.com/store/apps/details?id=";
    appUrl += "com.impossibleapps.towercrush"; //app package name
#endif

sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_LINK;
info.link  = appUrl;
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";

bool canPresent = sdkbox::PluginFacebook::canPresentWithFBApp(info);
CCLOG("##FB can present with facebook app: %s", canPresent ? "yes" : "no");
if (!canPresent)
{
    CCLOG("\n\n##FB ****************************");
    CCLOG("##FB will show web dialog for u, openning web browser...");
    CCLOG("##FB ****************************\n\n");
}

sdkbox::PluginFacebook::dialog(info);
```

### dialog photo

dialog photo dependency on `FB App`, so `FB App` must be installed in device

dialog photocan share photo, and user can add text by them self.

```c++
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_PHOTO;
info.title = "capture screen";
info.image = _captureImg;

bool canPresent = sdkbox::PluginFacebook::canPresentWithFBApp(info);
CCLOG("##FB can present: %s", canPresent ? "yes" : "no");
if (canPresent) {
    sdkbox::PluginFacebook::dialog(info);
} else {
    CCLOG("\n\n##FB ****************************");
    CCLOG("##FB dialog photo must present with facebook app, thanks!");
    CCLOG("##FB ****************************\n\n");
}
```

## TroubleShooting

if you got follow error on android, please add the key hash to your fb app android setting
```
Invalid key hash. The key hash XXXXXXXX does not match any stored key hashes. Configure your app key hashes at http://developers.facebook.com/apps/XXXXX
```
