## Proguard (optional)
* Edit `project.properties`  to specify a `Proguard` configuration file. Example:
```
proguard.config=proguard.cfg
```

* Edit `proguard.cfg`
```
# Fyber Mediation

-keep class com.sponsorpay.mediation.** { *;}

-keepattributes JavascriptInterface

-keep class com.sponsorpay.publisher.mbe.mediation.SPBrandEngageMediationJSInterface {
    void setValue(java.lang.String);
}

-keep class android.webkit.JavascriptInterface

# Google Advertising Id

-keep class com.google.android.gms.ads.identifier.** { *; }
```
 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
