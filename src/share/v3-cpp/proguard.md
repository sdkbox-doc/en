## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* Edit the file you specified to include the following:

```
# share
-keep class com.share.** { *; }
-dontwarn com.share.**


# cocos2d-x
-keep public class org.cocos2dx.** { *; }
-dontwarn org.cocos2dx.**
-keep public class com.chukong.** { *; }
-dontwarn com.chukong.**

#sdkbox
-keep public class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**

#twitter
-keep public com.twitter.sdk.android.** { *; }
-keep public io.fabric.sdk.android.** { *; }
```

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
