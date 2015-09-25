### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> PluginFacebook.jar

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
	proj.android/libs
	```

Copy the `pluginfacebook` and `sdkbox` directories from `plugin/android/jni` to your `<project_root>/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

Copy the `facebook_lib` directories from `plugin/android/libs` to your `<project_root>/libs/` directory.


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
  <uses-permission android:name="android.permission.INTERNET" />
```

There are also a few necessary meta-data tags that also need to be added:
```xml
<meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id"/>
<activity android:name="com.facebook.FacebookActivity"
  android:configChanges=
         "keyboard|keyboardHidden|screenLayout|screenSize|orientation"
  android:theme="@android:style/Theme.Translucent.NoTitleBar"
  android:label="@string/app_name" />

  <provider android:authorities="com.facebook.app.FacebookContentProvider__replace_with_your_app_id__"
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
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
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

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
