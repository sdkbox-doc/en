### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> android-support-v4.jar

> fabric.jar

> retrofit-1.8.0.jar

> twitter.jar

> PluginShare.jar

> sdkbox.jar

> digits

> tweetcomposer

> tweetui

> twittercore


<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
* Include the following permissions above the __application tag__:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.SEND_SMS"/>

```

* Include the following lines above the __application tag__:

```xml
<meta-data
            android:name="io.fabric.ApiKey"
            android:value="your fabric id(0673fbd412c9b67c9ac2182659839d92b93f2f65)" />

<activity
    android:name="com.twitter.sdk.android.core.identity.OAuthActivity"
    android:configChanges="orientation|screenSize"
    android:excludeFromRecents="true"
    android:exported="false" />

<service
    android:name="com.twitter.sdk.android.tweetcomposer.TweetUploadService"
    android:enabled="true"
    android:exported="false" />
```

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginShare
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
$(call import-module, ./pluginshare)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginshare)
```

### Edit `Aplication.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-9
```
