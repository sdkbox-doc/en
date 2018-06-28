## API Reference

### Methods
```lua
sdkbox.PluginUnityAds:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginUnityAds:setListener(listener)
```
> Set listener to listen for inmobi events

```lua
sdkbox.PluginUnityAds:isSupported()
```

```lua
sdkbox.PluginUnityAds:isReady(placementId)
```

```lua
sdkbox.PluginUnityAds:show(placementId)
```

```lua
sdkbox.PluginUnityAds:getPlacementState(placementId)
```

```lua
sdkbox.PluginUnityAds:setGDPR(enabled)
```
> Enable GDPR

```lua
sdkbox.PluginUnityAds:setServerId(sid)
```


### Listeners
```lua
unityAdsDidClick(placementId)
```

```lua
unityAdsPlacementStateChanged(placementId, oldState, newState)
```

```lua
unityAdsReady(placementId)
```

```lua
unityAdsDidError(error, message)
```

```lua
unityAdsDidStart(placementId)
```

```lua
unityAdsDidFinish(placementId, state)
```


