### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> PluginGoogleAnalytics.jar

> sdkbox.jar

Copy the `plugingoogleanalytics` and `sdkbox` directories from `plugin/android/jni` to your `proj.android/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

To enable __hardware acceleration__ in your __application tag__. This tag is
optional on newer sdk versions and doesn't work on version 2.3.3.
```xml
<android:hardwareAccelerated="true" />
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
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
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

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-9
```
