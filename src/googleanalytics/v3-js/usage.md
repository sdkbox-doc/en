### Register Javascript Functions
You need to register all the Google Analytics JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginGoogleAnalyticsJS.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginGoogleAnalyticsJS);
```

### Initialize Google Analytics
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginGoogleAnalytics.init();
```

You can always manually stop recording events at any time by calling:
```javascript
sdkbox.PluginGoogleAnalytics.stopSession();
```

However, in-order to record events again you must then manually call:
```javascript
sdkbox.PluginGoogleAnalytics.startSession();
```

Logged data usually shows up within one day.
