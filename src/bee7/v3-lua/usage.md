### Initialize Bee7
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginBee7:init();
```

### Using Bee7
#### Show Game Wall
```lua
sdkbox.PluginBee7:showGameWall()
```

### Bee7 events
This allows you to catch `Bee7` events so that you can perform operations after Bee7 events have occurred.

```lua
sdkbox.PluginBee7:setListener(function(args)
    dump(args)
    if args.name == "onAvailableChange" then
    elseif args.name == "onVisibleChange" then
    elseif args.name == "onGameWallWillClose" then
    elseif args.name == "onGiveReward" then
    end
end)
```
