## API Reference

### Methods
```lua
sdkbox.PluginKochava:init()
```
> init the kochava service

```lua
sdkbox.PluginKochava:shutdown()
```
> shutdown the kochava service

```lua
sdkbox.PluginKochava:enableLogging(enabled)
```
> enable kochava api logging

```lua
sdkbox.PluginKochava:trackEvent(event, value)
```
> track a single event

```lua
sdkbox.PluginKochava:spatialEvent(title, x, y, z)
```
> spatial event to help visualize data

```lua
sdkbox.PluginKochava:setLimitAdTracking(limitAdTracking)
```
> turn on/off ad tracking

```lua
sdkbox.PluginKochava:retrieveAttribution()
```
> returns the attribution data

```lua
sdkbox.PluginKochava:sendDeepLink(url, application)
```
> send a referral to where your app was opened from.

```lua
sdkbox.PluginKochava:setBeaconCallback(callback)
```
> specify beacon transition callback


### Listeners

