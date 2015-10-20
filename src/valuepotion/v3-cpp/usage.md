### Initialize Valuepotion
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginValuePotion/PluginValuePotion.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginValuePotion::init();
}
```

### Using Valuepotion
After initialization you can begin to use the Valuepotion functionality.
```cpp
sdkbox::PluginValuePotion::setTest(true);
sdkbox::PluginValuePotion::hasCachedInterstitial("default");

sdkbox::PluginValuePotion::trackEvent("test event");
sdkbox::PluginValuePotion::trackEvent("test event with value 23", 23);
sdkbox::PluginValuePotion::trackEvent("category", "event name", "label", 45);

sdkbox::PluginValuePotion::trackPurchaseEvent("test event", 56, "RMB", "order id", "product id");
sdkbox::PluginValuePotion::trackPurchaseEvent("test event", 67, "USD", "order id", "product id", "campaign id", "content id");
sdkbox::PluginValuePotion::trackPurchaseEvent("categroy", "event name", "label", 78, "ILY", "order id", "product id", "campaign id", "content id");

sdkbox::PluginValuePotion::userinfo("id", "user id");
sdkbox::PluginValuePotion::userinfo("serverid", "server id");
sdkbox::PluginValuePotion::userinfo("birth", "19991111"); //YYYYMMDD
sdkbox::PluginValuePotion::userinfo("gender", "M");
sdkbox::PluginValuePotion::userinfo("level", "9");
sdkbox::PluginValuePotion::userinfo("friends", "3");
sdkbox::PluginValuePotion::userinfo("accounttype", "facebook");
```

### Catch Valuepotion events (optional)
This allows you to catch the `Valuepotion` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::ValuePotionListener`
```cpp
#include "PluginValuePotion/PluginValuePotion.h"
class MyClass : public sdkbox::ValuePotionListener
{
private:
    virtual void onCacheInterstitial(const char *placement);

    virtual void onFailToCacheInterstitial(const char *placement, const char *errorMessage);

    virtual void onOpenInterstitial(const char *placement);

    virtual void onFailToOpenInterstitial(const char *placement, const char *errorMessage);

    virtual void onCloseInterstitial(const char *placement);

    virtual void onRequestOpenURL(const char *placement, const char *URL);

    virtual void onRequestPurchase(const char *placement, const char *name, const char *productId, int quantity, const char *campaignId, const char *contentId);

    virtual void onRequestRewards(const char *placement, std::vector<sdkbox::ValuePotionReward> rewards);
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginValuePotion::setListener(this);
```
