### Register Javascript Functions
You need to register all the Firebase JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFirebaseJS.hpp"
#include "PluginFirebaseJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
    sc->addRegisterCallback(register_all_PluginFirebaseJS);
    sc->addRegisterCallback(register_all_PluginFirebaseJS_helper);
```

### Initialize Firebase
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.firebase.Analytics.init();
```

### Log event
You can log game event

```javascript
const evt = {}
evt[sdkbox.firebase.Analytics.Param.kFIRParameterItemID] = 'id123456';
evt[sdkbox.firebase.Analytics.Param.kFIRParameterItemName] = 'name123456';
evt[sdkbox.firebase.Analytics.Param.kFIRParameterItemCategory] = 'category123456';
evt[sdkbox.firebase.Analytics.Param.kFIRParameterPrice] = '123.4';
sdkbox.firebase.Analytics.logEvent(sdkbox.firebase.Analytics.Event.kFIREventViewItem, evt);
```
