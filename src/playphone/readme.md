<!--
Include Base: /Users/jtsm/Chukong-Inc/en/src/playphone/v3-cpp
-->

#Playphone
Currently, `Playphone` is only available for __Android__.  Playphone is the leading games-only platform in emerging markets. Learn more about Playphone at: http://playphone.com.

##Integration
Open a terminal and use the following command to install the SDKBOX Playphone plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import playphone
```

##Extra steps
The following step assumes you have already registered as a __Playphone Developer__ in the Playphone Developer Portal and created a new __game__ there.

###Setup Android
* Open `AndroidManifest.xml` add the following line:

```xml
<meta-data android:name="store" android:value="playphone" />
<meta-data android:name="leaderboard" android:value="playphone" />
```

  NOTE: If you submit your *apk* to other store, such as __Google Play__, please remove this line or set the `store` with `googleplay`, otherwise, you will get wrong configuration for the other store. Example: `<meta-data android:name="store" android:value="googleplay" />`

```bash
$ sdkbox set store googleplay
```

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Playphone configuration, you need to replace `<base64EncodedPublicKey>` and `<your secret key>`  with your specific Playphone account information.

The <base64EncodedPublicKey> is the Public License Key for the game that can be found in the General section for that game in the Playphone Developer Portal.

 <your secret key> is a unique key that identifies you as the Playphone developer and can be found in the Company section of the Profile page of the Playphone Developer Portal.

Here is an example adding `Playphone`:
```json
{
    "ios":
    {
    },
    "android":
    {
    },
    "playphone" :
    {
        "skey":"<your secret key>",
        "iap":
        {
            "key":"<base64EncodedPublicKey>",
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

#playphone
-keep public class com.playphone.psgn.** { *; }
-dontwarn com.playphone.psgn.**
```

 __Note:__ Proguard only works with __Release__ builds (i.e `cocos run -m release`) debug builds do not invoke Proguard rules.
 