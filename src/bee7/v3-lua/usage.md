### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Bee7` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginBee7Lua.hpp"
#include "PluginBee7LuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginBee7Lua(L);
  register_all_PluginBee7Lua_helper(L);
}
```

### Initialize Bee7
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginBee7:init();
```

### Using Bee7
#### Show Game Wall
```lua
sdkbox.PluginBee7:showGameWall()
```

### Bee7 events
This allows you to catch `Bee7` events so that you can perform operations after Bee7 events have occurred.

```lua
sdkbox.PluginBee7:setListener(function(args)
    dump(args)
    if args.name == "onAvailableChange" then
    elseif args.name == "onVisibleChange" then
    elseif args.name == "onGameWallWillClose" then
    elseif args.name == "onGiveReward" then
    end
end)
```
