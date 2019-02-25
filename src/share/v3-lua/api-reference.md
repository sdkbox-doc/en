## API Reference

### Methods
```lua
sdkbox.PluginShare:init(jsonConfig)
```
>  initialize the plugin instance.

```lua
sdkbox.PluginShare:setListener(listener)
```
> Set listener to listen for share events

```lua
sdkbox.PluginShare:setSharePanelTitle(s)
```
> set custome share platform choose panel title, default is "Share to"

```lua
sdkbox.PluginShare:setSharePanelCancel(s)
```
> set custome share platform choose panel cancel button, default is "Cancel"

```lua
sdkbox.PluginShare:logoutTwitter()
```

```lua
sdkbox.PluginShare:setFileProviderAuthorities(authority)
```


### Listeners
```lua
onShareState(response)
```
> Notifies the delegate that share completion


