### Initialize Misc
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginMisc:init()
```

### send local notification
```lua
-- will receive notification after 10 second
local nid = sdkbox.PluginMisc:localNotify("test title", "this a test notify content", 1000 * 10);
cc.log('Local Notification ID:' .. nid);
```

### Implement MiscListner
* You can implement MiscListener if you want to receive callbacks like video finish playing.
```lua

sdkbox.PluginMisc.setListener(function(data)
    local event = args.event
    if "onHandleLocalNotify" == event then
    else
        cc.log('unknow event');
    end
end)

```
