### Modify Lua Code
* modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFlurryAnalyticsLua.hpp"
#include "PluginFlurryAnalyticsLuaHelper.h"
```

* We need to register the plugin with Lua. This is done by making a call to `register_all_PluginFlurryAnalyticsLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```lua
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginFlurryAnalyticsLua(tolua_s);
register_PluginFlurryAnalyticsLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

### Initialize Flurry Analytics
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFlurryAnalytics:init();
```

### Using Flurry Analytics
After initialization you can begin to use the Flurry Analytics functionality. Use `logevent` where ever you want from your code:
```lua
local eventName = "test event1"
sdkbox.PluginFlurryAnalytics:logEvent(eventName);
```

### Catch Flurry Analytics events (optional)
This allows you to catch the `FlurryAnalytics` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginFlurryAnalytics:init()
sdkbox.PluginFlurryAnalytics:setListener(function(data)
        local ret = json.decode(data)
        print("apiKey:", ret.apiKey, "sessionId:", ret.sessionId)
        -- check session state
        print("Flurry analytics session exist: ", f:activeSessionExists())
        print("Flurry analytics session: ", f:getSessionID())
        local eventName = "test event1"
        sdkbox.PluginFlurryAnalytics:logEvent(eventName);
    end)
sdkbox.PluginFlurryAnalytics:startSession()
```

### Ending Flurry Analytics (Android only)
When you are finished using `FlurryAnalytics` or when your games ends. It is necessary to end the `FlurryAnalytics` session. This is a requirement for Android but optional on iOS. Example:
```cpp
// end session just valid on android, but it's ok to invoke it on iOS
sdkbox.PluginFlurryAnalytics:endSession();
```
