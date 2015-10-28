<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/bee7/v3-cpp
-->

#Bee7

##Prerequisites
* __For Android, Bee7 requires a minimum version of 4.0.3. This version is newer than what the other SDKBOX plugins require.__

* __For iOS, Bee7's game wall is currently supporting only portrait.__

##Integration
Open a terminal and use the following command to install the SDKBOX Bee7 plugin. Make sure you setup SDKBOX installer correctly.
```bash
$ sdkbox import bee7
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically create a sample configuration `sdkbox_config.json` for you

Here is an example of the Bee7 configuration you can enable/disable debug mode for Bee7 here

```json
"Bee7":
{
    "debug":true,
    "key":"FE74A9C4-1288-4F6F-8D6E-C365699F2C72"
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage

##Extra steps
The following step assumes you already registered at [Bee7](http://bee7.com/), created a new __APP__ and activated it.

###Setup iOS
* Modify `Info.plist`, add URL Schemes:

	__Target -> Info -> URL Types__:

	1. click "+"
	2. fill "URL Schemes" with "your bee7 scheme"

###Setup Android
* Open `AndroidManifest.xml` and replace `_replace_with_your_bee7_scheme_` with your `bee7 scheme`
* Open `project.properties` and change target to `target=android-21`

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

##Manual Integration For Android and Android Studio
Both __Android__ development using a command-line and using __Android Studio__ are supported. `proj.android` will be used as our `<project_root>` for __command-line__ development, while `proj.android-studio` will be used as our `<project_root>` for __Android Studio__.
<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
