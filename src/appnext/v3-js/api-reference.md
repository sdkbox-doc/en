## API Reference

### Methods
```javascript
sdkbox.PluginAppnext.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginAppnext.setListener(listener);
```
> Set listener to listen for appnext events

```javascript
sdkbox.PluginAppnext.hideAd();
```
> Hide advertisement

```javascript
sdkbox.PluginAppnext.showAd();
```
> Show advertisement

```javascript
sdkbox.PluginAppnext.refreshAds();
```
> Refresh advertisement

```javascript
sdkbox.PluginAppnext.cacheAd(name);
```
> Cache advertisement

```javascript
sdkbox.PluginAppnext.isAdReady();
```
> Check if advertisement is ready

```javascript
sdkbox.PluginAppnext.cacheVideo(name);
```
> Cache video with @name

```javascript
sdkbox.PluginAppnext.showVideo(name);
```
> show video with @name

```javascript
sdkbox.PluginAppnext.refreshVideo(name);
```
> Refresh video with @name

```javascript
sdkbox.PluginAppnext.isVideoReady(name);
```
> Check if video is ready with @name

```javascript
sdkbox.PluginAppnext.setRewardsTransactionId(transactionId);
```
> Set reward video transaction id

```javascript
sdkbox.PluginAppnext.setRewardsUserId(userId);
```
> Set reward video user id

```javascript
sdkbox.PluginAppnext.setRewardsRewardTypeCurrency(currency);
```
> Set type of reward, such as life / credit / points.

```javascript
sdkbox.PluginAppnext.setRewardsAmountRewarded(amount);
```
> Set the amount of currency that was rewarded.

```javascript
sdkbox.PluginAppnext.setRewardsCustomParameter(parameter);
```
> Set reward video custom parameter.


### Listeners
```javascript
onAdError(msg);
```

```javascript
onAdLoaded();
```

```javascript
onAdOpened();
```

```javascript
onAdClosed();
```

```javascript
onAdClicked();
```

```javascript
onVideoLoaded(name);
```

```javascript
onVideoClicked(name);
```

```javascript
onVideoClosed(name);
```

```javascript
onVideoEnded(name);
```

```javascript
onVideoError(name, msg);
```


