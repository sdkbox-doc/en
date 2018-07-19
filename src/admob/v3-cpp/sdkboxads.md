# SDKBoxAds

You can use `SDKBoxAds` api to display AdMob ads. Also need to update your `sdkbox_config.json`:

```
    {
        "android": {
            "SdkboxAds": {
                "units": [
                    "AdMob" // Add Ad mediations, ["AdColony", "AdMob", "Chartboost", "Appnext", "UnityAds"]
                ],
                "placements": [
                    {
                        "id": "placement-admob", // ad group name
                        "strategy": "round-robin", // ["round-robin", "weight"]
                        "units": [
                            {
                                "unit": "AdMob", // Mediation name
                                "name": "gameover" // Ad name, comes from "AdMob" ads section
                            }
                        ]
                    }
                ]
            }
        },
        "ios": {
            "SdkboxAds": {
                "debug": true,
                "units": [
                    "AdMob"
                ],
                "placements": [
                    {
                        "id": "ads1",
                        "strategy": "round-robin",
                        "units": [
                            {
                                "unit": "AdMob",
                                "name": "gameover"
                            }
                        ]
                    }
                ]
            }
        }
    }
```



## SDKBoxAds Core API

> check ads available

```c++
sdkbox::PluginSdkboxAds::isAvailable(placementName)
// sdkbox::PluginSdkboxAds::isAvailable("ads1")
```

> show the ads

```c++
sdkbox::PluginSdkboxAds::placement(placementName)
// sdkbox::PluginSdkboxAds::placement("ads1")
```


