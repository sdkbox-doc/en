### Modify Lua Code
* Modify `Classes/AppDelegate.cpp`to include the following headers:
```cpp
#include "PluginReviewLua.hpp"
#include "PluginReviewLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginReviewLua(<lua_State*>);`.

  __Note:__ It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`.

	Here is an example of what this might look like for you:
```cpp
#include "PluginReviewLua.hpp"
#include "PluginReviewLuaHelper.hpp"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginReviewLua(tolua_s);
	register_all_PluginReviewLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### Initialize Review
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginReview:init()
```

### Setting Review (optional)
You can set a custom string for the rate prompt, if you don't want to use the default string.

`Note:` if you set `tryPromptWhenInit` to __true__ which is in `sdkbox.config`, you must call the following functions before `init()`:
```cpp
sdkbox.PluginReview:setTitle("custom title");
sdkbox.PluginReview:setMessage("custom message");
sdkbox.PluginReview:setCancelButtonTitle("custom cancel");
sdkbox.PluginReview:setRateButtonTitle("custom rate");
sdkbox.PluginReview:setRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `show` try to display rate prompt:
```cpp
sdkbox.PluginReview:show();
```

If you set `UserEventLimit` not 0 in `sdkbox.config`, you must call `userDidSignificantEvent` increase user event count:
```cpp
sdkbox.PluginReview:userDidSignificantEvent(true);
```

### Catch Review events (optional)
This allows you to catch the `Review` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginReview
plugin:setListener(function(args)
    local event = args.event
    if "onDisplayAlert" == event then
        print("didDisplayAlert")
    elseif "onDeclineToRate" == event then
        print("didDeclineToRate")
    elseif "onRate" == event then
        print("didToRate")
    elseif "onRemindLater" == event then
        print("didToRemindLater")
    end
end)
plugin:init()
```
