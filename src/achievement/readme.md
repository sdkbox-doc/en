<!--
Include Base: /Users/jtsm/Chukong-Inc/pr/en/src/achievement/v3-cpp
-->

#Achievement

##Prerequisites
* Only support `Android` now

supported backend:
- playphone
    + if you using playphone as backend, please call `IAP::init()` to initialize playphone

##Integration
Open a terminal and use the following command to install the SDKBOX Achievement plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import achievement
```

Add backend.
```
$ sdkbox import playphone
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]

<<[sdkbox-config-encrypt.md]-->

##Usage

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]
