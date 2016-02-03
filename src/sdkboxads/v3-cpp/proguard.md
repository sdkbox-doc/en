## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt
```

* Edit the file you specified to include each AdUnit's proguard configuration.

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
