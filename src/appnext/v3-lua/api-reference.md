## API Reference

### Methods
```lua
sdkbox.PluginAppnext:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginAppnext:setListener(listener)
```
> Set listener to listen for appnext events

```lua
sdkbox.PluginAppnext:hideAd()
```
> Hide advertisement

```lua
sdkbox.PluginAppnext:showAd()
```
> Show advertisement

```lua
sdkbox.PluginAppnext:refreshAds()
```
> Refresh advertisement

```lua
sdkbox.PluginAppnext:cacheAd(name)
```
> Cache advertisement

```lua
sdkbox.PluginAppnext:isAdReady()
```
> Check if advertisement is ready

```lua
sdkbox.PluginAppnext:cacheVideo(name)
```
> Cache video with @name

```lua
sdkbox.PluginAppnext:showVideo(name)
```
> show video with @name

```lua
sdkbox.PluginAppnext:refreshVideo(name)
```
> Refresh video with @name

```lua
sdkbox.PluginAppnext:isVideoReady(name)
```
> Check if video is ready with @name

```lua
sdkbox.PluginAppnext:setRewardsTransactionId(transactionId)
```
> Set reward video transaction id

```lua
sdkbox.PluginAppnext:setRewardsUserId(userId)
```
> Set reward video user id

```lua
sdkbox.PluginAppnext:setRewardsRewardTypeCurrency(currency)
```
> Set type of reward, such as life / credit / points.

```lua
sdkbox.PluginAppnext:setRewardsAmountRewarded(amount)
```
> Set the amount of currency that was rewarded.

```lua
sdkbox.PluginAppnext:setRewardsCustomParameter(parameter)
```
> Set reward video custom parameter.


### Listeners
```lua
onAdError(msg)
```

```lua
onAdLoaded()
```

```lua
onAdOpened()
```

```lua
onAdClosed()
```

```lua
onAdClicked()
```

```lua
onVideoLoaded(name)
```

```lua
onVideoClicked(name)
```

```lua
onVideoClosed(name)
```

```lua
onVideoEnded(name)
```

```lua
onVideoError(name, msg)
```


