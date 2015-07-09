### Modify Lua Code
Modify `lua_module_register.h` to include the necessary headers and calls to register `GoogleAnalytics` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginGoogleAnalyticsLua.hpp"
#include "PluginGoogleAnalyticsLuaHelper.h"
```
```cpp
register_all_PluginGoogleAnalyticsLua(L);
register_PluginGoogleAnalyticsLua_helper(L);
```

### Initialize Google Analytics
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginGoogleAnalytics:init();
```
