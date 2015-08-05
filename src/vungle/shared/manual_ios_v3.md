## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `Vungle` bundle into your Xcode project, check `Copy items if needed` when
adding frameworks:

    > sdkbox.framework

    > PluginVungle.framework

    > VungleSDK.framework

The above frameworks depend upon a large number of other frameworks. You also need to add the following system frameworks, if you don't already have them:

    > AdSupport.framework

    > AudioToolbox.framework

    > AVFoundation.framework

    > CFNetwork.framework

    > CoreGraphics.framework

    > CoreMedia.framework

    > Foundation.framework

    > libz.dylib

    > libsqlite3.dylib

    > MediaPlayer.framework

    > QuartzCore.framework

    > Security.framework

    > StoreKit.framework

    > SystemConfiguration.framework

    > UIKit.framework
