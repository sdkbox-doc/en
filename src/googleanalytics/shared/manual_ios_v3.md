## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of
the`GoogleAnalytics` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginGoogleAnalytics.framework

The above frameworks depend upon other frameworks. You also need to add the
following system frameworks, if you don't already have them:

> CoreData.framework

> Security.framework

> SystemConfiguration.framework

> libz.dylib

> libsqlite3.dylib

> libAdIdAccess.a (optional, required for IDFA)

> AdSupport.framework (optional, required for IDFA)

Add a linker flag, if your setup requires it, to:
__Target -> Build Settings -> Linking -> Other Linker Flags__:

> -force_load /path/to/libAdIdAccess.a
