### Proguard (release, optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=proguard.cfg
```

* Edit the file you specified to include the following:
```
# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}
```
 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
