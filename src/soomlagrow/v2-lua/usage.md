### Modify Lua Code
* Modify `Classes/AppDelegate.cpp`to include the following headers:
```cpp
#include "PluginSoomlaGrowLua.hpp"
#include "PluginSoomlaGrowLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginSoomlaGrowLua(<lua_State*>);`.

  __Note:__ It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`.

	Here is an example of what this might look like for you:
```cpp
#include "PluginSoomlaGrowLua.hpp"
#include "PluginSoomlaGrowLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginSoomlaGrowLua(tolua_s);
	register_PluginSoomlaGrowLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### Initialize SoomlaGrow
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSoomlaGrow:init()
```

### Using SoomlaGrow user insight module
After initialization you can begin to use the SoomlaGrow functionality. Use `refreshInsight`, 'getUserInsightInfo' wherever you want from your code:
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
