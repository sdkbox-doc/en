### Copy Files
Copy the everything from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.GET_TASKS"/>
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginApteligent
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
$(call import-module, ./pluginapteligent)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginapteligent)
```

### Edit `Application.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-15
```

