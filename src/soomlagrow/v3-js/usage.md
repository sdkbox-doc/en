### Register Javascript Functions
You need to register all the SoomlaGrow JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginSoomlaGrowJS.hpp"
#include "PluginSoomlaGrowJSHelper.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginSoomlaGrowJS);
sc->addRegisterCallback(register_all_PluginSoomlaGrowJS_helper);
```

### Initialize SoomlaGrow
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginSoomlaGrow.init();
```

### Using SoomlaGrow user insight module
After initialization you can begin to use the SoomlaGrow functionality. Use `refreshInsight`, 'getUserInsightInfo' wherever you want from your code:
```javascript
sdkbox.PluginSoomlaGrow.refreshInsight()
sdkbox.PluginSoomlaGrow.getUserInsightInfo()
```

### Catch SoomlaGrow events (optional)
This allows you to catch the `SoomlaGrow` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
sdkbox.PluginSoomlaGrow.setListener({
            onHighWayInitialized: function(data) {cc.log("onHighWayInitialized")},
            onHighWayConnected: function(data) { cc.log("onHighWayConnected") },
            onHighWayDisconnected: function(data) { cc.log("onHighWayDisconnected") }
            })
sdkbox.PluginSoomlaGrow.init()
```
