### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Review` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginReviewLua.hpp"
#include "PluginReviewLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginReviewLua(L);
  register_PluginReviewLua_helper(L);
}
```

### Initialize Review
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginReview:init()
```

### Setting Review (optional)
you can set custom string of rate prompt, if you wan't to use default string

`Note:` if you set `tryPromptWhenInit` ture which in `sdkbox.config`, you must call the fllow function before `init()`
```cpp
sdkbox.PluginReview:setCustomPromptTitle("custom title");
sdkbox.PluginReview:setCustomPromptMessage("custom message");
sdkbox.PluginReview:setCustomPromptCancelButtonTitle("custom cancel");
sdkbox.PluginReview:setCustomPromptRateButtonTitle("custom rate");
sdkbox.PluginReview:setCustomPromptRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `tryToShowPrompt` try to display rate prompt:
```cpp
sdkbox.PluginReview:tryToShowPrompt();
```

Use `forceToShowPrompt` to display rate prompt without checks:
```cpp
sdkbox.PluginReview:forceToShowPrompt();
```

if you set `UserEventLimit` not 0 in `sdkbox.config`, you must call `userDidSignificantEvent` increase user event count
```cpp
sdkbox.PluginReview:userDidSignificantEvent(true);
```

### Catch Review events (optional)
This allows you to catch the `Review` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginReview
plugin:setListener(function(args)
    local event = args.event
    if "didDisplayAlert" == event then
        print("didDisplayAlert")
    elseif "didDeclineToRate" == event then
        print("didDeclineToRate")
    elseif "didToRate" == event then
        print("didToRate")
    elseif "didToRemindLater" == event then
        print("didToRemindLater")
    end
end)
plugin:init()
```
