## API Reference

### Methods
```lua
sdkbox.PluginShare:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginShare:setListener(listener)
```
> Set listener to listen for share events

```lua
sdkbox.PluginShare:getListener();
```
> Get the listener

```lua
sdkbox.PluginShare:removeListener();
```
> Remove the listener, and can't listen to events anymore

```lua
sdkbox.PluginShare:share(info);
```
> Share content, e.g. {text= "share string"}

### Listeners
```lua
onShareState(response)
```
> Notifies the delegate that share completion


