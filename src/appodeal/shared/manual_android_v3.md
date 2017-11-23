### Copy Files
Copy the following __jar__ files from `plugin/android/libs` folder of this
bundle into your project’s __<project_root>/libs__ folder.

> PluginAppodeal.jar

> sdkbox.jar

> android-support-v4-22.2.1.jar

> applovin-sdk-6.0.1.jar

> appodeal-1.13.1.jar

> chartboost-5.2.0.jar

> my-target-4.0.13.jar

> unity-ads-1.4.7.jar


* If you're using cocos2d-x from source copy the __jar__ files to:

	Android command-line:
	```
	cocos2d/cocos/platform/android/java/libs
	```

    Android Studio:
    ```
    cocos2d/cocos/platform/android/java/libs
    cocos2d/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using cocos2d-js or lua copy the __jar__ files to:

	Android command-line:
	```
	frameworks/cocos2d-x/cocos/platform/android/java/libs
	```

    Android Studio:
    ```
    frameworks/cocos2d-x/cocos/platform/android/java/libs
    frameworks/cocos2d-x/cocos/platform/android/libcocos2dx/libs
    ```

* If you're using prebuilt cocos2d-x copy the __jar__ files to:

	Android command-line:
	```
	proj.android/libs
	```


<<[../../shared/copy_jni_lib.md]


### Edit `AndroidManifest.xml`
Include the following permissions above the __application tag__:
```xml
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

There are also necessary meta-data and activity tags that also need to be added:
```xml
<meta-data android:name="com.appodeal.framework" android:value="sdkbox" />
<activity android:name="com.appodeal.ads.InterstitialActivity"
        android:configChanges="orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar" />
<activity android:name="com.appodeal.ads.VideoActivity"
        android:configChanges="orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar" />

<activity android:name="com.appodeal.ads.LoaderActivity"
        android:configChanges="orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar" />

<meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version" />

<activity android:name="com.google.android.gms.ads.AdActivity"
        android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"
        android:theme="@android:style/Theme.Translucent" />

<activity android:name="com.chartboost.sdk.CBImpressionActivity"
        android:theme="@android:style/Theme.Translucent"
        android:excludeFromRecents="true" />

<activity android:name="com.applovin.adview.AppLovinInterstitialActivity"
        android:theme="@android:style/Theme.Translucent" />

<activity android:name="com.mopub.mobileads.MoPubActivity"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Translucent" />
<activity android:name="com.mopub.common.MoPubBrowser"
        android:configChanges="keyboardHidden|orientation|screenSize" />
<activity android:name="com.mopub.mobileads.MraidActivity"
        android:configChanges="keyboardHidden|orientation|screenSize" />
<activity android:name="com.mopub.mobileads.MraidVideoPlayerActivity"
        android:configChanges="keyboardHidden|orientation|screenSize" />

<activity android:name="org.nexage.sourcekit.mraid.MRAIDBrowser"
        android:configChanges="orientation|keyboard|keyboardHidden|screenSize"
        android:theme="@android:style/Theme.Translucent" />

<activity android:name="com.amazon.device.ads.AdActivity"
        android:configChanges="keyboardHidden|orientation|screenSize"/>

<activity android:name="com.unity3d.ads.android.view.UnityAdsFullscreenActivity"
        android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
        android:hardwareAccelerated="true" />

<activity android:name="ru.mail.android.mytarget.ads.MyTargetActivity"
        android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"/>

<activity android:name="org.nexage.sourcekit.vast.activity.VASTActivity"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen" />

<activity android:name="com.facebook.ads.InterstitialAdActivity"
        android:configChanges="keyboardHidden|orientation|screenSize" />

<activity android:name="com.jirbo.adcolony.AdColonyOverlay"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyFullscreen"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
<activity android:name="com.jirbo.adcolony.AdColonyBrowser"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />

<activity android:name="com.vungle.publisher.FullScreenAdActivity"
        android:configChanges="keyboardHidden|orientation|screenSize"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"/>
```

### Edit `Android.mk`
Edit `<project_root>/jni/Android.mk` to:

Add additional requirements to __LOCAL_WHOLE_STATIC_LIBRARIES__:
```
LOCAL_WHOLE_STATIC_LIBRARIES += PluginAppodeal
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
$(call import-module, ./pluginappodeal)
```

This means that your ordering should look similar to this:
```
$(call import-add-path,$(LOCAL_PATH))
$(call import-module, ./sdkbox)
$(call import-module, ./pluginappodeal)
```

  __Note:__ It is important to make sure these statements are above the existing `$(call import-module,./prebuilt-mk)` statement, if you are using the pre-built libraries.

### Modify `Application.mk` (Cocos2d-x v3.0 to v3.2 only)
Edit `<project_root>/jni/Application.mk` to make sure __APP_STL__ is defined
correctly. If `Application.mk` contains `APP_STL := c++_static`, it should be
changed to:
```
APP_STL := gnustl_static
```
