<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/fyber/v3-cpp
-->

#Fyber

##Prerequisites
* __For Android, Fyber requires a minimum version of 4.0.3. This version is newer than what the other SDKBOX plugins require.__

##Integration
Open a terminal and use the following command to install the SDKBOX Fyber plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import fyber
```

##Extra steps

The following step assuming you already registered as a Fyber Developer
And created a new __APP__ on Fyber

###Setup iOS
* Configure your __APP__ following [iOS Quick Start Guide](http://developer.fyber.com/content/ios/)

###Setup Android
* Make sure `java -version` >= 1.7
* Configure your __APP__ on Fyber follow [Android Quick Start Guide](http://developer.fyber.com/content/android/basics/)
* Open `project.properties` and change target to `target=android-15`

## Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the Fyber configuration you can enable/disable debug mode for Fyber here
```json
"Fyber":
{
    "debug":true,
    "appid":"12345",
    "token":"34a9643edf4d3052d2bc1928b2e34d00"
}
```

<<[sdkbox-config-encrypt.md]

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
