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
sdkbox.PluginLeadBolt:startSession(apiKey)
```
> start session

```lua
sdkbox.PluginLeadBolt:closeSession()
```
> close session

```lua
sdkbox.PluginLeadBolt:setSyncDataPeriodInSecond(periodInSecond)
```
> sync data second, just valid on ios

```lua
sdkbox.PluginLeadBolt:sync()
```
> sync data

```lua
sdkbox.PluginLeadBolt:event(name)
```

```lua
sdkbox.PluginLeadBolt:event(name, floatValue)
```

```lua
sdkbox.PluginLeadBolt:transaction(name, floatValue, currencyCode)
```

```lua
sdkbox.PluginLeadBolt:transaction(name, floatValue, currencyCode, instant)
```

```lua
sdkbox.PluginLeadBolt:transaction(name, floatValue, currencyCode, ref)
```

```lua
sdkbox.PluginLeadBolt:transaction(name, floatValue, currencyCode, ref, instant)
```

```lua
sdkbox.PluginLeadBolt:loadModule(placement)
```

```lua
sdkbox.PluginLeadBolt:loadModule(placement, userData)
```

```lua
sdkbox.PluginLeadBolt:loadModuleToCache(placement)
```

```lua
sdkbox.PluginLeadBolt:loadModuleToCache(placement, userData)
```

```lua
sdkbox.PluginLeadBolt:destroyModule()
```

```lua
sdkbox.PluginLeadBolt:setCrashHandlerStatus(enable)
```

```lua
sdkbox.PluginLeadBolt:crashWithName(crashName, description)
```

```lua
sdkbox.PluginLeadBolt:fixAdOrientation(orientation)
```

```lua
sdkbox.PluginLeadBolt:isAdReady(placement)
```

```lua
sdkbox.PluginLeadBolt:setAgeRange(range)
```

```lua
sdkbox.PluginLeadBolt:setGender(gender)
```

```lua
sdkbox.PluginLeadBolt:setFramework(f)
```


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
> Notifies the delegate that the module has finished


