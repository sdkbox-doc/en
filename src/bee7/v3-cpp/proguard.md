## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=proguard.cfg
```

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
