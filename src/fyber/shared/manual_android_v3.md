### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> PluginFyber.jar

> sdkbox.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

	Android command-line:
	```
	cocos2d/cocos/platform/android/java/libs
	```

	Android Studio:
	```
	cocos2d/cocos/platform/android/libcocos2dx/libs
	```

* If you're using cocos2d-js or lua copy the __jar__ files to:

	Android command-line:
	```
	frameworks/cocos2d-x/cocos/platform/android/java/libs
	```

	Android Studio:
	```
	frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
	```

* If you're using prebuilt cocos2d-x copy the __jar__ files to:

	Android command-line:
	```
	<project_root>/libs
	```

Copy the `pluginfyber` and `sdkbox` directories from `plugin/android/jni` to your `<project_root>/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

Copy the `fyber_lib` directories from `plugin/android/libs` to your `<project_root>/libs/` directory.


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
<activity
    android:name="com.fyber.ads.ofw.OfferWallActivity"
    android:configChanges="screenSize|orientation" />
<activity
    android:name="com.fyber.ads.videos.RewardedVideoActivity"
    android:configChanges="screenSize|orientation"
    android:hardwareAccelerated="true"
  android:theme="@android:style/Theme.Translucent" />
<activity
    android:name="com.fyber.ads.interstitials.InterstitialActivity"
    android:configChanges="screenSize|orientation"
    android:theme="@android:style/Theme.Translucent" />
<activity
    android:configChanges="screenSize|orientation"
    android:name="com.fyber.cache.CacheVideoDownloadService"
    android:hardwareAccelerated="true"/>
<service android:name="com.fyber.cache.CacheVideoDownloadService" android:exported="false" />
```

### Edit `Android.mk`
Edit `<project_root>/jni/Android.mk` to:

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
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-14
```
