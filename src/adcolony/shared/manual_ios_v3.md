## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `AdColony` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

    > sdkbox.framework

    > PluginAdColony.framework

    > AdColony.framework

The above frameworks depend upon a large number of other frameworks. You also need to add the following system frameworks, if you don't already have them:

    > libz.1.2.5.dylib

    > AdSupport.framework (Set to Optional)

    > AudioToolbox.framework

    > AVFoundation.framework

    > CoreGraphics.framework

    > CoreMedia.framework

    > CoreTelephony.framework

    > EventKit.framework

    > EventKitUI.framework

    > MediaPlayer.framework

    > MessageUI.framework

    > QuartzCore.framework

    > Security.framework

    > Social.framework (Set to Optional)

    > StoreKit.framework (Set to Optional)

    > SystemConfiguration.framework

    > WebKit.framework (Set to Optional)

Add two separate linker flags to:
__Target -> Build Settings -> Linking -> Other Linker Flags__:

    > -force_load AdColony.framework/AdColony

    > -fobjc-arc (this allows AdColony to use ARC even if your project does not)
