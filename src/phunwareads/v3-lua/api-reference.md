## API Reference

### Methods
```lua
sdkbox.PluginPhunwareAds:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginPhunwareAds:setListener(listener)
```
> Set listener to listen for phunware events

```lua
sdkbox.PluginPhunwareAds:cache(name)
```
> cache ad by specifying ad name, auto cache default.

```lua
sdkbox.PluginPhunwareAds:isAvailable(name)
```
> is the specified ad available?

```lua
sdkbox.PluginPhunwareAds:show(name)
```
> show ad by specifying ad name.

```lua
sdkbox.PluginPhunwareAds:hide(name)
```
> hide ad by specifying ad name.

```lua
sdkbox.PluginPhunwareAds:setUserID(userID)
```
> set user ID for rewarded video.

```lua
sdkbox.PluginPhunwareAds:getRemainingViews(name)
```
> get remaining views of rewarded video.

```lua
sdkbox.PluginPhunwareAds:setCustomData(name, data)
```
> set custom data of rewarded video


### Listeners
```lua
adLoaded(name)
```
> there is cached content

```lua
adFailed(name, errorCode, msg)
```
> there is error when cache content

```lua
adWillPresent(name)
```
> ad will present

```lua
adDidPresent(name)
```
> ad did present

```lua
adWillDissmiss(name)
```
> ad will dissmiss

```lua
adDidDismiss(name)
```
> ad did dismiss

```lua
willLeaveApp(name)
```
> will leave application

```lua
reward(name, amount, currency, customData)
```
> reward user with specifying ad name


