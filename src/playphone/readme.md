<!--
Include Base: /Users/jtsm/Chukong-Inc/en/src/playphone/v3-cpp
-->

#Playphone
Currently, `Playphone` is only available for __Android__.

##Integration
Open a terminal and use the following command to install the SDKBOX Playphone plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import playphone
$ sdkbox import iap
```

<<[../../shared/notice.md]

##Extra steps
The following step assuming you already registered as a __Playphone Developer__ and created a new __game__ on [Playphone](https://developer.playphone.com/games/)

###Setup Android
* Open `AndroidManifest.xml` add the following line:

```
<meta-data android:name="channel" android:value="playphone" />
```

  NOTE: If you submit your *apk* to other channel, such as __Google Play__, please remove this line or set the `channel` with `googleplay`, otherwise, you will get wrong configuration for the other channel. Example: `<meta-data android:name="channel" android:value="googleplay" />`

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Playphone configuration, you need to replace `<base64EncodedPublicKey>` and `<your secret key>`  with your specific Playphone account information. Here is an example adding `Playphone`:
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
