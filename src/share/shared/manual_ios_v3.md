## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `Share` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> PluginShare.framework

> TwitterCore.framework

> TwitterKit.framework

> TwitterKitResources.bundle -> TwitterKit.framework/TwitterKitResources.bundle

> TwitterShareExtensionUIResources.bundle -> TwitterKit.framework/TwitterShareExtensionUIResources.bundle

add the following system frameworks, if you don't already have them:

> Accounts.framework

> CoreText.framework

> CoreMedia.framework

> CoreData.framework

> Social.framework

> GameController.framework

> SystemConfiguration.framework

> MediaPlayer.framework

> MessageUI.framework

> CoreMotion.framework

> SafariServices.framework
