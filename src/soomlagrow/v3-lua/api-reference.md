## API Reference

### Methods
```lua
sdkbox.PluginSoomlaGrow:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginSoomlaGrow:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginSoomlaGrow:refreshInsight()
```
>  Refreshed SoomlaInsights information from the server

```lua
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```
>  get user insight info
>  Note: the return may be empty


### Listeners
```lua
onHighWayInitialized()
```

>  The delegate named onHighWayInitialized is triggerred once the highway initialized.

```lua
onHighWayConnected()
```

>  The delegate named onHighWayConnected is triggerred once the highway connected to server success.

```lua
onHighWayDisconnected()
```

>  The delegate named onHighWayDisconnected is triggerred once the highway disconnect to server.

