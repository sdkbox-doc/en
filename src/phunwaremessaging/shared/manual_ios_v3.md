## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `PhunwareAds` bundle into your Xcode project
>check `Copy items if needed` when adding frameworks:


> sdkbox.framework

> PluginPhunwareMessaging.framework

> PWCore.framework

> PWMessaging.framework


The above frameworks depend upon other frameworks. You also need to add the
following system frameworks
>if you don't already have them:

> CoreLocation.framework

> libz.tbd

> libsqlite3.tbd

> SystemConfiguration.framework

> GameController.framework

> MediaPlayer.framework

> MobileCoreServices.framework

> CoreTelephony.framework

