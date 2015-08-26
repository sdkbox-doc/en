## Manual Integration For Android.

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> KochavaSDK.jar

> PluginKochava.jar

> sdkbox.jar

Copy the `pluginkochava` and `sdkbox` directories from `plugin/android/jni`
to your `proj.android/jni/` directory. If the `sdkbox` folder exists, it's ok
to overwrite it.

### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name ="android.permission.INTERNET"/>
<uses-permission android:name ="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name ="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name ="android.permission.READ_PHONE_STATE"/>
```

Additionally, you will need to add the Kochava broadcast receiver and the
following meta-data tag between the __application tags__, this is needed for the Google Play referral data capture:
```xml
<receiver android:name ="com.kochava.android.tracker.ReferralCapture"
  android:exported ="true" >
  <intent-filter>
  <action android:name ="com.android.vending.INSTALL_REFERRER" />
  </intent-filter>
  </receiver>
  <meta-data
    android:name ="com.google.android.gms.version"
    android:value ="@integer/google_play_services_version"/>
```

To enable __hardware acceleration__ in your __application tag__. This tag is
optional on newer sdk versions and doesn't work on version 2.3.3.
```xml
<android:hardwareAccelerated="true" />
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginKochava
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
$(call import-module, ./pluginkochava)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginkochava)
```

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-9
```
