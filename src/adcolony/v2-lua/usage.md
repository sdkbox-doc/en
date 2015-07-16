### Modify `AppDelegate.cpp`
* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAdColonyLua.hpp"
#include "PluginAdColonyLuaHelper.hpp"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginAdColonyLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```lua
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginAdColonyLua(tolua_s);
register_all_PluginAdColonyLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
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
