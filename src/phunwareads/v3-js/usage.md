### Register Javascript Functions
You need to register all the PhunwareAds JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginPhunwareAdsJS.hpp"
#include "PluginPhunwareAdsJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginPhunwareAdsJS);
sc->addRegisterCallback(register_all_PluginPhunwareAdsJS_helper);
```

### Initialize PhunwareAds
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginPhunwareAds.init();
```

### Showing Ads
Display an ad where ever you want from your code:
```javascript
// To use customized location
sdkbox.PluginPhunwareAds.show("your_ad_name");
```

### Cache Ads
```javascript
sdkbox.PluginPhunwareAds.cache("your_ad_name")
```

### Hide Ads
```javascript
sdkbox.PluginPhunwareAds.hide("your_ad_name")
```

### Catch PhunwareAds events (optional)
This allows you to catch the `PhunwareAds` events so that you can perform operations such as providing player rewards for viewing ads.

* Create a listener (demonstrated by logging events):
```javascript
sdkbox.PluginPhunwareAds.setListener({

    adLoaded : function(name) { cc.log("adLoaded " + name) },
    adFailed : function(name, errorCode, msg) { cc.log("adFailed " + name + " " + msg) },
    adWillPresent : function(name) { cc.log("adWillPresent " + name) },
    adDidPresent : function(name) { cc.log("adDidPresent " + name) },
    adWillDissmiss : function(name) { cc.log("adWillDissmiss " + name) },
    adDidDismiss : function(name) { cc.log("adDidDismiss " + name) },
    willLeaveApp : function(name) { cc.log("willLeaveApp " + name)},
    reward : function(name, amount, currency) { cc.log("reward " + name) },

})
```
