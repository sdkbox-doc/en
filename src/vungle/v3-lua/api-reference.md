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
> sets userID for rewarded ads.

### Listeners
```lua
onVungleCacheAvailable()
```
> there is cache available of videos

```lua
onVungleStarted()
```
> Vungle has started and is ready to go.

```lua
onVungleFinished()
```
> Vungle is stopped and not running

```lua
onVungleAdViewed()
```
> an ad was viewed.
