### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Valuepotion` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginValuePotionLua.hpp"
#include "PluginValuePotionLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginValuePotionLua(L);
  register_all_PluginValuePotionLua_helper(L);
}
```

### Initialize Valuepotion
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginValuePotion:init()
```

### Using Valuepotion
After initialization you can begin to use the Valuepotion functionality. Use `check` wherever you want from your code:
```lua
sdkbox.PluginValuePotion:init()
sdkbox.PluginValuePotion:setTest(true)
if not sdkbox.PluginValuePotion:hasCachedInterstitial("default") then
    sdkbox.PluginValuePotion:cacheInterstitial("default")
end

sdkbox.PluginValuePotion:trackEvent("test event")
sdkbox.PluginValuePotion:trackEvent("test event with value 23", 23)
sdkbox.PluginValuePotion:trackEvent("category", "event name", "label", 45)

sdkbox.PluginValuePotion:trackPurchaseEvent("test event", 56, "RMB", "order id", "product id")
sdkbox.PluginValuePotion:trackPurchaseEvent("test event", 67, "USD", "order id", "product id", "campaign id", "content id")
sdkbox.PluginValuePotion:trackPurchaseEvent("categroy", "event name", "label", 78, "ILY", "order id", "product id", "campaign id", "content id");

sdkbox.PluginValuePotion:userinfo("id", "user id")
sdkbox.PluginValuePotion:userinfo("serverid", "server id")
sdkbox.PluginValuePotion:userinfo("birth", "19991111") -- YYYYMMDD
sdkbox.PluginValuePotion:userinfo("gender", "M")
sdkbox.PluginValuePotion:userinfo("level", "9")
sdkbox.PluginValuePotion:userinfo("friends", "3")
sdkbox.PluginValuePotion:userinfo("accounttype", "facebook")
```

### Catch Valuepotion events (optional)
This allows you to catch the `Valuepotion` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginValuePotion:init()
sdkbox.PluginValuePotion:setListener(function(data)
        local event = args.event
        print("receive event:", event)
        dump(args, "value potion listener info:")
    end)
```
