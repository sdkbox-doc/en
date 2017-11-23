### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> InMobiLib.jar

> PluginInMobi.jar

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
* Include the following permissions above the __application tag__:

```xml
<!--Mandatory permissions to receive ads-->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

<!--Recommended permissions to receive brand‐centric ads with interactive functionality for better eCPMs-->
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
<uses-permission android:name="android.permission.VIBRATE"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="com.google.android.gms.permission.ACTIVITY_RECOGNITION"/>
<uses-permission android:name="android.permission.READ_CALENDAR"/>
<uses-permission android:name="android.permission.WRITE_CALENDAR"/>
<uses-permission android:name="android.permission.GET_TASKS"/>
```

* Include the following lines above the __application tag__:

```xml
<!--Required Activity for rendering ads in the embedded browser-->
<activity android:name="com.inmobi.rendering.InMobiAdActivity"
            android:configChanges="keyboardHidden|orientation|keyboard|smallestScreenSize|screenSize"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:hardwareAccelerated="true" />


<!--Required Receiver for enhanced targeting for better ads.-->

<receiver android:name="com.inmobi.commons.core.utilities.uid.ImIdShareBroadCastReceiver"
            android:enabled="true"
            android:exported="true" >
    <intent-filter>
       <action android:name="com.inmobi.share.id" />
    </intent-filter>
</receiver>

<service android:enabled="true" android:name="com.inmobi.signals.activityrecognition.ActivityRecognitionManager" />

<!--Required for Google Play Services-->

<meta-data android:name="com.google.android.gms.version"
            android:value="@integer/google_play_services_version"/>
```

### Edit `Android.mk`
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginInMobi
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
$(call import-module, ./plugininmobi)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./plugininmobi)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
