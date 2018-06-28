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

<pre>
interstitial does not support hide
</pre>

```javascript
sdkbox.PluginAdMob.isAvailable(name);
```
> check whether ad available with @name

```javascript
sdkbox.PluginAdMob.getCurrBannerWidth(name);
```
> get width of current banner

<pre>
@return: -1 means current banner is not available
</pre>

```javascript
sdkbox.PluginAdMob.getCurrBannerHeight(name);
```
> get height of current banner

<pre>
@return: -1 means current banner is not available
</pre>

```javascript
sdkbox.PluginAdMob.getCurrBannerWidthInPixel(name);
```
> get width of current banner in pixel

<pre>
@return -1 means current banner is not available
</pre>

```javascript
sdkbox.PluginAdMob.getCurrBannerHeightInPixel(name);
```
> get height of current banner in pixel

<pre>
@return: -1 means current banner is not available
</pre>

```javascript
sdkbox.PluginAdMob.setGDPR(enabled);
```
> set GDPR


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

```javascript
reward(name, currency, amount);
```


