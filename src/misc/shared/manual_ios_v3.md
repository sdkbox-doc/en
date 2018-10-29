## Manual Integration For iOS

Drag and drop the following frameworks from the __plugins/ios__ folder of the `Misc` bundle into your Xcode project, check `Copy items if needed` when
adding frameworks:

> sdkbox.framework

> PluginMisc.framework

You also need to add the following system frameworks, if you don't already have them:

> SystemConfiguration.framework

file change list:

- proj.ios_mac/ios/AppController.mm

```diff

  #import "RootViewController.h"

+ #include "PluginMisc/PluginMisc.h"

  @implementation AppController


  - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      ...
      //run the cocos2d-x game scene
      app->run();

+     if (launchOptions[UIApplicationLaunchOptionsLocalNotificationKey]) {
+         [self handleLocalNotification:launchOptions[UIApplicationLaunchOptionsLocalNotificationKey]];
+     }

      return YES;
  }
  
+ - (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification {
+     [self handleLocalNotification:notification.userInfo];
+ }
+ 
+ - (void)handleLocalNotification:(NSDictionary *)payloadDic {
+     NSError *error = nil;
+     NSData *jsonData = [NSJSONSerialization dataWithJSONObject:payloadDic
+                                                        options:0
+                                                          error:&error];
+     if (nil != jsonData) {
+         NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
+         sdkbox::PluginMisc::handleLocalNotify([jsonString UTF8String]);
+     } else {
+         NSLog(@"Error:%@", error);
+     }
+ }
  
  - (void)applicationWillResignActive:(UIApplication *)application {

```

