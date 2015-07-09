### Initialize Google Analytics
* Call `sdkbox.PluginGoogleAnalytics.init();` where appropriate in your code. We recommend to do this in the `app.js`

* modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginGoogleAnalyticsJS.hpp"
```

* Modify `AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginGoogleAnalyticsJS);
```
This registers the Javascript callbacks.
