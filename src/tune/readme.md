[&#8249; TUNE Doc Home](./)

<h1>TUNE Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##SDK Version
<<[../version]

##Integration
Open a terminal and use the following command to install the SDKBOX Tune plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import tune
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
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

##Extra steps

###Setup iOS
* Apply the code change to `AppController.mm` instead of `AppDelegate.cpp`

```
#import <Tune/Tune.h>

- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary *)options {
    // Pass the deep link URL to Tune
    [Tune handleOpenURL:url options:options];
    // Take care of the redirect yourself here
    ...
    return YES;
}

- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
    // Pass the deep link URL to Tune
    [Tune handleOpenURL:url sourceApplication:sourceApplication];
    // Take care of the redirect yourself here
    ...
    return YES;
}
- (BOOL)application:(UIApplication *)application continueUserActivity:(nonnull NSUserActivity *)userActivity restorationHandler:(nonnull void (^)(NSArray * _Nullable))restorationHandler {
    BOOL handledByTune = [Tune handleContinueUserActivity:userActivity restorationHandler:restorationHandler];
    // If handledByTune is false, take care of the redirect yourself
    if (!handledByTune) {
        ...
    }
    return YES;
}
```

<!--<<[sdkbox-config-encrypt.md]-->

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

