## Manual Integration For Android Studio.

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android-studio/app/libs__ folder.

> PluginFyber.jar

> sdkbox.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

  ```
  cocos2d/cocos/platform/android/java/libs
  ```

* If you're using cocos2d-js or lua copy the __jar__ files to:

  ```
  frameworks/cocos2d-x/cocos/platform/android/java/libs
  ```

Copy the `pluginfyber` and `sdkbox` directories from `plugin/android/jni` to your `proj.android-studio/app/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

Copy the `fyber_lib` directories from `plugin/android/libs` to your `proj.android-studio/app/libs/` directory.


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

There are also a few necessary meta-data tags that also need to be added:
```xml
<activity android:name="com.sponsorpay.publisher.ofw.SPOfferWallActivity" android:configChanges="orientation"/>
<activity
    android:configChanges="screenSize|orientation"
    android:name="com.sponsorpay.publisher.interstitial.SPInterstitialActivity"
    android:hardwareAccelerated="true"/>
<activity
    android:configChanges="screenSize|orientation"
    android:name="com.sponsorpay.publisher.mbe.SPBrandEngageActivity"
    android:hardwareAccelerated="true"/>
```

### Edit `Android.mk`
Edit `proj.android-studio/app/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginFyber
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
$(call import-module, ./pluginfyber)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginfyber)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `proj.android-studio/app/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-14
```
