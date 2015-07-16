### Modify `AppDelegate.cpp`
* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginChartboostLua.hpp"
#include "PluginChartboostLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginChartboostLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```lua
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginChartboostLua(tolua_s);
register_PluginChartboostLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

### Initialize Chartboost
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginChartboost:init()
```

### Showing Ads
Display an ad where ever you want from your code:
```lua
// To use the Chartboost predefined locations
sdkbox.PluginChartboost:show("Default")
// To use customized location
sdkbox.PluginChartboost:show("your_ad_name")
```

### Catch Chartboost events (optional)
This allows you to catch the `Chartboost` events so that you can perform operations such as providing player rewards for viewing ads.

* Create a listener (demonstrated by logging events):
```lua
sdkbox.PluginChartboost:setListener(function(args)
    if "onChartboostCached" == args.func then
        local name = args.name -- string
        print("onChartboostCached")
        print("name:", args.name)
    elseif "onChartboostShouldDisplay" == args.func then
        local name = args.name -- string
        print("onChartboostShouldDisplay")
        print("name:", args.name)
    elseif "onChartboostDisplay" == args.func then
        local name = args.name -- string
        print("onChartboostDisplay")
        print("name:", args.name)
    elseif "onChartboostDismiss" == args.func then
        local name = args.name -- string
        print("onChartboostDismiss")
        print("name:", args.name)
    elseif "onChartboostClose" == args.func then
        local name = args.name -- string
        print("onChartboostClose")
        print("name:", args.name)
    elseif "onChartboostClick" == args.func then
        local name = args.name -- string
        print("onChartboostClick")
        print("name:", args.name)
    elseif "onChartboostReward" == args.func then
        local name = args.name -- string
        local reward = args.reward -- int
        print("onChartboostReward")
        print("name:", args.name)
        print("reward:", reward)
    elseif "onChartboostFailedToLoad" == args.func then
        local name = args.name -- string
        local e = args.e -- int
        print("onChartboostFailedToLoad")
        print("name:", args.name)
        print("error:", e)
    elseif "onChartboostFailToRecordClick" == args.func then
        local name = args.name -- string
        local e = args.e -- int
        print("onChartboostFailToRecordClick")
        print("name:", args.name)
        print("error:", e)
    elseif "onChartboostConfirmation" == args.func then
        local name = args.name -- string
        print("onChartboostConfirmation")
    elseif "onChartboostCompleteStore" == args.func then
        local name = args.name -- string
        print("onChartboostCompleteStore")
    end
end)
```
