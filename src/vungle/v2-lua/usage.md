### Modify `AppDelegate.cpp`
* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginVungleLua.hpp"
#include "PluginVungleLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginVungleLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```lua
lua_State* tolua_s = pStack->getLuaState();
register_all_PluginVungleLua(tolua_s);
register_all_PluginVungleLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

### Initialize Vungle
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginVungle:init();
```

### Showing Ads
Display an ad where ever you want from your code, either __video__ or __reward__:
```lua
sdkbox.PluginVungle:show("video");
sdkbox.PluginVungle:show("reward");
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
