## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `Tune` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginTune.framework

> MobileAppTracker.framework

The above frameworks depend upon other frameworks. You also need to add the
following system frameworks, if you don't already have them:

> CoreTelephony.framework

> Security.framework

> SystemConfiguration.framework

> AdSupport.framework

> iAd.framework

> MobileCoreServices.framework

> StoreKit.framework
