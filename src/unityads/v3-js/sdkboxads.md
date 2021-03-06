# SDKBoxAds

You can use `SDKBoxAds` api to display AdMob ads. Also need to update your `sdkbox_config.json`:

```
    {
        "android": {
            "SdkboxAds": {
                "units": [
                    "UnityAds" // Add Ad mediations, ["AdColony", "AdMob", "Chartboost", "Appnext", "UnityAds"]
                ],
                "placements": [
                    {
                        "id": "placement-admob", // ad group name
                        "strategy": "round-robin", // ["round-robin", "weight"]
                        "units": [
                            {
                                "unit": "UnityAds", // Mediation name
                                "name": "video" // Ad name, comes from "AdMob" ads section
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
                    "UnityAds"
                ],
                "placements": [
                    {
                        "id": "ads1",
                        "strategy": "round-robin",
                        "units": [
                            {
                                "unit": "UnityAds",
                                "name": "video"
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

```javascript
sdkbox.PluginSdkboxAds.isAvailable(placementName)
// sdkbox.PluginSdkboxAds.isAvailable("ads1")
```

> show the ads

```javascript
sdkbox.PluginSdkboxAds.placement(placementName)
// sdkbox.PluginSdkboxAds.placement("ads1");
```


