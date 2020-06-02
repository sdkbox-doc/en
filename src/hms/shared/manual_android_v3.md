### Copy Files
#### Copy jar files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project's __<project_root>/libs__ folder.

> PluginHMS.jar

> sdkbox.jar


<<[../../shared/copy_jars.md]

<<[../../shared/copy_jni_lib.md]

### Edit `build.gradle`

your modification maybe look like following:

project root gradle file
```gradle

buildscript {
    repositories {
        google()
        jcenter()
        maven { url 'https://developer.huawei.com/repo/' } // for hms
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.4.1'
        classpath 'com.huawei.agconnect:agcp:1.2.1.301' // for hms
    }
}

allprojects {
    repositories {
        google()
        jcenter()
        maven { url 'https://developer.huawei.com/repo/' } // for hms
    }
}

```

application's build.gradle
```gradle
apply plugin: 'com.android.application'
apply plugin: 'com.huawei.agconnect' // for hms

...

dependencies {
    ...
    implementation 'com.huawei.hms:hwid:4.0.1.301' // for hms
    implementation 'com.huawei.hms:iap:4.0.2.300' // for hms
}

```


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="com.android.vending.BILLING"/>
```

### Edit `Android.mk`
Edit `<project_root>/jni/Android.mk` to:

Add additional dependencies to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginHMS
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
$(call import-module, ./pluginhms)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginhms)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 - v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
