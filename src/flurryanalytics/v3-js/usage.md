### Register Javascript Functions
You need to register all the Facebook JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFlurryAnalyticsJS.hpp"
#include "PluginFlurryAnalyticsJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginFlurryAnalyticsJS);
sc->addRegisterCallback(register_PluginFlurryAnalyticsJs_helper);
```

### Initialize Flurry Analytics
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginFlurryAnalytics.init();
```

### Using Flurry Analytics
After initialization you can begin to use the Flurry Analytics functionality. Use `logevent` where ever you want from your code:
```javascript
sdkbox.PluginFlurryAnalytics.logEvent("test event2 js", JSON.stringify({"eKey1":"eVal1", "eKey2":"eVal2"}));
```

### Catch Flurry Analytics events (optional)
This allows you to catch the `FlurryAnalytics` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
sdkbox.PluginFlurryAnalytics.init();
sdkbox.PluginFlurryAnalytics.setListener({
    flurrySessionDidCreateWithInfo:function(info) {
        var jsonInfo = JSON.parse(info)
        console.log("session started")
        console.log("APIKey :" + jsonInfo.apiKey + " session id :" + jsonInfo.sessionId);
        sdkbox.PluginFlurryAnalytics.logEvent("test event2 js", JSON.stringify({"eKey1":"eVal1", "eKey2":"eVal2"}));
    }
});
sdkbox.PluginFlurryAnalytics.startSession();
```

### Ending Flurry Analytics (Android only)
When you are finished using `FlurryAnalytics` or when your games ends. It is necessary to end the `FlurryAnalytics` session. This is a requirement for Android but optional on iOS. Example:
```javascript
// end session just valid on android, but it's ok to invoke it on iOS
sdkbox.PluginFlurryAnalytics.endSession();
```
