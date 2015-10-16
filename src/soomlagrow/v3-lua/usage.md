### Initialize SoomlaGrow
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSoomlaGrow:init()
```

### Using GROW's Insights module
After initialization you can begin to use the Insights functionality. Use `refreshInsight`, `getUserInsightInfo` wherever you want from your code:
```lua
sdkbox.PluginSoomlaGrow:refreshInsight()
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```

### Catch GROW events (optional)
This allows you to catch the `SOOMLA Grow` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginSoomlaGrow:setListener(function(data)
            if "onHighWayInitialized" == data.event then
                //highway initialized
            elseif "onHighWayConnected" == data.event then
                //highway connected
            elseif "onHighWayDisconnected" == data.event then
                //highway disconnected
            end
        end)
sdkbox.PluginSoomlaGrow:init()
```
