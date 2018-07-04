## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* Edit the file you specified to include the following:

```
# flurry
-keep class com.flurry.** { *; }
-dontwarn com.flurry.**
-keepattributes *Annotation*,EnclosingMethod,Signature
-keepclasseswithmembers class * {
    public <init>(android.content.Context, android.util.AttributeSet, int);
}

# Google Play Services library
-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}

-keep class com.google.protobuf.** { *; }
-dontwarn com.google.protobuf.**

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

#If you are using the Google Mobile Ads SDK, add the following:
# Preserve GMS ads classes
-keep class com.google.android.gms.** { *;
}
-dontwarn com.google.android.gms.**


#If you are using the InMobi SDK, add the following:
# Preserve InMobi Ads classes
-keep class com.inmobi.** { *;
}
-dontwarn com.inmobi.**
#If you are using the Millennial Media SDK, add the following:
# Preserve Millennial Ads classes
-keep class com.millennialmedia.** { *;
}
-dontwarn com.millennialmedia.**



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
