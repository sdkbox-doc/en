**NOTE**: not support eclipse project right now

### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __proj.android/libs__ folder.

> sdkbox.jar


<<[../../shared/copy_jni_lib.md]


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

### Edit `Android.mk`
Edit `proj.android/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += android_native_app_glue
LOCAL_LDLIBS += -landroid
LOCAL_LDLIBS += -llog
LOCAL_WHOLE_STATIC_LIBRARIES += PluginPhunwareMessaging
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
$(call import-module, ./pluginphunwaremessaging)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginphunwaremessaging)
```

### Edit `Application.mk`
Edit `proj.android/jni/Application.mk` to:

Add __APP_PATFORM__ version requirements:
```
APP_PLATFORM := android-16
```

### Edit `AndroidManifest.xml`

Edit `manifest`. Example:

    ```
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
              package="org.cocos2dx.cpp3141"
              xmlns:ns1="http://schemas.android.com/tools" <!-- ADD THIS LINE -->
              android:installLocation="auto" android:versionCode="1"
              android:versionName="1.0">
    ```

Edit `application`. Example:

    ```
    <application android:icon="@drawable/icon"
                 ns1:replace="android:label" <!-- ADD THIS LINE -->
                 android:label="@string/app_name" >

        <!-- ADD START-->
        <activity android:name=".AppActivity">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <data android:mimeType="locationmessaging/message" />
            </intent-filter>
        </activity>
        <!-- ADD END-->

    </application>
    ```

### Edit `build.gradle`

Edit `cocos2d/cocos/platform/android/libcocos2dx/build.gradle`. Example:

    ```
    ...
    android {
        compileSdkVersion 23                    # THIS LINE
        buildToolsVersion "23.0.3"              # THIS LINE
        useLibrary  'org.apache.http.legacy'    # THIS LINE


        defaultConfig {
            minSdkVersion 16                    # THIS LINE
            targetSdkVersion 22                 # THIS LINE
            versionCode 1
            versionName "1.0"
        }

        ...
    }
    ...
    ```

Edit `proj.android-studio/app/build.gradle`


    ```
    android {
    +    compileSdkVersion 23
    +    buildToolsVersion "23.0.3"
    +    useLibrary  'org.apache.http.legacy'

         defaultConfig {
             applicationId "org.cocos2dx.cpp3141"   <!-- MUST SAME WITH google-services.json -->
    +        minSdkVersion 16
             targetSdkVersion 22
             versionCode 1
             versionName "1.0"

             ...

         buildTypes {
    +        debug {
    +            ndk {
    +                abiFilters = ["armeabi"]
    +            }
    +        }
    +
             release {
    +            ndk {
    +                abiFilters = ["armeabi"]
    +            }
    +
                 minifyEnabled false
                 proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
                 if (project.hasProperty("RELEASE_STORE_FILE")) {

                 ...

     dependencies {
    +    compile 'com.google.android.gms:play-services-maps:9.6.1'
    +    compile 'com.android.support:appcompat-v7:23.3.0'
    +    compile 'com.phunware.messaging:messaging:3.0.4'
         compile fileTree(dir: 'libs', include: ['*.jar'])
         compile project(':libcocos2dx')
     }

     clean.dependsOn cleanAssets
     preBuild.dependsOn copyAssets
    +
    +apply plugin: 'com.google.gms.google-services'
    ```

Edit `proj.android-studio/build.gradle`

    ```
             // NOTE: Do not place your application dependencies here; they belong
             // in the individual module build.gradle files
    +        classpath 'com.google.gms:google-services:3.0.0'
    +
         }
     }

     allprojects {
         repositories {
             jcenter()
    +        maven {
    +            url "https://nexus.phunware.com/content/groups/public/"
    +        }
         }
     }
    ```
