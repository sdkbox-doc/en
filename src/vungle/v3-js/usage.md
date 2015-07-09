### Initialize Vungle
* call `sdkbox.PluginVungle.init();` where appropriate in your code. We recommend to do this in the `app.js`

* modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginVungleJS.hpp"
#include "PluginVungleJSHelper.h"
```

* modify `AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginVungleJS);
sc->addRegisterCallback(register_PluginVungelJs_helper);
```
This registers the Javascript callbacks.

### Showing Ads
Display an ad where ever you want from your code, either __video__ or __reward__:
```javascript
sdkbox.PluginVungle.show("video");
sdkbox.PluginVungle.show("reward");
```

### Catch Vungle events (optional)
This allows you to catch the `Vungle` events so that you can perform operations such as providing player rewards for watching the video.

* Create a listener (demonstrated by logging events):
```javascript
sdkbox.PluginVungle.setListener({
    onVungleCacheAvailable : function() { cc.log("onVungleCacheAvailable") },
    onVungleStarted : function() { cc.log("onVungleStarted") },
    onVungleFinished : function() { cc.log("onVungleFinished") },
    onVungleAdViewed : function(isComplete) { cc.log("onVungleAdViewed" + isComplete) }
})
```
