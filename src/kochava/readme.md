<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/kochava/v3-cpp
-->

#Tune

##Integration
Use the following command to install the SDKBOX Kochava plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import kochava
```

##Extra steps
<<[extra-step.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Kochava configuration, you need to replace
`<KOCHAVA_APP_ID>` with your specific [Kochava](https://kochava.com/) account information.
Here is an example adding `Kochava`:
```json
"kochava" :
{
    "kochavaAppId" : "<KOCHAVA_APP_ID>",
    "enableLogging" : 1,
    "retrieveAttribution" : 1
}
```

##Usage
<<[usage.md]

<<[api-reference.md]
