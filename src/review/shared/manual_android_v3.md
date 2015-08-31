## Manual Integration For Android.

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> PluginReview.jar

> sdkbox.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

  ```
  cocos2d/cocos/platform/android/java/libs
  ```

* If you're using cocos2d-js or lua copy the __jar__ files to:

  ```
  frameworks/cocos2d-x/cocos/platform/android/java/libs
  ```

* If you're using prebuilt cocos2d-x copy the __jar__ files to:

  ```
  proj.android/libs
  ```

Copy the `pluginreview` and `sdkbox` directories from `plugin/android/jni` to your `proj.android/jni/` directory. If the `sdkbox` folder exists, it's ok to overwrite it.

Copy the `plugin_review_res_project` directory from `plugin/android` to your `proj.android` directory.
make your android project reference the `plugin_review_res_project` project.

### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_STATIC_LIBRARIES__:
```
LOCAL_STATIC_LIBRARIES += PluginReview
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
$(call import-module, ./pluginreview)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginreview)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `proj.android/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
