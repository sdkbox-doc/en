[&#8249; SdkboxAds Doc Home](./)

<h1>SdkboxAds Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Prerequisites
* None

##Integration
Open a terminal and use the following command to install the SDKBOX SdkboxAds plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import sdkboxadsplus
```

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the SdkboxAds configuration:
```json
    "SdkboxAds": {
        "units": [
                "AdColony",
                "Fyber",
                "Chartboost",
                "Vungle"
            ],
        "placements": [
            {
                "id" : "placement-1",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "AdColony",
                      "name": "video"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Default"
                    }
                ]
            },
            {
                "id" : "placement-2",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "Vungle",
                      "name": "reward"
                    },
                    {
                      "unit": "AdColony",
                      "name": "v4vc"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Next Level"
                    }
                ]
            }
        ]
    }
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
