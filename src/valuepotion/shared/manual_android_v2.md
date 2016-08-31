### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> valuepotion.jar

> PluginValuePotion.jar

> sdkbox.jar

<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

There are also a few necessary tags that also need to be added:

```xml
<application>

......

<meta-data android:name="com.google.android.gms.version"
            android:value="@integer/google_play_services_version" />

<!-- Valuepotion Components -->
<!-- for interstital ad interface -->
<activity
        android:name="com.valuepotion.sdk.VPInterstitialActivity"
        android:theme="@android:style/Theme.Translucent" >
</activity>

<!-- for CPI tracking -->
<receiver
        android:name="com.valuepotion.sdk.VPInstallReceiver"
        android:exported="true" >
        <intent-filter>
                <action android:name="com.android.vending.INSTALL_REFERRER" />
        </intent-filter>
</receiver>
<!-- Valuepotion Components End -->

.....

</application>
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginValuePotion
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
$(call import-module, ./pluginvaluepotion)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginvaluepotion)
```

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-9
```
