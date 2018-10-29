[&#8249; Misc Doc Home](./)

<h1>Misc Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration

Open a terminal and use the following command to install the SDKBOX Misc plugin.
```bash
$ sdkbox import misc
```

### Extern iOS Modification

File change list:

- `proj.ios_mac/ios/AppController.mm`
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

### Extern Android Modification

File change list:

- proj.android/app/src/org/cocos2dx/cpp/AppActivity.java

    this should be your app activity java file
```diff
  package org.cocos2dx.cpp;

+ import android.content.Intent;
  import android.os.Bundle;
  import org.cocos2dx.lib.Cocos2dxActivity;

- public class AppActivity extends Cocos2dxActivity {
+ public class AppActivity extends com.sdkbox.plugin.SDKBoxActivity {

      @Override
      protected void onCreate(Bundle savedInstanceState) {
              return;
          }
          // DO OTHER INITIALIZATION BELOW

+         com.sdkbox.plugin.PluginMisc.onHandleNotification(getIntent());
          
      }

+     @Override
+     protected void onNewIntent(Intent intent) {
+         super.onNewIntent(intent);
+         com.sdkbox.plugin.PluginMisc.onHandleNotification(intent);
+     }

  }
```

-proj.android/app/AndroidManifest.xml

    add `singleTask` to your activity
```diff
              android:screenOrientation="landscape"
              android:configChanges="orientation|keyboardHidden|screenSize"
              android:label="@string/app_name"
              android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
+             android:launchMode="singleTask" >
              <intent-filter>
                  <action android:name="android.intent.action.MAIN" />

```

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`

#### Example:
```json

{
    "ios": {
        "Misc":{
        }
    },
    "android": {
        "Misc":{
        }
    }
}

```

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[proguard.md]
