## API Reference

### Methods
```lua
sdkbox.PluginSoomlaGrow:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginSoomlaGrow:setListener(listener)
```
> Set listener to listen for GROW events

```lua
sdkbox.PluginSoomlaGrow:refreshInsight()
```
>  Refreshed Insights information from the server

```lua
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```
>  get user insight info
>  Note: the returned value may be empty


### Listeners
```lua
onHighWayInitialized()
```

>  This event is triggered once the highway initialized.

```lua
onHighWayConnected()
```

>  This event is triggered once the highway is connected to server.

```lua
onHighWayDisconnected()
```

>  This event is triggered once the highway disconnect from the server.
