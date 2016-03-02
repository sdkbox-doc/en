## API Reference

### Methods
```lua
sdkbox.PluginLeadBolt:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginLeadBolt:setListener(listener)
```
> Set listener to listen for leadbolt events

```lua
sdkbox.PluginLeadBolt:loadModuleToCache(placement, userData)
```
> Cache Ad with name @placement (referenced from your json config file)

```lua
sdkbox.PluginLeadBolt:isAdReady(placement)
```
> Check if Ad with name @placement (referenced from your json config file) is available for display

```lua
sdkbox.PluginLeadBolt:loadModule(placement, userData)
```
> Load/Display Ad with name @placement (referenced from your json config file)

```lua
sdkbox.PluginLeadBolt:setAgeRange(range)
sdkbox.PluginLeadBolt:setGender(gender)
```
>You can increase your App’s performance by optionally including the additional information above. This allows selected premium advertisers to display their Ads to your users. To pass this additional information, use the following methods BEFORE calling loadModuleToCache.

>Allowed values:

>- for age range are: "13-17", "18-25", "26-35", "36-45", "46+"

>- for gender are: "Male", "Female"

### Listeners
```lua
onModuleLoaded(placement)
```
> Notifies the delegate that the module has finished loading

```lua
onModuleClosed(placement)
```
> Notifies the delegate that the module has closed

```lua
onModuleClicked(placement)
```
> Notifies the delegate that the module has clicked

```lua
onModuleCached(placement)
```
> Notifies the delegate that the module has cached

```lua
onModuleFailed(placement, error, iscached)
```
> Notifies the delegate that the module has fail

```lua
onMediaFinished(viewCompleted)
```
> Notifies the delegate that the rewarded video has finished playing.
