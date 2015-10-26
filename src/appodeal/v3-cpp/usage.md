### Initialize Appodeal
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginAppodeal/PluginAppodeal.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAppodeal::init();
}
```

### Using Appodeal
After initialization you can begin to use the Appodeal functionality:
```cpp
// set user id
sdkbox::PluginAppodeal::setUserVkId("user id");
// cache all type ad
sdkbox::PluginAppodeal::cacheAd(sdkbox::PluginAppodeal::AdType::AppodealAdTypeAll);
//show interstitial ad
sdkbox::PluginAppodeal::showAd(sdkbox::PluginAppodeal::ShowStyle::AppodealShowStyleInterstitial);
```

### Catch Appodeal events (optional)
This allows you to catch the `Appodeal` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::AppodealListener`
```cpp
#include "PluginAppodeal/PluginAppodeal.h"
class ADListener : public sdkbox::AppodealListener {
public:
    virtual void onBannerDidLoadAd();
    virtual void onBannerDidFailToLoadAd();
    virtual void onBannerDidClick();
    virtual void onBannerPresent();

    virtual void onInterstitialDidLoadAd();
    virtual void onInterstitialDidFailToLoadAd();
    virtual void onInterstitialWillPresent();
    virtual void onInterstitialDidDismiss();
    virtual void onInterstitialDidClick();

    virtual void onVideoDidLoadAd();
    virtual void onVideoDidFailToLoadAd();
    virtual void onVideoDidPresent();
    virtual void onVideoWillDismiss();
    virtual void onVideoDidFinish();
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginAppodeal::setListener(this);
```
