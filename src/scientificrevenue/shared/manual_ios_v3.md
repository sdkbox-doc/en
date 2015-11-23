## Manual Integration For iOS
Drag and drop the following frameworks from the __plugins/ios__ folder of the `PluginScientificRevenue` bundle into your Xcode project, check `Copy items if needed` when adding frameworks:

> sdkbox.framework

> ScientificRevenueSDK.framework

> PluginScientificRevenue.framework

The above frameworks depend upon other frameworks. You also need to add the following system frameworks, if you don't already have them:

> Security.framework

> StoreKit.framework

> SystemConfiguration.framework

> AddressBook.framework

> CoreLocation.framework

> MediaPlayer.framework

> GameController.framework

> CFNetwork.framework

> CoreData.framework

> MobileCoreService.framework

Add the linker flag "-force_load ScientificRevenueSDK.framework/ScientificRevenueSDK"