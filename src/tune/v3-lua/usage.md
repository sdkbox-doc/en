### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Tune` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginTuneLua.hpp"
#include "PluginTuneLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginTuneLua(L);
  register_PluginTuneLua_helper(L);
}
```

### Initialize Tune
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```cpp
sdkbox.PluginTune:init()
```

### Using Tune
After initialization you can begin to use the Tune functionality. Tune uses a concept of __events__ (also known as __MAT Native Event Types__). You log __events__ that you care about and you can later view them using the web-based report viewer. Tune provides a structure for these events in their documentation. Example:
```lua
sdkbox.PluginTune:measureEventName("login")
sdkbox.PluginTune:measureEventId(0123456789)

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
sdkbox.PluginTune:setListener(function(eventName, eventData, timeout)
        -- the third param "timeout" valid, when eventName equal "onReceiveDeeplink"
        print(eventName, eventData)
    end)
```
