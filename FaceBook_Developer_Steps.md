Steps For Facebook Plugin
----

* sign up to be a [Facebook Developer](http://developers.facebook.com)

* create a new __APP__

* create a test version of this __App__

* under __Roles__ create a __Test User__. Ensure that you set a password for this test user and assign the permissions you need.

* integrate sdkbox `sdkbox import facebook`

* in the info.plist file you need to specify a few additional keys
```xml
<key>CFBundleURLTypes</key>
<array>
<dict>
    <key>CFBundleURLName</key>
    <string></string>
    <key>CFBundleURLSchemes</key>
    <array>
        <string>fb655158077954837</string>
    </array>
</dict>
</array>
<key>FacebookAppID</key>
<string>655158077954837</string>
<key>FacebookDisplayName</key>
<string>MyTestApp</string>
```

* ios: ensure that you have added the following to `AppController.mm`:
```objc
(void)applicationDidBecomeActive:(UIApplication *)application {
 [FBSDKAppEvents activateApp];
}
```
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 return [[FBSDKApplicationDelegate sharedInstance] application:application
        didFinishLaunchingWithOptions:launchOptions];
}
```
```objc
- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
            sourceApplication:(NSString *)sourceApplication
            annotation:(id)annotation
{
    return [[FBSDKApplicationDelegate sharedInstance] application:application openURL:url sourceApplication:sourceApplication
        annotation:annotation];
}
```
