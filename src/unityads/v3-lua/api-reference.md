## API Reference

### Methods
```lua
sdkbox.PluginUnityAds:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginUnityAds:setListener(listener)
```
> Set listener to listen for unityads events

```lua
sdkbox.PluginUnityAds:isSupported();
```
> is unityads support current platform

```lua
sdkbox.PluginUnityAds:isReady(placementId);
```
> is unityads ready to show

```lua
sdkbox.PluginUnityAds:show(placementId);
```
> show unityads

```lua
sdkbox.PluginUnityAds:getPlacementState(placementId);
```
> unityads placement state


### Listeners
```lua
unityAdsDidClick(const std::string& placementId);
```
> unityads clicked

```lua
unityAdsPlacementStateChanged(placementId, oldState, newState);
```
> unityads placement state changed

```lua
unityAdsReady(placementId);
```
> unityads ready

```lua
unityAdsDidError(error, message);
```
> unityads error

```lua
unityAdsDidStart(placementId);
```
> unityads start

```lua
unityAdsDidFinish(placementId, state);
```
> unityads finish

