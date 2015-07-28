<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/facebook/v3-cpp
-->

#Facebook

##Integration
Use the following command to install the SDKBOX Facebook plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import facebook
```

##Extra steps
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the Facebook configuration there isn't much to do here except set your debug preference.
```json
"Facebook":
{
    "debug":true
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]
