### Register Javascript Functions
You need to register all the PhunwareMessaging JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginPhunwareMessagingJS.hpp"
#include "PluginPhunwareMessagingJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginPhunwareMessagingJS);
sc->addRegisterCallback(register_all_PluginPhunwareMessagingJS_helper);
```

### Initialize PhunwareMessaging
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginPhunwareMessaging.init();
```

### Read message
```javascript
sdkbox.PluginPhunwareMessaging.read("123");
```

### Remove message
```javascript
sdkbox.PluginPhunwareMessaging.remove("123")
```

### Get all messages
```javascript
sdkbox.PluginPhunwareMessaging.messages()
```

### Catch PhunwareMessaging events (optional)
This allows you to catch the `PhunwareMessaging` events so that you can perform operations such as providing player rewards for viewing ads.

* Create a listener (demonstrated by logging events):
```javascript
sdkbox.PluginPhunwareMessaging.setListener({
    init : function(success, message) {},
    error : function(message) {},
})
```
