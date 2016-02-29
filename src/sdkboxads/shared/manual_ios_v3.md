## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of
the `SdkboxAds` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginSdkboxAds.framework

The above frameworks depend upon a large number of other frameworks. You also need to add the following system frameworks, if you don't already have them:

> Security.framework

> AdSupport.framework

Also, *all* frameworks needed by each AdUnit you will be adding to SdkboxAds.