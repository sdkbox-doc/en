## API Reference

### Methods
```lua
sdkbox.PluginAdColony:zoneStatusForZone(zoneID)
```
> returns the status for the specified zone. Use this to pre-load a zone.

```lua
sdkbox.PluginAdColony:isVirtualCurrencyRewardAvailableForZone(zoneID)
```
> check if this zone offers a virtual currency reward.

```lua
sdkbox.PluginAdColony:show(name)
```
> play video ad using provided __zone name__ that was specified in `sdkbox_config.json`.

```lua
sdkbox.PluginAdColony:getStatus(name)
```
> Check the availability of the AdColony ads by name

```lua
sdkbox.PluginAdColony:getVirtualCurrencyRewardAmountForZone(zoneID)
```
> is there a virtual currency reward available to the user today for passed in
zone.

```lua
sdkbox.PluginAdColony:init()
```
> initialize the instance.

```lua
sdkbox.PluginAdColony:videoAdCurrentlyRunning()
```
> is there a video currently showing?

```lua
sdkbox.PluginAdColony:turnAllAdsOff()
```
> turn off all ads.

```lua
sdkbox.PluginAdColony:getVideoCreditBalance(currencyName)
```
> get video credit balance for passed in currency name.

```lua
sdkbox.PluginAdColony:getVideosPerReward(currencyName)
```
> are there multiple videos to watch per reward? Get the number of them.

```lua
sdkbox.PluginAdColony:getVirtualCurrencyNameForZone(zoneID)
```
> get virtual currency name for passed in zone.

```lua
sdkbox.PluginAdColony:getVirtualCurrencyRewardsAvailableTodayForZone(zoneID)
```
> is there a virtual currency reward available to the user today for passed in
zone.

```lua
sdkbox.PluginAdColony:cancelAd()
```
> stop the currently showing ad.

### Listeners
```cpp
/**
 * The structure of data
 * data.name : name of the ad (in sdkbox_config.json)
 * data.zoneID : the zoneID of the ad
 * data.shown : indicates wether the ad gets shown or closed by user
 * data.iapEnabled : indicating whether or not the associated ad is an IAP
 * data.iapProductID : product identifier for the associated ad's IAP
 * data.iapQuantity : he number of items the user wishes to purchase
 * data.iapEngagementType : indicating the IAP engagement mechanism
 *
 * avail = bool
 */
```
```lua
onAdColonyChange(data, available)
```
> called when AdColony is finished loading.

```lua
onAdColonyReward(data, currencyName, amount, success)
```
> reward was received.

```lua
onAdColonyStarted(data)
```
> showing an ad has started.

```lua
onAdColonyFinished(data)
```
> showing an ad has finished.
