[&#8249; Amazon Doc Home](./)

<h1>Amazon Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

#Prerequisites
- Currently, `Amazon` is only available for __Android__. Learn more about Amazon at: [https://developer.amazon.com/](https://developer.amazon.com/).
- Amazon Kindle Fire device

###NOTE:
If you are using __Amazon__ plugin then you must install __IAP__ plugin at first to make it to work.

##Integration
Open a terminal and use the following command to install the SDKBOX Amazon plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import amazon
$ sdkbox set store amazon
```

##Extra steps
The following step assumes you have already registered as a __Amazon Developer__ in the Amazon Developer Portal and created a new __game__ there.

###Setup Android
* Open `AndroidManifest.xml` add the following line:

```xml
<meta-data android:name="store" android:value="amazon" />
```

  NOTE: If you submit your *apk* to other store, such as __Google Play__, please remove this line or set the `store` with `googleplay`, otherwise, you will get wrong configuration for the other store. Example: `<meta-data android:name="store" android:value="googleplay" />`

```bash
$ sdkbox set store googleplay
```

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example adding `Amazon`:
```json
{
    "ios":
    {
    },
    "android":
    {
    },
    "amazon" :
    {
        "iap":
        {
            "items":{
                "remove_ads":{
                    "id":"com.cocos2dx.non1",
                    "type":"non_consumable"
                },
                "double_coin":{
                    "id":"com.cocos2dx.non2",
                    "type":"non_consumable"
                },
                "coin_package":{
                    "id":"com.cocos2dx.plugintest2"
                },
                "coin_package2":{
                    "id":"com.cocos2dx.plugintest3"
                }
            }
        }
    }
}
```

##Proguard (optional)

* Edit `project.properties` to specify a `Proguard` configuration file. Example:

```
proguard.config=proguard.cfg
```

* proguard.cfg

```
# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

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
-keep public class com.sdkbox.** { *; }
-dontwarn com.sdkbox.**

```

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.

