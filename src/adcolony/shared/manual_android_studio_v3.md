## Manual Integration For Android Studio.

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android-studio/app/libs__ folder.

> adcolony.jar

> PluginAdColony.jar

> sdkbox.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

    ```
    cocos2d/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using cocos2d-js or lua copy the __jar__ files to:

    ```
    frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
    ```

Copy the `pluginadcolony` and `sdkbox` directories from `plugin/android/jni`
to your `proj.android-studio/app/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.VIBRATE" />
```

To enable __hardware acceleration__ in your __application tag__. This tag is
optional on newer sdk versions and doesn't work on version 2.3.3.
```xml
<android:hardwareAccelerated="true" />
```

Copy and paste the following three activity definitions just before the end of the __application tags__, near the bottom.
```xml
<activity android:name="com.jirbo.adcolony.AdColonyOverlay"
      android:configChanges="keyboardHidden|orientation"
      android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyFullscreen"
      android:configChanges="keyboardHidden|orientation"
      android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyBrowser"
      android:configChanges="keyboardHidden|orientation"
      android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
```

 __Note:__ if your application targets below __API 13__, you will likely need to remove `screenSize` from the __configChanges__ property of the above __activity tags__.

### Edit `Android.mk`
Edit `proj.android-studio/app/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginAdColony
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

Add a call to:
```
$(call import-add-path,$(LOCAL_PATH))
```
before any __import-module__ statements.

Add additional __import-module__ statements at the end:
```
$(call import-module, ./sdkbox)
$(call import-module, ./pluginadcolony)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginadcolony)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `proj.android/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
