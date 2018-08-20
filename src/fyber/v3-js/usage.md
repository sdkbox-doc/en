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

Request Coin
```javascript
sdkbox.PluginFyber.requestDeltaOfCoins();
// sdkbox.PluginFyber.requestDeltaOfCoins("coins");

//
// **Best Practice Check**
//
// Some Offer Wall requests can take a few moments longer to load, so ensure that you've configured
// for a potential 5 second delay.

// Although we recommend you call the VCS when returning from the Offer Wall (after a short delay;
// recommended 5 seconds), you can also call when you're loading the screen that shows currency or
// after the user comes back from the Offer Wall.
```

[Fyber iOS](https://ios.fyber.com/docs/sdk-rewards#VCS%20Hosting), [Fyber Android](https://android.fyber.com/docs/learning-rewarding)

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

Display an available rewarded video, call `requestOffers()` first and then `showOffers()`. Developer can `requestOffers()` anytime, then `showOffers()` without any delay:
```javascript
sdkbox.PluginFyber.requestOffers();
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

Fetches the amount of a given currency earned since the last time this method was
invoked for the current user ID / app ID combination.
```javascript
sdkbox.PluginFyber.requestDeltaOfCoins();
```
or
```
sdkbox.PluginFyber.requestDeltaOfCoins("currencyId")
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
