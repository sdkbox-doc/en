### Proguard (release, optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=proguard.cfg
```

* Edit the file you specified to include the following:
```
-libraryjars libs/android-support-v4.jar

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
