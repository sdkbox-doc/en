### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> PluginFyber.jar

> sdkbox.jar

Copy the `pluginfyber` and `sdkbox` directories from `plugin/android/jni` to your `proj.android/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

To enable __hardware acceleration__ in your __application tag__. This tag is
optional on newer sdk versions and doesn't work on version 2.3.3.
```xml
<android:hardwareAccelerated="true" />
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
<activity android:name="com.fyber.ads.videos.RewardedVideoActivity"
  android:configChanges="screenSize|orientation" android:hardwareAccelerated="true" android:theme="@android:style/Theme.Translucent" />
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
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

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-14
```
