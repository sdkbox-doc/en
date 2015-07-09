### Proguard (release, optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=proguard.cfg
```

* Edit the file you specified to include the following:
```
-dontwarn com.vungle.**
-keep class com.vungle.** { public *; }
-keep class javax.inject.*
```
 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
