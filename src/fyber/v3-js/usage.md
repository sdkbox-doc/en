### Register Javascript Functions
You need to register all the Fyber JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFyberJS.hpp"
#include "PluginFyberJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginFyberJS);
sc->addRegisterCallback(register_all_PluginFyberJS_helper);
```

### Initialize Fyber
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginFyber.init();
```

### Using Fyber
#### Offer Wall
Displaying the Offer Wall with default placementId
```javascript
sdkbox.PluginFyber.showOfferWall();
```

Displaying the Offer Wall with custom placementId
```javascript
sdkbox.PluginFyber.showOfferWall("coins");
```

#### Rewarded Video
- iOS configure follow [rewarded-video-iOS](http://developer.fyber.com/content/ios/rewarded-video/introduction/existing-integration/)
- Android configure follow [rewarded-video-android](http://developer.fyber.com/content/android/rewarded-video/)

Queries the server for BrandEngage offers availability with default placementId.
```javascript
sdkbox.PluginFyber.requestOffers();
```

Queries the server for BrandEngage offers availability with custom placementId.
```javascript
sdkbox.PluginFyber.requestOffers("coins");
```

Display an available rewarded video, call `requestOffers` first.
```javascript
sdkbox.PluginFyber.showOffers();
```

#### Interstitials
Check if interstitial ads are available
```javascript
sdkbox.PluginFyber.requestInterstitial();
```

Shows an interstitial ad. call `requestInterstitial` first.
```javascript
sdkbox.PluginFyber.showInterstitial();
```

### Fyber events
This allows you to catch `Fyber` events so that you can perform operations after Fyber events have occurred.

```javascript
sdkbox.PluginFyber.setListener({
	onVirtualCurrencyConnectorFailed: function(error, errorCode, errorMsg) {},
	onVirtualCurrencyConnectorSuccess: function(deltaOfCoins, currencyId, currencyName, transactionId) {},
	onCanShowInterstitial: function(canShowInterstitial) {},
	onInterstitialDidShow: function() {},
	onInterstitialDismiss: function(reason) {},
	onInterstitialFailed: function() {},
	onBrandEngageClientReceiveOffers: function(areOffersAvailable) {},
	onBrandEngageClientChangeStatus: function(status, msg) {},
	onOfferWallFinish: function(status) {}
});
```
