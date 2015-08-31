### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `AdColony` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginAdColonyLua.hpp"
#include "PluginAdColonyLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginAdColonyLua(L);
  register_all_PluginAdColonyLua_helper(L);
}
```

### Initialize AdColony
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAdColony:init()
```

### Showing Ads
Display an ad wherever you want from your code, by specifying ad type:
```lua
sdkbox.PluginAdColony:show("video")
```
or:
```lua
sdkbox.PluginAdColony:show("v4vc")
```

### Catch AdColony events (optional)
This allows you to catch the `AdColony` events so that you can perform operations such as providing player rewards for watching the video.

* Create a listener (demonstrated by logging events):
```lua
sdkbox.PluginAdColony:setListener(function(args)
    if "onAdColonyChange" == args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
        local available = args.available -- boolean
				dump(info, "onAdColonyChange:")
        print("available:", available)
    elseif "onAdColonyReward" ==  args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
        local currencyName = args.currencyName -- string
        local amount = args.amount -- int
        local success = args.success -- boolean
				dump(info, "onAdColonyReward:")
        print("currencyName:", currencyName)
        print("amount:", amount)
        print("success:", success)
    elseif "onAdColonyStarted" ==  args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
				dump(info, "onAdColonyStarted:")
    elseif "onAdColonyFinished" ==  args.name then
        local info = args.info  -- sdkbox::AdColonyAdInfo
				dump(info, "onAdColonyFinished:")
    end
end)
```
