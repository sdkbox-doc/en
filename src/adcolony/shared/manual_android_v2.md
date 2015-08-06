## Manual Integration For Android.

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> adcolony.jar

> PluginAdColony.jar

> sdkbox.jar

Copy the `pluginadcolony` and `sdkbox` directories from `plugin/android/jni`
to your `proj.android/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

### 2.2 Edit `AndroidManifest.xml`
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
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_STATIC_LIBRARIES__:
```
LOCAL_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_STATIC_LIBRARIES += PluginAdColony
LOCAL_STATIC_LIBRARIES += sdkbox
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

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-9
```
