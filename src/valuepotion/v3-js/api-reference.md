## API Reference

### Methods
```javascript
sdkbox.PluginValuePotion.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginValuePotion.setListener(listener);
```
> Set listener to listen for adcolony events

```javascript
sdkbox.PluginValuePotion.setTest(isTest);
```
> for intergation test

```javascript
sdkbox.PluginValuePotion.hasCachedInterstitial(placement);
```
> check if ad is cached

```javascript
sdkbox.PluginValuePotion.cacheInterstitial(placement);
```
> cached ad

```javascript
sdkbox.PluginValuePotion.openInterstitial(placement);
```
> show ad

```javascript
sdkbox.PluginValuePotion.trackEvent(eventName);
```
> track game event

```javascript
sdkbox.PluginValuePotion.trackEvent(eventName, eventValue);
```

```javascript
sdkbox.PluginValuePotion.trackEvent(category, eventName, label, eventValue);
```

```javascript
sdkbox.PluginValuePotion.trackPurchaseEvent(eventName,
                                             revenueAmount,
                                             currency,
                                             orderId,
                                             productId);
```
> track purchase event

```javascript
sdkbox.PluginValuePotion.trackPurchaseEvent(eventName,
                                             revenueAmount,
                                             currency,
                                             orderId,
                                             productId,
                                             campaignId,
                                             contentId);
```

```javascript
sdkbox.PluginValuePotion.trackPurchaseEvent(category,
                                             eventName,
                                             label,
                                             revenueAmount,
                                             currency,
                                             orderId,
                                             productId,
                                             campaignId,
                                             contentId);
```

```javascript
sdkbox.PluginValuePotion.userinfo(attribute, value);
```
> set user info


### Listeners
```javascript
onCacheInterstitial(placement);
```

```javascript
onFailToCacheInterstitial(placement, errorMessage);
```

```javascript
onOpenInterstitial(placement);
```

```javascript
onFailToOpenInterstitial(placement, errorMessage);
```

```javascript
onCloseInterstitial(placement);
```

```javascript
onRequestOpenURL(placement, URL);
```

```javascript
onRequestPurchase(placement, name, productId, quantity, campaignId, contentId);
```

```javascript
onRequestRewards(placement, rewards);
```


