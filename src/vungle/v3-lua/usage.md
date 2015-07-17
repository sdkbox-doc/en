### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Vungle` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginVungleLua.hpp"
#include "PluginVungleLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginVungleLua(L);
  register_PluginVungleLua_helper(L);
}
```

### Initialize Vungle
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginVungle:init()
```

### Showing Ads
Display an ad where ever you want from your code, either __video__ or __reward__:
```lua
sdkbox.PluginVungle:show("video")
sdkbox.PluginVungle:show("reward")
```

### Catch Vungle events (optional)
This allows you to catch the `Vungle` events so that you can perform operations such as providing player rewards for watching the video.

* Create a listener (demonstrated by logging events):
```lua
sdkbox.PluginVungle:setListener(function(name, isComplete)
    if "onVungleCacheAvailable" == name then
        print("onVungleCacheAvailable")
    elseif "onVungleStarted" ==  name then
        print("onVungleStarted")
    elseif "onVungleFinished" ==  name then
        print("onVungleFinished")
    elseif "onVungleAdViewed" ==  name then
        print("onVungleAdViewed:", isComplete)
    end
end)
```
