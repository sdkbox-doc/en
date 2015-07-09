## API Reference

### Methods
```javascript
sdkbox.PluginVungle.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginVungle.show(name);
```
> show ad with a provided name.

```javascript
sdkbox.PluginVungle.setDebug(enable);
```
> enable or disable debug mode.

```javascript
sdkbox.PluginVungle.isCacheAvailable();
```
> is there a cached video available.

```javascript
sdkbox.PluginVungle.setUserID(userID);
```
> sets userID for rewarded ads.

### Listeners
```javascript
onVungleCacheAvailable()
```
> ad cache is available.

```javascript
onVungleStarted()
```
> Vungle is running and available.

```javascript
onVungleFinished()
```
> Vungle is not running/has stopped.

```javascript
onVungleAdViewed()
```
> Vungle ad has been viewed.
