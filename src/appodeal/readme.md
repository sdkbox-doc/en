[&#8249; Appodeal Doc Home](./)

<h1>Appodeal Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites
Certain SDKBOX plugins do not work together. If you use __Appodeal__, then you cannot also use the __Flurry Analytics__ and __Chartboost__ services, in the same project.

###NOTE: Please note that Appodeal only supports iOS 8.0+

##Integration
Open a terminal and use the following command to install the SDKBOX Appodeal plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import appodeal
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Appodeal configuration, you need to replace `<app_key>` items with your specific [__Appodeal Key__](http://www.appodeal.com/) account information.
```json
"Appodeal":{
    "app_key":"2cfc9cc638980eb7f5ff35d6eb63dbe404503151ccc451ed"
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* Edit the file you specified to include the following:

```
# appodeal

-keep class com.appodeal.** { *; }
-keep class com.amazon.** { *; }
-keep class com.mopub.** { *; }
-keep class org.nexage.** { *; }
-keep class com.applovin.** { *; }
-keep class com.chartboost.** { *; }
-keep class com.unity3d.ads.** { *; }
-keep class com.applifier.** { *; }
-keep class com.yandex.** { *; }
-keep class com.inmobi.** { *; }
-keep class ru.mail.android.mytarget.** { *; }
-keep class com.google.android.gms.ads.** { *; }
-keep class com.google.android.gms.common.GooglePlayServicesUtil { *; }
-keep class * extends java.util.ListResourceBundle {
  protected Object[][] getContents();
}
-keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable {
  public static final *** NULL;
}
-keepnames @com.google.android.gms.common.annotation.KeepName class *
-keepclassmembernames class * {
  @com.google.android.gms.common.annotation.KeepName *;
}
-keepnames class * implements android.os.Parcelable {
  public static final ** CREATOR;
}
-dontwarn com.facebook.ads.**
-dontwarn com.jirbo.adcolony.**
-dontwarn com.vungle.**
-dontwarn com.startapp.**
-dontwarn com.yandex.**
-dontwarn com.inmobi.**
-keep class android.support.v4.app.Fragment { *; }
-keep class android.support.v4.app.FragmentActivity { *; }
-keep class android.support.v4.app.FragmentManager { *; }
-keep class android.support.v4.app.FragmentTransaction { *; }
-keep class android.support.v4.content.LocalBroadcastManager { *; }
-keep class android.support.v4.util.LruCache { *; }
-keep class android.support.v4.view.PagerAdapter { *; }
-keep class android.support.v4.view.ViewPager { *; }

-dontwarn com.appodeal.**
-dontwarn ru.mail.android.mytarget.**


# cocos2d-x
-keep public class org.cocos2dx.** { *; }
-dontwarn org.cocos2dx.**
-keep public class com.chukong.** { *; }
-dontwarn com.chukong.**

# google play service
-keep public class com.google.android.gms.** { public *; }
-dontwarn com.google.android.gms.**

-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}

-keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable {
    public static final *** NULL;
}

-keepnames @com.google.android.gms.common.annotation.KeepName class *
-keepclassmembernames class * {
    @com.google.android.gms.common.annotation.KeepName *;
}

-keepnames class * implements android.os.Parcelable {
    public static final ** CREATOR;
}

#sdkbox
-keep class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**
```

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.

