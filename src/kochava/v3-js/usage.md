### Initialize Kochava
* Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginKochava.init();
```

* modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginKochavaJS.hpp"
```

* modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginKochavaJS);
```
This registers the Javascript callbacks.

### Tracking Events
Kochava provides tracking __custom__, __spatial__ or __referral__ events.

* Tracking a __custom__ event:
```javascript
sdkbox.PluginKochava.trackEvent("<EVENT>", "<VALUE>");
```

* Tracking a __spatial__ event, by providing a title and position in the world:
```javascript
sdkbox.PluginKochava.spatialEvent("<TITLE>", <X>, <Y>, <Z>);
```

* Tracking a __referral__ event (also known as a deep link):
```javascript
sdkbox.PluginKochava.sendDeepLink("<URI>", "<YOUR APP>");
```
 __Note:__ On Android, the 2nd parameter (__<YOUR APP>__) is not used. You just need to pass the __<URI>__.
