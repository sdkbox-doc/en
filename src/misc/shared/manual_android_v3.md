## Manual Integration For Android Studio

- proj.android/app/libs <- $PLUGIN_MISC_BUNDLE/plugin/android/libs
- proj.android/app/jni  <- $PLUGIN_MISC_BUNDLE/plugin/android/jni
- proj.android/app/src/org/cocos2dx/cpp/AppActivity.java
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
- proj.android/app/build.gradle
```diff
  dependencies {
      implementation fileTree(dir: 'libs', include: ['*.jar'])
      implementation project(':libcocos2dx')
+     implementation 'com.android.support:support-v4:26.1.0'
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

