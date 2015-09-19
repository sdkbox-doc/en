## Manual Integration For Android.

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> PluginFacebook.jar

> sdkbox.jar

Copy the `pluginfacebook` and `sdkbox` directories from `plugin/android/jni` to your `proj.android/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

Copy the `facebook_lib` directories from `plugin/android/libs` to your `proj.android/libs/` directory.

### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
```

To enable __hardware acceleration__ in your __application tag__. This tag is
optional on newer sdk versions and doesn't work on version 2.3.3.
```xml
<android:hardwareAccelerated="true" />
```

There are also a few necessary meta-data tags that also need to be added:
```xml
<meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id"/>
<activity android:name="com.facebook.FacebookActivity"
  android:configChanges=
         "keyboard|keyboardHidden|screenLayout|screenSize|orientation"
  android:theme="@android:style/Theme.Translucent.NoTitleBar"
  android:label="@string/app_name" />

  <provider android:authorities="com.facebook.app.FacebookContentProvider__replace_with_your_app_id__}"
  android:name="com.facebook.FacebookContentProvider"
  android:exported="true" />
```

### Edit strings.xml
Open `res/values/strings.xml`, Add a new string with the name
`facebook_app_id` and value as your Facebook App ID. Example:

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
      <string name="app_name">facebook</string>
      <string name="facebook_app_id">280194012150923</string>
  </resources>
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginFacebook
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
$(call import-module, ./pluginfacebook)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginfacebook)
```

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-19
```
