### Register Javascript Functions
You need to register all the LeadBolt JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginLeadBoltJS.hpp"
#include "PluginLeadBoltJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginLeadBoltJS);
sc->addRegisterCallback(register_all_PluginLeadBoltJS_helper);
```

### Initialize LeadBolt
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginLeadBolt.init();
```

### leadbolt
After initialization you can begin to use the LeadBolt functionality. Use `leadbolt` wherever you want from your code:
```javascript
if (sdkbox.PluginLeadBolt.isAdReady("adname")) {
    sdkbox.PluginLeadBolt.loadModule("adname");
} else {
    console.log("ad is not ready")
}
```

### Catch LeadBolt events (optional)
This allows you to catch the `LeadBolt` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginLeadBolt
plugin.setListener({
  onModuleLoaded: function(placement) {
    console.log("onModuleLoaded:" + placement)
  },
  onModuleClosed: function(placement) {
    console.log("onModuleClosed:" + placement)
  },
  onModuleClicked: function(placement) {
    console.log("onModuleClicked:" + placement)
  },
  onModuleCached: function(placement) {
    console.log("onModuleCached:" + placement)
  },
  onModuleFailed: function(placement, error, cached) {
    console.log("onModuleFailed:" + placement + " error:" + error + " cached:" + cached)
  },
  onMediaFinished: function(viewCompleted) {
    console.log("onMediaFinished:" + viewCompleted)
  }
})
plugin.init();
```
