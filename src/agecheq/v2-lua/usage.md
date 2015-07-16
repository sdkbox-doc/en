### Modify Lua Code
* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginAgeCheqLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```cpp
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginAgeCheqLua(tolua_s);
register_PluginAgeCheqLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

* Modify to include the following headers:
```cpp
#include "PluginAgeCheqLua.hpp"
#include "PluginAgeCheqLuaHelper.h"
```

### Initialize AgeCheq
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAgeCheq:init()
```

### Using AgeCheq
After initialization you can begin to use the AgeCheq functionality. Use `check` wherever you want from your code:
```lua
sdkbox.PluginAgeCheq:check("agecheqPin")
```

### Catch AgeCheq events (optional)
This allows you to catch the `AgeCheq` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginAgeCheq:init()
sdkbox.PluginAgeCheq:setListener(function(data)
	    if "checkResponse" == data.event then
	        dump(data)
	    elseif "associateDataResponse" == data.event then
	        dump(data)
	    end
	end)
sdkbox.PluginAgeCheq:check("agecheqPin")
```
