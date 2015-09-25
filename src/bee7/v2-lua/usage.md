### Modify `AppDelegate.cpp`
* Modify `Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginBee7Lua.hpp"
#include "PluginBee7LuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginBee7Lua(<lua_State*>);`.

  __Note:__ It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`.

	Here is an example of what this might look like for you:
```cpp
#include "PluginBee7Lua.hpp"
#include "PluginBee7LuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginBee7Lua(tolua_s);
	register_all_PluginBee7Lua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### Initialize Bee7
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginBee7:init()
```

### Using Bee7
#### Show Game Wall
```lua
sdkbox.PluginBee7:showOfferWall()
```

Displaying the Offer Wall with custom placementId
```lua
sdkbox.PluginBee7:showGameWall()
```

### Catch Bee7 events (optional)
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
