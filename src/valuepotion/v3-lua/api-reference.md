## API Reference

### Methods
```lua
sdkbox.PluginValuePotion:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginValuePotion:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginValuePotion:setTest(isTest)
```
> for intergation test

```lua
sdkbox.PluginValuePotion:hasCachedInterstitial(placement)
```
> check if ad is cached

```lua
sdkbox.PluginValuePotion:cacheInterstitial(placement)
```
> cached ad

```lua
sdkbox.PluginValuePotion:openInterstitial(placement)
```
> show ad

```lua
sdkbox.PluginValuePotion:trackEvent(eventName)
```
> track game event

```lua
sdkbox.PluginValuePotion:trackEvent(eventName, eventValue)
```

```lua
sdkbox.PluginValuePotion:trackEvent(category, eventName, label, eventValue)
```

```lua
sdkbox.PluginValuePotion:trackPurchaseEvent(eventName,
                                             revenueAmount,
                                             currency,
                                             orderId,
                                             productId)
```
> track purchase event

```lua
sdkbox.PluginValuePotion:trackPurchaseEvent(eventName,
                                             revenueAmount,
                                             currency,
                                             orderId,
                                             productId,
                                             campaignId,
                                             contentId)
```

```lua
sdkbox.PluginValuePotion:trackPurchaseEvent(category,
                                             eventName,
                                             label,
                                             revenueAmount,
                                             currency,
                                             orderId,
                                             productId,
                                             campaignId,
                                             contentId)
```

```lua
sdkbox.PluginValuePotion:userinfo(attribute, value)
```
> set user info

<pre>
Field              Description
userId             User account id used in game
serverId           If you need to distinguish users by server which they belong to, you should set serverId. Then you can get statistics based on serverId.
birth              Date of birth in YYYYMMDD. If you know only year of birth, fill last four digits with "0" like "19840000". If you know only date of birth(but not year), fill first four digits with "0" like "00001109".
gender             "M" for male, "F" for female.
level              Level of user in game.
friends            Number of user's friends.
accountType        Type of user's account type. (facebook, google, guest, etc)
</pre>


### Listeners
```lua
onCacheInterstitial(placement)
```

```lua
onFailToCacheInterstitial(placement, errorMessage)
```

```lua
onOpenInterstitial(placement)
```

```lua
onFailToOpenInterstitial(placement, errorMessage)
```

```lua
onCloseInterstitial(placement)
```

```lua
onRequestOpenURL(placement, URL)
```

```lua
onRequestPurchase(placement, name, productId, quantity, campaignId, contentId)
```

```lua
onRequestRewards(placement, rewards)
```


