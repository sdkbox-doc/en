### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> PluginGoogleAnalytics.jar

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

<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
  <uses-permission android:name="android.permission.INTERNET" />
  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.WAKE_LOCK" />
```

There are also a few necessary meta-data tags that also need to be added:
```xml
<meta-data android:name="com.google.android.gms.version"
    android:value="@integer/google_play_services_version" />
<meta-data
    android:name="com.google.android.gms.analytics.globalConfigResource"
    android:resource="@xml/global_tracker" />
```

Next, register the __AnalyticsReceiver__:
```xml
<receiver android:name="com.google.android.gms.analytics.AnalyticsReceiver"
    android:enabled="true">
    <intent-filter>
        <action android:name="com.google.android.gms.analytics.ANALYTICS_DISPATCH" />
    </intent-filter>
</receiver>
<service android:name="com.google.android.gms.analytics.AnalyticsService"
    android:enabled="true"
    android:exported="false"/>
```

If you want to use optional __Receivers__, specify them next:
```xml
<!-- Optionally, register CampaignTrackingReceiver and CampaignTrackingService to enable installation campaign reporting -->
<receiver android:name="com.google.android.gms.analytics.CampaignTrackingReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="com.android.vending.INSTALL_REFERRER" />
    </intent-filter>
</receiver>
<service android:name="com.google.android.gms.analytics.CampaignTrackingService" />
```

### Edit the meta-data files
In the step above a file named `global_tracker.xml` was specified. This file needs to be created and populated with a few required settings. So where does it go? Take a look again at the code tag from above:
```
<meta-data
    android:name="com.google.android.gms.analytics.globalConfigResource"
    android:resource="@xml/global_tracker" />
```
Notice the `android:resource=` attribute. This gives you the path of where to create this file, in this case it would be `<project_root>/res/xml`.

This file needs to contain required settings. The contents of this file could be something like this:
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <integer name="ga_dispatchPeriod">300</integer>
    <string name="ga_logLevel">verbose</string>
</resources>
```

### Edit `Android.mk`
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginGoogleAnalytics
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
$(call import-module, ./plugingoogleanalytics)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./plugingoogleanalytics)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
