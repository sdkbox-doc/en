Manual Integration for Google Play Services SDK (dependent library only)
---

### Suggestion
Please try the SDKBOX installer first. It will do all the following step for you automatically.
```bash
$ sdkbox import googleplayservices
```


### Modify `project.properties`
An __Android Library Reference__ for __Google Play Services__ is required. The
path will be different depending upon your setup. Also, this is an additional
download that does not come as part of a standard install. To install use the
__sdk installer__ and choose __extras->google play services__. Here is an example of what this line could look like:
```
android.library.reference.1=
../android/sdk.latest/extras/google/google_play_services/libproject/
google-play-services_lib
```
__Note:__ if you already have an `android.library.reference.1` you can add
another by incrementing the number as `android.library.reference.2`, etc.


###Integration manually

We make a lite version of Google Play Services, the project repo is [https://github.com/darkdukey/Google-Play-Service-Lite](https://github.com/darkdukey/Google-Play-Service-Lite)

#### Copy Files
Copy the `gps` folder from `plugin` folder of this bundle into your project's __<project_root>/libs__ folder.

* If you're using cocos2d-x from source copy the `gps` folder to:

    Android command-line:
    ```
    cocos2d/cocos/platform/android/java/libs
    ```

    Android Studio:
    ```
    cocos2d/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using cocos2d-js or lua copy the `gps` folder to:

    Android command-line:
    ```
    frameworks/cocos2d-x/cocos/platform/android/java/libs
    ```

    Android Studio:
    ```
    frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using prebuilt cocos2d-x copy the `gps` folder to:

    Android command-line:
    ```
    <project_root>/libs
    ```


#### Modify files for Eclipse
1. Modify project.properties

```
# For source project
android.library.reference.2=../cocos2d/cocos/platform/android/java/libs/gps/

# Or
# For framework project
android.library.reference.1=libs/gps/
```

#### Modify files for Android Studio

##### 1. Modify cocos2d/cocos/platform/android/libcocos2dx/build.gradle

```
 dependencies {
+    compile project(':gps')
     compile fileTree(dir: '../java/libs', include: ['*.jar'])
 }
```

##### 2. Modify proj.android-studio/app/project.properties

```
 # Project target.
 target=android-14
+android.library.reference.1=../cocos2d/cocos/platform/android/java/libs/gps/
```

##### 3. Modify proj.android-studio/settings.gradle

```
 project(':libcocos2dx').projectDir = new File(settingsDir, '../cocos2d/cocos/platform/android/libcocos2dx')
 include ':your_project_name'
 project(':your_project_name').projectDir = new File(settingsDir, 'app')
+
+include ':gps'
+project(':gps').projectDir = new File(settingsDir, '../cocos2d/cocos/platform/android/java/libs/gps')
```
