### Initialize PhunwareMessaging
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginPhunwareMessaging:init()
```

### Read message
```lua
// To use customized location
sdkbox.PluginPhunwareMessaging:read("123")
```

### Remove message
```lua
sdkbox.PluginPhunwareMessaging:remove("123")
```

### Get all messages
```lua
sdkbox.PluginPhunwareMessaging:messages()
```

### Catch PhunwareMessaging events (optional)
This allows you to catch the `PhunwareMessaging` events so that you can perform operations such as providing player rewards for viewing ads.

* Create a listener (demonstrated by logging events):
```lua
sdkbox.PluginPhunwareMessaging:setListener(function(args)

    if "init" = args.event then
        print(args.event, args.success, args.message)
    elseif "error" = args.event then
        print(args.event, args.message)
    end

end)
```
