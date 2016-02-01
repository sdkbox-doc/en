### Initialize Share
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginShare:init()
```

### share
After initialization you can begin to use the Share functionality:
```lua
sdkbox.PluginShare:share({text="#sdkbox the end of sdk figue (www.sdkbox.com)"})
```

### Catch Share events (optional)
This allows you to catch the `Share` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginShare
plugin:setListener(function(responsed)
    dump(responsed, "share listener info:")
end)
plugin:init()
```
