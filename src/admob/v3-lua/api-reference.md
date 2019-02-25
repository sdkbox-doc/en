## API Reference

### Methods
```lua
sdkbox.PluginAdMob:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginAdMob:setListener(listener)
```
> Set listener to listen for admob events

```lua
sdkbox.PluginAdMob:getVersion()
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```lua
sdkbox.PluginAdMob:setTestDevices(devices)
```
> Set test devices

```lua
sdkbox.PluginAdMob:cache(name)
```
> Cache ad with @name

```lua
sdkbox.PluginAdMob:show(name)
```
> show ad with @name

```lua
sdkbox.PluginAdMob:hide(name)
```
> hide ad with @name

<pre>
interstitial does not support hide
</pre>

```lua
sdkbox.PluginAdMob:isAvailable(name)
```
> check whether ad available with @name

```lua
sdkbox.PluginAdMob:getCurrBannerWidth(name)
```
> get width of current banner

<pre>
@return: -1 means current banner is not available
</pre>

```lua
sdkbox.PluginAdMob:getCurrBannerHeight(name)
```
> get height of current banner

<pre>
@return: -1 means current banner is not available
</pre>

```lua
sdkbox.PluginAdMob:getCurrBannerWidthInPixel(name)
```
> get width of current banner in pixel

<pre>
@return -1 means current banner is not available
</pre>

```lua
sdkbox.PluginAdMob:getCurrBannerHeightInPixel(name)
```
> get height of current banner in pixel

<pre>
@return: -1 means current banner is not available
</pre>

```lua
sdkbox.PluginAdMob:setGDPR(enabled)
```
> set GDPR. true: non-personalized ads, false: personalized ads.


### Listeners
```lua
adViewDidReceiveAd(name)
```

```lua
adViewDidFailToReceiveAdWithError(name, msg)
```

```lua
adViewWillPresentScreen(name)
```

```lua
adViewDidDismissScreen(name)
```

```lua
adViewWillDismissScreen(name)
```

```lua
adViewWillLeaveApplication(name)
```

```lua
reward(name, currency, amount)
```


