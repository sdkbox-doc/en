### Modify Lua Code
* modify `Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginTuneLua.hpp"
#include "PluginTuneLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginTuneLua(<lua_State*>);`.

  __Note:__ It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`.

	Here is an example of what this might look like for you:
```cpp
#include "PluginTuneLua.hpp"
#include "PluginTuneLuaHelper.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginTuneLua(tolua_s);
	register_all_PluginTuneLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### Initialize Tune
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```cpp
sdkbox.PluginTune:init()
```

### Using Tune
After initialization you can begin to use the Tune functionality. Tune uses a concept of __events__ (also known as __MAT Native Event Types__). You log __events__ that you care about and you can later view them using the web-based report viewer. Tune provides a structure for these events in their documentation. Example:
```lua
sdkbox.PluginTune:measureEventName("login");
sdkbox.PluginTune:measureEventId(0123456789);
local event = {}
event.eventName = "purchase"
event.refId = "RJ1357"
event.searchString = "sweet srisp red apples"
event.attribute1 = "srisp"
event.attribute2 = "red"
event.quantity = 3
sdkbox.PluginTune:measureEventForScript(json.encode(event))
```

### Catch Tune events (optional)
This allows you to catch the `Tune` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginTune:setListener(function(eventName, eventData)
       print(eventName, eventData)
   end)
```
