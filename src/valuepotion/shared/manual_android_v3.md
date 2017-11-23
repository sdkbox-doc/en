### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> valuepotion.jar

> PluginValuePotion.jar

> sdkbox.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

	Android command-line:
	```
	cocos2d/cocos/platform/android/java/libs
	```

    Android Studio:
    <pre>
    cocos2d/cocos/platform/android/java/libs
    cocos2d/cocos/platform/android/libcocos2dx/libs
    </pre>

* If you're using cocos2d-js or lua copy the __jar__ files to:

	Android command-line:
	```
	frameworks/cocos2d-x/cocos/platform/android/java/libs
	```

    Android Studio:
    <pre>
    frameworks/cocos2d-x/cocos/platform/android/java/libs
    frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
    </pre>

* If you're using prebuilt cocos2d-x copy the __jar__ files to:

	Android command-line:
	```
	proj.android/libs
	```

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
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
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

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
