## API Reference

### Methods
```javascript
sdkbox.PluginUnityAds.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginUnityAds.setListener(listener);
```
> Set listener to listen for unityads events

```javascript
sdkbox.PluginUnityAds.isSupported();
```
> is unityads support current platform

```javascript
sdkbox.PluginUnityAds.isReady(placementId);
```
> is unityads ready to show

```javascript
sdkbox.PluginUnityAds.show(placementId);
```
> show unityads

```javascript
sdkbox.PluginUnityAds.getPlacementState(placementId);
```
> unityads placement state


### Listeners

```javascript
unityAdsDidClick(const std::string& placementId);
```
> unityads clicked

```javascript
unityAdsPlacementStateChanged(placementId, oldState, newState);
```
> unityads placement state changed

```javascript
unityAdsReady(placementId);
```
> unityads ready

```javascript
unityAdsDidError(error, message);
```
> unityads error

```javascript
unityAdsDidStart(placementId);
```
> unityads start

```javascript
unityAdsDidFinish(placementId, state);
```
> unityads finish

