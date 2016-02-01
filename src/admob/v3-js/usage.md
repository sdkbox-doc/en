### Register Javascript Functions
You need to register all the AdMob JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAdMobJS.hpp"
#include "PluginAdMobJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginAdMobJS);
sc->addRegisterCallback(register_all_PluginAdMobJS_helper);
```

### Initialize AdMob
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginAdMob.init();
```

### cache ad
```javascript
sdkbox.PluginAdMob.cache("home");
sdkbox.PluginAdMob.cache("gameover");
```

### show ad
```javascript
sdkbox.PluginAdMob.show("home");
sdkbox.PluginAdMob.show("gameover");
```

### hide ad
You can not hide an interstitial ad
```javascript
sdkbox.PluginAdMob.hide("home");
```

### check ad available
```javascript
sdkbox.PluginAdMob.isAvailable("home");
sdkbox.PluginAdMob.isAvailable("gameover");
```

### Implement AdMobListner
* You can implement AdMobListener if you want to receive callbacks like video finish playing.
```javascript

sdkbox.PluginAdMob.setListener({
    adViewDidReceiveAd : function(name) { },
    adViewDidFailToReceiveAdWithError : function(name, msg) { },
    adViewWillPresentScreen : function(name) { },
    adViewDidDismissScreen : function(name) { },
    adViewWillDismissScreen : function(name) { },
    adViewWillLeaveApplication : function(name) { }
});

```
