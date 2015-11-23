### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> PluginBee7.jar

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


Copy the `bee7-android-sdk-gamewall` directories from `plugin/android/libs` to your `<project_root>/libs/` directory.


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

Make sure that you have one of the two settings below, for proper function of the game wall’s video component:

  - `<uses-sdk>` with targetSdkVersion set to the latest Android SDK version available, for example:

    ```xml
    <uses-sdk android:minSdkVersion="9" android:targetSdkVersion="23" .../>
    ```

  - The flag `android:hardwareAccelerated` set to `true` for your application (or for the activity that
    will display the game wall – that is a custom main activity):

    ```xml
        <application android:label="@string/app_name"
                 android:icon="@drawable/icon"
                 android:hardwareAccelerated="true">
        </application>
    ```

There are also a few necessary meta-data tags that also need to be added:

```xml
<activity>
  <intent-filter>
      <action android:name="android.intent.action.VIEW"/>
      <category android:name="android.intent.category.DEFAULT"/>
      <category android:name="android.intent.category.BROWSABLE"/>
      <data android:scheme="your_bee7_scheme" android:host="publisher"/>
  </intent-filter>
</activity>

<service
  android:name="com.bee7.sdk.service.RewardingService"
  android:process=":rewardingservice"
  android:enabled="true">
</service>

<receiver android:name="com.bee7.sdk.publisher.RewardReceiver" android:enabled="true" android:exported="true">
    <intent-filter>
        <action android:name="com.bee7.action.REWARD" />
    </intent-filter>
</receiver>

<receiver
  android:name="com.bee7.sdk.service.RewardingServiceReceiver"
  android:enabled="true"
  android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.USER_PRESENT" />
    </intent-filter>
</receiver>
```

### Edit `Android.mk`
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginBee7
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
$(call import-module, ./pluginbee7)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginbee7)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-21
```

### Edit `project.property`

```
android.library.reference.1=./libs/bee7-android-sdk-gamewall
```
