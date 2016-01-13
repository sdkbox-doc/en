## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of
the`Fyber` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginFyber.framework

The above frameworks depend upon a large number of other frameworks. You also need to add the following system frameworks, if you don't already have them:

> AdSupport.framework

> CoreGraphics.framework

> CoreLocation.framework

> CoreTelephony.framework

> MediaPlayer.framework

> QuartzCore.framework

> StoreKit.framework

> SystemConfiguration.framework

> Security.framework

> CFNetwork.framework

> GameController.framework

Add separate linker flags to:
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -ObjC

