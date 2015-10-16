### Modify Lua Code
* Modify `Classes/AppDelegate.cpp`to include the following headers:
```cpp
#include "PluginValuePotionLua.hpp"
#include "PluginValuePotionLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginValuePotionLua(<lua_State*>);`.

  __Note:__ It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`.

	Here is an example of what this might look like for you:
```cpp
#include "PluginValuePotionLua.hpp"
#include "PluginValuePotionLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginValuePotionLua(tolua_s);
	register_all_PluginValuePotionLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### Initialize ValuePotion
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
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
sdkbox.PluginValuePotion:userinfo("firends", "3")
sdkbox.PluginValuePotion:userinfo("accounttype", "facebook")
```

### Using ValuePotion
After initialization you can begin to use the ValuePotion functionality. Use `check` wherever you want from your code:
```lua
sdkbox.PluginValuePotion:check("valuepotionPin")
```

### Catch ValuePotion events (optional)
This allows you to catch the `ValuePotion` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginValuePotion:init()
sdkbox.PluginValuePotion:setListener(function(data)
		local event = args.event
		print("receive event:", event)
        dump(args, "value potion listener info:")
	end)
```
