### Modify `AppDelegate.cpp`
* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginGoogleAnalyticsLua.hpp"
#include "PLuginGoogleAnalyticsLuaHelper.hpp"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginGoogleAnalyticsLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```lua
lua_State* tolua_s = pStack->getLuaState();
register_all_PluginGoogleAnalyticsLua(tolua_s);
register_all_PluginGoogleAnalyticsLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

### Initialize Google Analytics
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginGoogleAnalytics:init();
```
