### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> PluginSdkboxPlay.jar

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

Copy the `sdkboxplay_lib` directories from `plugin/android/libs` to your `<project_root>/libs/` directory.

<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.GET_ACCOUNTS" />
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
LOCAL_WHOLE_STATIC_LIBRARIES += PluginSdkboxPlay
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
$(call import-module, ./pluginsdkboxplay)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginsdkboxplay)
```

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PLATFORM__ version requirements:
```
APP_PLATFORM := android-10
```

