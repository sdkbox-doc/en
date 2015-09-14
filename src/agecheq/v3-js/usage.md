### Register Javascript Functions
You need to register all the AgeCheq JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAgeCheqJS.hpp"
#include "PluginAgeCheqJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginAgeCheqJS);
sc->addRegisterCallback(register_PluginAgeCheqJS_helper);
```

### Initialize AgeCheq
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginAgeCheq.init();
```

### Using AgeCheq
After initialization you can begin to use the AgeCheq functionality. Use `check` wherever you want from your code:
```cpp
sdkbox.PluginAgeCheq.check("agecheqPin");
```

### Catch AgeCheq events (optional)
This allows you to catch the `AgeCheq` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
sdkbox.PluginAgeCheq.init();
sdkbox.PluginAgeCheq.setListener({
    checkResponse : function (rtn, rtnmsg, apiversion, checktype, appauthorized, appblocked, parentverified, under13, under18, underdevage, trials) {
        cc.log("checkResponse rtn:" + rtn + " rtnmsg:" + rtnmsg
            + " apiversion:" + apiversion + " checktype:" + checktype
            + " appauthorized:" + appauthorized + " appblocked:" + appblocked
            + " parentverified:" + parentverified + " under13:" + under13
            + " under18:" + under18 + " underdevage:" + underdevage + " trials:" + trials);
    },
    associateDataResponse : function (rtn, rtnmsg) {
        cc.log("associateDataResponse rtn:" + rtn + " rtnmsg:" + rtnmsg);
    }
})
sdkbox.PluginAgeCheq.check("agecheqPin");
```
