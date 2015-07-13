### Initialize Tune
* Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginTune.init();
```

* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginTuneJS.hpp"
#include "PluginTuneJSHelper.hpp"
```

* Modify `AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginTuneJS);
sc->addRegisterCallback(register_PluginTuneJs_helper);
```
This registers the Javascript callbacks.

### Using Tune
After initialization you can begin to use the Tune functionality. Tune uses a concept of __events__ (also known as __MAT Native Event Types__). You log __events__ that you care about and you can later view them using the web-based report viewer. Tune provides a structure for these events in their documentation. Example:
```javascript
sdkbox.PluginTune.measureEventName("login");
sdkbox.PluginTune.measureEventId(0123456789);

var event = {};
event.eventName = "purchase";
event.refId = "RJ1357";
event.searchString = "sweet srisp red apples";
event.attribute1 = "srisp";
event.attribute2 = "red";
event.quantity = 3;
sdkbox.PluginTune.measureEventForScript(JSON.stringify(event));
```

### Catch Tune events (optional)
This allows you to catch the `Tune` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
sdkbox.PluginTune.setListener({
  onEnqueuedAction: function(data) {},
  onSucceed: function(data) {},
  onFailed: function(data) {},
  onReceiveDeeplink: function(data) {}
});
```
