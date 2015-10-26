### Initialize Appodeal
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAppodeal:init()
```

### Using Appodeal
After initialization you can begin to use the Appodeal functionality:
```lua
local plugin = sdkbox.PluginAppodeal
plugin:init()
plugin:setUserVkId("user id");
plugin:cacheAd(15);
```

### Catch Appodeal events (optional)
This allows you to catch the `Appodeal` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginAppodeal
plugin:setListener(function(args)
    local event = args.event
    dump(args, "appodeal listener info:")
end)
plugin:init()
```
