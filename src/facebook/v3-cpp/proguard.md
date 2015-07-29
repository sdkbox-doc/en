### Proguard (release, optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=proguard.cfg
```

* Edit the file you specified to include the following:
```
-libraryjars libs/facebook_lib/libs/android-support-v4.jar

-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}
```
 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
