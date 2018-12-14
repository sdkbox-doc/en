[&#8249; Tapcore Doc Home](./)

<h1>Tapcore Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##SDK Version
<<[../version]

##Integration
First, you must sign up for [Tapcore](http://tapcore.com/?refid=Y3DgX).

Second, Open a terminal and use the following command to install the SDKBOX Tapcore plugin.
```bash
$ sdkbox import tapcore --apitoken "your_profile_token"
```

**NOTE**

Tapcore support lots of `APP_ABI`:

```
     0  01-04-2018 08:38   lib/x86_64/
     9880  01-04-2018 08:38   lib/x86_64/libdVexZld.so
        0  01-04-2018 08:38   lib/mips64/
    14472  01-04-2018 08:38   lib/mips64/libdVexZld.so
        0  01-04-2018 08:38   lib/mips/
    71228  01-04-2018 08:38   lib/mips/libdVexZld.so
        0  01-04-2018 08:38   lib/arm64-v8a/
     9616  01-04-2018 08:38   lib/arm64-v8a/libdVexZld.so
        0  01-04-2018 08:38   lib/armeabi-v7a/
    13564  01-04-2018 08:38   lib/armeabi-v7a/libdVexZld.so
        0  01-04-2018 08:38   lib/x86/
     9360  01-04-2018 08:38   lib/x86/libdVexZld.so
        0  01-04-2018 08:38   lib/armeabi/
    13552  01-04-2018 08:38   lib/armeabi/libdVexZld.so
```

plz remove those `ABI` that your game do not support. How to check your game abi:

1. unzip your.apk
2. check folder name in `libs`

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]
