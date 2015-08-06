<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/tune/v3-cpp
-->

#Tune

##Integration
Open a terminal and use the following command to install the SDKBOX Tune plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import tune
```

##Extra steps for Android
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

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_ios.md]

<<[manual_android.md]
