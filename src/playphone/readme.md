<!--
Include Base: /Users/jtsm/Chukong-Inc/en/src/playphone/v3-cpp
-->

#Playphone
Currently, `Playphone` is only support `android`.

##Integration
Open a terminal and use the following command to install the SDKBOX Playphone plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import playphone
```

<<[../../shared/notice.md]

##Extra steps
The following step assuming you already registered as a Playphone Developer
And created a new __game__ on [Playphone](https://developer.playphone.com/games/)

###Setup Android
* Open `AndroidManifest.xml` add the following line:

```
<meta-data android:name="channel" android:value="playphone" />
```

*NOTE: If you submite your apk to other channel, such as `Google play`, please remove this line or set the `channel` with empty value, otherwise, you
will get wrong configuration for the other channel.*

example:

```
<meta-data android:name="channel" android:value="" />
```

# Open `AndroidManifest.xml` and replace `your_package_name` with android 
  package name, such as `org.cocos2dx.cpp`.


## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Playphone configuration, you need to replace `<base64EncodedPublicKey>` and `<your secret key>`  with your specific [Playphone](https://playphone.com/) account information.
Here is an example adding `playphone`:
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
        "iap":
        {
            "key":"<base64EncodedPublicKey>",
            "skey":"<your secret key>",
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

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[manual_integration.md]

##Manual Integration For Android and Android Studio
Both __Android__ development using a command-line and using __Android Studio__ are supported. `proj.android` will be used as our `<project_root>` for __command-line__ development, while `proj.android-studio` will be used as our `<project_root>` for __Android Studio__.
<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
