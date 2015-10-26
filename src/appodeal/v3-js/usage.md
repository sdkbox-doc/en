### Register Javascript Functions
You need to register all the Appodeal JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAppodealJS.hpp"
#include "PluginAppodealJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginAppodealJS);
sc->addRegisterCallback(register_all_PluginAppodealJS_helper);
```

### Initialize Appodeal
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginAppodeal.init();
```

### Using Appodeal
After initialization you can begin to use the Appodeal functionality:
```cpp
plugin.setUserVkId("user id");
plugin.cacheAd(15);
```

### Catch Appodeal events (optional)
This allows you to catch the `Appodeal` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginAppodeal
plugin.setListener({
    onBannerDidLoadAd: function() { cc.log("onBannerDidLoadAd") },
    onBannerDidFailToLoadAd: function() { cc.log("onBannerDidFailToLoadAd") },
    onBannerDidClick: function() { cc.log("onBannerDidClick") },
    onBannerPresent: function() { cc.log("onBannerPresent") },
    onInterstitialDidLoadAd: function() { cc.log("onInterstitialDidLoadAd") },
    onInterstitialDidFailToLoadAd: function() { cc.log("onInterstitialDidFailToLoadAd") },
    onInterstitialWillPresent: function() { cc.log("onInterstitialWillPresent") },
    onInterstitialDidDismiss: function() { cc.log("onInterstitialDidDismiss") },
    onInterstitialDidClick: function() { cc.log("onInterstitialDidClick") },
    onVideoDidLoadAd: function() { cc.log("onVideoDidLoadAd") },
    onVideoDidFailToLoadAd: function() { cc.log("onVideoDidFailToLoadAd") },
    onVideoDidPresent: function() { cc.log("onVideoDidPresent") },
    onVideoWillDismiss: function() { cc.log("onVideoWillDismiss") },
    onVideoDidFinish: function() { cc.log("onVideoDidFinish") }
})
plugin.init()
```
