## API Reference

### Methods
```javascript
sdkbox.PluginUnityAds.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginUnityAds.setListener(listener);
```
> Set listener to listen for inmobi events

```javascript
sdkbox.PluginUnityAds.isSupported();
```

```javascript
sdkbox.PluginUnityAds.isReady(placementId);
```

```javascript
sdkbox.PluginUnityAds.show(placementId);
```

```javascript
sdkbox.PluginUnityAds.getPlacementState(placementId);
```

```javascript
sdkbox.PluginUnityAds.setGDPR(enabled);
```
> Enable GDPR

```javascript
sdkbox.PluginUnityAds.setServerId(sid);
```


### Listeners
```javascript
unityAdsDidClick(placementId);
```

```javascript
unityAdsPlacementStateChanged(placementId, oldState, newState);
```

```javascript
unityAdsReady(placementId);
```

```javascript
unityAdsDidError(error, message);
```

```javascript
unityAdsDidStart(placementId);
```

```javascript
unityAdsDidFinish(placementId, state);
```


