## API Reference

### Methods
```lua
sdkbox.PluginPhunwareMessaging:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginPhunwareMessaging:setListener(listener)
```
> Set listener to listen for phunwaremessaging events

```lua
sdkbox.PluginPhunwareMessaging:read(messageID)
```

```lua
sdkbox.PluginPhunwareMessaging:remove(messageID)
```

```lua
sdkbox.PluginPhunwareMessaging:messages()
```

```lua
sdkbox.PluginPhunwareMessaging:deviceId()
```

```lua
sdkbox.PluginPhunwareMessaging:serviceName()
```

```lua
sdkbox.PluginPhunwareMessaging:version()
```


### Listeners
```lua
init(success, message)
```
> Notifies the delegate that the module has finished loading

```lua
error(message)
```


