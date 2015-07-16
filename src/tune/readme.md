<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/tune/v3-cpp
-->

#Tune

##Integration
Use the following command to install the SDKBOX Tune plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import tune
```

##Extra steps
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Tune configuration, you need to replace
`<TUNE ID>` and `<TUNE KEY>`  with your specific [__Tune ID__](http://www.mobileapptracking.com) account information.
Here is an example adding `Tune`:
```json
"Tune":{
    "id":"<TUNE ID>",
    "key":"<TUNE KEY>",
    "debug":false
}
```

##Usage
<<[usage.md]

<<[api-reference.md]
