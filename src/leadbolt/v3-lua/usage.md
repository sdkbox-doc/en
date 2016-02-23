### Initialize LeadBolt
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginLeadBolt:init()
```

### leadbolt
After initialization you can begin to use the LeadBolt functionality:
```lua
if plugin:isAdReady('ad1') then
    plugin:loadModule('ad1')
else
    print('leadbolt ad is not ready')
end
```

### Catch LeadBolt events (optional)
This allows you to catch the `LeadBolt` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginLeadBolt
plugin:setListener(function(args)
    local event = args.event
    dump(args, "leadbolt listener info:")
end)
plugin:init()
```
