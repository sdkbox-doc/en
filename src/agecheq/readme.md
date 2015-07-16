<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/agecheq/v3-cpp
-->

#AgeCheq

##Integration
Use the following command to install the SDKBOX AgeCheq plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import agecheq
```

##Extra steps
<<[extra-step.md]
<<[proguard.md]

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the AgeCheq configuration, you need to replace `<app id>` and `<zone id>` items with your specific [__AgeCheq ID__](http://developer.agecheq.com/) account information.
```json
"AgeCheq":{
            "AppID":"ca0e20a3-3bb8-42e1-a5ac-55af7f63dbfc",
            "DeveloperKey":"9102be76-232b-49b1-9c4f-1c6806d3a975"
}
```

##Usage
<<[usage.md]

<<[api-reference.md]
