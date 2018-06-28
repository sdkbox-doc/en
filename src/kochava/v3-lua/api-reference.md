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

<pre>
http://support.kochava.com/support/solutions/articles/1000059874-ios-sdk-documentation#caleve
</pre>

```lua
sdkbox.PluginKochava:spatialEvent(title, x, y, z)
```
> spatial event to help visualize data

<pre>
http://support.kochava.com/support/solutions/articles/1000059874-ios-sdk-documentation#senspa
just support on ios
</pre>

```lua
sdkbox.PluginKochava:setLimitAdTracking(limitAdTracking)
```
> turn on/off ad tracking

<pre>
http://support.kochava.com/support/solutions/articles/1000059874-ios-sdk-documentation#toglim
</pre>

```lua
sdkbox.PluginKochava:sendDeepLink(url, application)
```
> send a referral to where your app was opened from.


### Listeners

