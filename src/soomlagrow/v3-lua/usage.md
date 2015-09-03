### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `SoomlaGrow` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginSoomlaGrowLua.hpp"
#include "PluginSoomlaGrowLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginSoomlaGrowLua(L);
  register_PluginSoomlaGrowLua_helper(L);
}
```

### Initialize SoomlaGrow
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSoomlaGrow:init()
```

### Using SoomlaGrow user insight module
After initialization you can begin to use the SoomlaGrow functionality. Use `refreshInsight`, `getUserInsightInfo` wherever you want from your code:
```lua
sdkbox.PluginSoomlaGrow:refreshInsight()
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```

### Catch SoomlaGrow events (optional)
This allows you to catch the `SoomlaGrow` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginSoomlaGrow:setListener(function(data)
            if "onHighWayInitialized" == data.event then
                //highway initialized
            elseif "onHighWayConnected" == data.event then
                //highway connected
            elseif "onHighWayDisconnected" == data.event then
                //highway disconnected
            end
        end)
sdkbox.PluginSoomlaGrow:init()
```
