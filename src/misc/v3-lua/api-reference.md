## API Reference

### Methods
```lua
sdkbox.PluginMisc:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginMisc:setListener(listener)
```
> Set listener to listen for misc events

```lua
sdkbox.PluginMisc:localNotify(title, content, delaymillisecond);
```
> send a local notification
@return notification id


### Listeners
```lua
onHandleLocalNotify (payloadJson);
```
