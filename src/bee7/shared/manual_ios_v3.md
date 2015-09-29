## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of
the`Bee7` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginBee7.framework

> Bee7GWResources.bundle

The above frameworks depend upon a large number of other frameworks. You also need to add the following system frameworks, if you don't already have them:

> MessageUI.framework

> CoreMedia.framework

> SystemConfiguration.framework

> StoreKit.framework

> AdSupport.framework

> libsqlite3.dylib


Add separate linker flags to:
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -force_load PluginBee7.framework/PluginBee7

