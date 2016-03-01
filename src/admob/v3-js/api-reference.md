## API Reference

### Methods
```javascript
sdkbox.PluginAdMob.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginAdMob.setListener(listener);
```
> Set listener to listen for admob events

```javascript
sdkbox.PluginAdMob.getVersion();
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```javascript
sdkbox.PluginAdMob.setTestDevices(devices);
```
> Set test devices

```javascript
sdkbox.PluginAdMob.cache(name);
```
> Cache ad with @name

```javascript
sdkbox.PluginAdMob.show(name);
```
> show ad with @name

```javascript
sdkbox.PluginAdMob.hide(name);
```
> hide ad with @name

```javascript
sdkbox.PluginAdMob.isAvailable(name);
```
> check whether ad available with @name

```javascript
sdkbox.PluginAdMob.getCurrBannerWidth();
```
> get width of current banner

```javascript
sdkbox.PluginAdMob.getCurrBannerHeight();
```
> get height of current banner


### Listeners
```javascript
adViewDidReceiveAd(name);
```

```javascript
adViewDidFailToReceiveAdWithError(name, msg);
```

```javascript
adViewWillPresentScreen(name);
```

```javascript
adViewDidDismissScreen(name);
```

```javascript
adViewWillDismissScreen(name);
```

```javascript
adViewWillLeaveApplication(name);
```


