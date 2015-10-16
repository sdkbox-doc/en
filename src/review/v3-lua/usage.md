### Initialize Review
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginReview:init()
```

### Setting Review (optional)
You can set a custom string for the rate prompt, if you don't want to use the default string.

`Note:` if you set `tryPromptWhenInit` to __true__ which is in `sdkbox.config`, you must call the following functions before `init()`:
```lua
sdkbox.PluginReview:setCustomPromptTitle("custom title");
sdkbox.PluginReview:setCustomPromptMessage("custom message");
sdkbox.PluginReview:setCustomPromptCancelButtonTitle("custom cancel");
sdkbox.PluginReview:setCustomPromptRateButtonTitle("custom rate");
sdkbox.PluginReview:setCustomPromptRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `show` try to display rate prompt:
```lua
sdkbox.PluginReview:show();
```

If you set `UserEventLimit` not 0 in `sdkbox.config`, you must call `userDidSignificantEvent` increase user event count: `userDidSignificantEvent` increase user event count
```lua
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
