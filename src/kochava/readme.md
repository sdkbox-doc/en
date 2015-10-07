<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/kochava/v3-cpp
-->

#Kochava

##Integration
Open a terminal and use the following command to install the SDKBOX Kochava plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import kochava
```

<<[../../shared/notice.md]

## Configuration

<<[../../shared/remote_application_config.md]

### JSON Configuration
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

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

##Manual Integration For Android and Android Studio
Both __Android__ development using a command-line and using __Android Studio__ are supported. `proj.android` will be used as our `<project_root>` for __command-line__ development, while `proj.android-studio` will be used as our `<project_root>` for __Android Studio__.
<<[manual_android.md]

<<[extra-step.md]
