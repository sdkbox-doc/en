## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

Use any Google Play proguard configuration that fitst your needs.
This is default proguard config:

```
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
```

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
