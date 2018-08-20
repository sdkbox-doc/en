### Initialize Fyber
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginFyber/PluginFyber.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFyber::init();
}
```

### Using Fyber
#### Offer Wall
Displaying the Offer Wall with default __placementId__
```cpp
sdkbox::PluginFyber::showOfferWall();
```

Displaying the Offer Wall with custom __placementId__
```cpp
sdkbox::PluginFyber::showOfferWall("coins");
```

Request Coin
```
sdkbox::PluginFyber::requestDeltaOfCoins();
// sdkbox::PluginFyber::requestDeltaOfCoins("coins");

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

Queries the server for __BrandEngage__ offers availability with __default placementId__:
```cpp
sdkbox::PluginFyber::requestOffers();
```

Queries the server for __BrandEngage__ offers availability with custom __placementId__:
```
sdkbox::PluginFyber::requestOffers("coins");
```

Display an available rewarded video, call `requestOffers()` first and then `showOffers()`. Developer can `requestOffers()` anytime, then `showOffers()` without any delay:
```cpp
sdkbox::PluginFyber::requestOffers();
sdkbox::PluginFyber::showOffers();
```

#### Interstitials
Check if interstitial ads are available:
```cpp
sdkbox::PluginFyber::requestInterstitial();
```

Shows an interstitial ad. Call `requestInterstitial` first:
```cpp
sdkbox::PluginFyber::showInterstitial();
```

Fetches the amount of a given currency earned since the last time this method was invoked for the current user ID / app ID combination:
```cpp
sdkbox::PluginFyber::requestDeltaOfCoins();
```
or:
```
sdkbox::PluginFyber::requestDeltaOfCoins("currencyId")
```

### Fyber events
This allows you to catch `Fyber` events so that you can perform operations after Fyber events have occurred.

* Allow your class to extend `sdkbox::FyberListener` and override the functions listed:
```cpp
#include "PluginFyber/PluginFyber.h"
class MyClass : public sdkbox::FyberListener
{
private:
	void onVirtualCurrencyConnectorFailed(int error,
	                                              const std::string& errorCode,
	                                              const std::string& errorMsg);
	void onVirtualCurrencyConnectorSuccess(double deltaOfCoins,
	                                               const std::string& currencyId,
	                                               const std::string& currencyName,
	                                               const std::string& transactionId);
	void onCanShowInterstitial(bool canShowInterstitial);
	void onInterstitialDidShow();
	void onInterstitialDismiss(const std::string& reason);
	void onInterstitialFailed();
	void onBrandEngageClientReceiveOffers(bool areOffersAvailable);
	void onBrandEngageClientChangeStatus(int status, const std::string& msg);
	void onOfferWallFinish(int status);
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginFyber::setListener(this);
```
