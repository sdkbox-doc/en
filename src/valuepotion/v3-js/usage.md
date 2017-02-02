### Register Javascript Functions
You need to register all the Valuepotion JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginValuePotionJS.hpp"
#include "PluginValuePotionJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginValuePotionJS);
sc->addRegisterCallback(register_all_PluginValuePotionJS_helper);
```

### Initialize Valuepotion
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginValuePotion.init();
```

### Using Valuepotion
After initialization you can begin to use the Valuepotion functionality. Use `check` wherever you want from your code:
```javascript
sdkbox.PluginValuePotion.setTest(true)
if (!sdkbox.PluginValuePotion.hasCachedInterstitial("default")) {
    sdkbox.PluginValuePotion.cacheInterstitial("default")
}

sdkbox.PluginValuePotion.trackEvent("test event")
sdkbox.PluginValuePotion.trackEvent("test event with value 23", 23)
sdkbox.PluginValuePotion.trackEvent("category", "event name", "label", 45)

sdkbox.PluginValuePotion.trackPurchaseEvent("test event", 56, "RMB", "order id", "product id")
sdkbox.PluginValuePotion.trackPurchaseEvent("test event", 67, "USD", "order id", "product id", "campaign id", "content id")
sdkbox.PluginValuePotion.trackPurchaseEvent("categroy", "event name", "label", 78, "ILY", "order id", "product id", "campaign id", "content id");

sdkbox.PluginValuePotion.userinfo("id", "user id")
sdkbox.PluginValuePotion.userinfo("serverid", "server id")
sdkbox.PluginValuePotion.userinfo("birth", "birther day")
sdkbox.PluginValuePotion.userinfo("gender", "M")
sdkbox.PluginValuePotion.userinfo("level", "9")
sdkbox.PluginValuePotion.userinfo("friends", "3")
sdkbox.PluginValuePotion.userinfo("accounttype", "facebook")
```

### Catch Valuepotion events (optional)
This allows you to catch the `Valuepotion` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
sdkbox.PluginValuePotion.init();
sdkbox.PluginValuePotion.setListener({
    onCacheInterstitial: function(placement) { cc.log("onCacheInterstitial ") },
    onFailToCacheInterstitial: function(placement, errorMessage) { cc.log("onFailToCacheInterstitial ") },
    onOpenInterstitial: function(placement) { cc.log("onOpenInterstitial ") },
    onFailToOpenInterstitial: function(placement, errorMessage) { cc.log("onFailToOpenInterstitial ") },
    onCloseInterstitial: function(placement) { cc.log("onCloseInterstitial ") },
    onRequestOpenURL: function(placement, URL) { cc.log("onRequestOpenURL ") },
    onRequestPurchase: function(placement, name, productId, quantity, campaignId, contentId) {
        cc.log("onRequestPurchase ");
    },
    onRequestRewards: function(placement, rewards) {
        cc.log("onRequestRewards ");
        for (var i = rewards.length - 1; i >= 0; i--) {
            var r = rewards[i]
            cc.log("%d name:%s, q:%d", i, r.name, r.quantity)
        };

    }
})
```
