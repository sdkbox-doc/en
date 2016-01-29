### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

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


* If you're using cocos2d-x from source copy the __jar__ files to:

    Android command-line:
    ```
    cocos2d/cocos/platform/android/java/libs
    ```

* If you're using cocos2d-js or lua copy the __jar__ files to:

    Android command-line:
    ```
    frameworks/cocos2d-x/cocos/platform/android/java/libs
    ```

* If you're using prebuilt cocos2d-x copy the __jar__ files to:

    Android command-line:
    ```
    proj.android/libs
    ```

* If you're using android-studio, edit `proj.android-studio/app/build.gradle`, like fllow:

    head of file `proj.android-studio/app/build.gradle`:

``` gradle
    buildscript {
        repositories {
            maven {
                url 'https://maven.fabric.io/public'
            }
        }
        dependencies {
            classpath 'io.fabric.tools:gradle:1.+'
        }
    }
    apply plugin: 'com.android.application'
    apply plugin: 'io.fabric'
    repositories {
        maven { url 'https://maven.fabric.io/public' }
    }
```

__dependencies tag__ in file `proj.android-studio/app/build.gradle`


``` gradle
    dependencies {
        compile('com.twitter.sdk.android:twitter:+@aar') {
            transitive = true; exclude module: 'support-v4'
        }
    }
```


<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
* Include the following permissions above the __application tag__:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
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
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
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

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
