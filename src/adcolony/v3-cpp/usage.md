### Initialize AdColony
* Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginAdColony/PluginAdColony.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAdColony::init();
}
```

### Showing Ads
Display an ad wherever you want from your code, by specifying ad type:
```cpp
sdkbox::PluginAdColony::show("video");
```
or:
```cpp
sdkbox::PluginAdColony::show("v4vc");
```

### Catch AdColony events (optional)
This allows you to catch the `AdColony` events so that you can perform operations such as providing player rewards for watching the video.

* Allow your class to extend `sdkbox::AdColonyListener`
```cpp
#include "PluginAdColony/PluginAdColony.h"
class MyClass : public sdkbox::AdColonyListener
{
private:

    /*
     * Interstitial Callback
     */
    void adColonyInterstitialDidLoad(const std::string& interstitial);
    void adColonyInterstitialDidFailToLoad(const std::string& error);
    void adColonyInterstitialWillOpen(const std::string& interstitial);
    void adColonyInterstitialDidClose(const std::string& interstitial);
    void adColonyInterstitialExpired(const std::string& interstitial);
    void adColonyInterstitialWillLeaveApplication(const std::string& interstitial);
    void adColonyInterstitialDidReceiveClick(const std::string& interstitial);
    void adColonyInterstitialIapOpportunity(const std::string& interstitial, const std::string& iapProductID, int engagement);

    /*
     * Banner Callback
     */
    void adColonyAdViewDidLoad(const std::string& adView);
    void adColonyAdViewDidFailToLoad(const std::string& error);
    void adColonyAdViewWillLeaveApplication(const std::string& adView);
    void adColonyAdViewWillOpen(const std::string& adView);
    void adColonyAdViewDidClose(const std::string& adView);
    void adColonyAdViewDidReceiveClick(const std::string& adView);

    /*
     * Rewards Callback
     */
    void adColonyReward(const std::string name, const std::string& currencyName, int amount, bool success);

};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginAdColony::setListener(this);
```
