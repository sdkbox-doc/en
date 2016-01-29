### Register Javascript Functions
You need to register all the Share JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginShareJS.hpp"
#include "PluginShareJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginShareJS);
sc->addRegisterCallback(register_all_PluginShareJS_helper);
```

### Initialize Share
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginShare.init();
```

### share
After initialization you can begin to use the Share functionality. Use `share` wherever you want from your code:
```javascript
sdkbox.PluginShare.share({text: "#sdkbox(www.sdkbox.com) - the cure for sdk fatigue"})
```

### Catch Share events (optional)
This allows you to catch the `Share` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginShare
plugin.setListener({
    onShareState: function(response) {
        cc.log("onSharestate:" + response.state + " error:" + response.error)
        if (response.state == sdkbox.PluginShare.ShareState.ShareStateSuccess) {
            cc.log("post success")
        }
    }
})
plugin.init();
```
