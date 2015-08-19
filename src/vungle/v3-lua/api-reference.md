## API Reference

### Methods
```lua
sdkbox.PluginVungle:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginVungle:show(name)
```
> show ad with a provided name.

```lua
sdkbox.PluginVungle:setDebug(enable)
```
> enable or disable debug mode.

```lua
sdkbox.PluginVungle:isCacheAvailable()
```
> is there a cached video available.

```lua
sdkbox.PluginVungle:setUserID(userID)
```
> sets the userID for rewarded ads.


### Listeners
```lua
onVungleCacheAvailable()
```
> ad cache is available.

```lua
onVungleStarted()
```
> Vungle is running and available.

```lua
onVungleFinished()
```
> Vungle is not running/has stopped.

```lua
onVungleAdViewed(isComplete)
```
> Vungle ad has been viewed.


