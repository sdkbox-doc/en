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

Add following meta-data tags:
```xml
<meta-data android:name="com.google.android.gms.version"
    android:value="@integer/google_play_services_version" />
<meta-data android:name="com.google.android.gms.games.APP_ID" 
    android:value="@string/google_app_id" />
```

Make sure to add an entry to the file `res/values/string.xml` of the form: `<string name="google_app_id">777734739048</string>`
Change that value for your own generated play games App Id.

### Edit `Android.mk`

Edit `<project_root>/jni/Android.mk` to:

Install in a folder named `gpg` inside your `proj.android\jni` directory

Add this to your `android.mk` file

#### Add include path
```
LOCAL_C_INCLUDES += ./gpg/include/
```

#### Add static libraries

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += gpg-1
LOCAL_WHOLE_STATIC_LIBRARIES += PluginSdkboxGooglePlay
LOCAL_WHOLE_STATIC_LIBRARIES += sdkbox
```

Add a call to:
```
$(call import-add-path,$(LOCAL_PATH))
```
before any __import-module__ statements.

Add additional __import-module__ statements at the end:
```
$(call import-module, ./gpg)
$(call import-module, ./sdkbox)
$(call import-module, ./pluginsdkboxgoogleplay)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
