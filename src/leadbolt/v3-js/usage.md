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

### Cache Ad
>Note: Leadbolt ads are cached before use for better user experience. Please allow time for ads to be cached.  Once an ad is cached, you will be able to see the ad. While caching is in progress, ads are not available for display.
```javascript
sdkbox.PluginLeadbolt.loadModuleToCache("directdeal");
sdkbox.PluginLeadbolt.loadModuleToCache("rewardedvideo");
```

### Load/Display Ad
```javascript
sdkbox.PluginLeadbolt.loadModule("directdeal");
sdkbox.PluginLeadbolt.loadModule("rewardedvideo");
```

### Check if Ad is available
```javascript
sdkbox.PluginLeadbolt.isAdReady("directdeal");
sdkbox.PluginLeadbolt.isAdReady("rewardedvideo");
```

### Catch LeadBolt events (optional)
This allows you to catch the `LeadBolt` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginLeadBolt
plugin.setListener({
  onModuleLoaded: function(placement) {},
  onModuleClosed: function(placement) {},
  onModuleClicked: function(placement) {},
  onModuleCached: function(placement) {},
  onModuleFailed: function(placement, error, cached) {},
  onMediaFinished: function(viewCompleted) {}
})
plugin.init();
```
