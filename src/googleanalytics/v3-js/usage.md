### Initialize Google Analytics
* Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginGoogleAnalytics.init();
```

* modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginGoogleAnalyticsJS.hpp"
```

* Modify `AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginGoogleAnalyticsJS);
```
This registers the Javascript callbacks.
