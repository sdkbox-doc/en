### Register Javascript Functions
You need to register all the Bee7 JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginBee7JS.hpp"
#include "PluginBee7JSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginBee7JS);
sc->addRegisterCallback(register_all_PluginBee7JS_helper);
```

### Initialize Bee7
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginBee7.init();
```

### Using Bee7
#### Show Game Wall
```javascript
sdkbox.PluginBee7.showGameWall();
```

### Bee7 events
This allows you to catch `Bee7` events so that you can perform operations after Bee7 events have occurred.

```javascript
sdkbox.PluginBee7.setListener({
	onAvailableChange: function(available) {},
	onVisibleChange: function(available) {},
	onGameWallWillClose: function() {},
	onGiveReward: function(bee7Points, virtualCurrencyAmount, appId, cappedReward,
						   campaignId, videoReward) {}
});
```
