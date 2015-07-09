### Modify `AppDelegate.cpp`
* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginKochavaLua.hpp"
#include "PluginKochavaLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginKochavaLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```cpp
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginKochavaLua(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

### Initialize Kochava
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginKochava:init();
```

### Tracking Events
Kochava provides tracking __custom__, __spatial__ or __referral__ events.

* Tracking a __custom__ event:
```lua
sdkbox.PluginKochava:trackEvent("<EVENT>", "<VALUE>");
```

* Tracking a __spatial__ event, by providing a title and position in the world:
```lua
sdkbox.PluginKochava:spatialEvent("<TITLE>", <X>, <Y>, <Z>);
```

* Tracking a __referral__ event (also known as a deep link):
```lua
sdkbox.PluginKochava:sendDeepLink("<URI>", "<YOUR APP>");
```
 __Note:__ On Android, the 2nd parameter (__<YOUR APP>__) is not used. You just need to pass the __<URI>__.
