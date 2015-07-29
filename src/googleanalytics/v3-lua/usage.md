### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `GoogleAnalytics` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginGoogleAnalyticsLua.hpp"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginGoogleAnalyticsLua(L);
}
```

### Initialize Google Analytics
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginGoogleAnalytics:init()
```

You can always manually stop recording events at any time by calling:
```lua
sdkbox.PluginGoogleAnalytics:stopSession();
```

However, in-order to record events again you must then manually call:
```lua
sdkbox.PluginGoogleAnalytics:startSession();
```

Logged data usually shows up within one day.
