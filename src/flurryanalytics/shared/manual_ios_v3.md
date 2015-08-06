## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `FlurryAnalytics` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginFlurryAnalytics.framework

The above frameworks depend upon other frameworks. You also need to add the
following system frameworks, if you don't already have them:

> Security.framework

> SystemConfiguration.framework
