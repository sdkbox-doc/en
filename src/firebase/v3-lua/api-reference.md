## API Reference

### Methods
```lua
sdkbox.firebase.Analytics:init()
```
>  initialize the plugin instance.

```lua
sdkbox.firebase.Analytics:getVersion()
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```lua
sdkbox.firebase.Analytics:setUserProperty(name, value)
```

```lua
sdkbox.firebase.Analytics:setUserID(userID)
```

```lua
sdkbox.firebase.Analytics:setScreenName(screen, screenClass)
```

```lua
sdkbox.firebase.Analytics:logEvent(event, params)
```

```lua
sdkbox.firebase.Analytics:resetAnalyticsData()
```
> Clears all analytics data for this instance from the device and resets the app instance ID.
FIRAnalyticsConfiguration values will be reset to the default values.

```lua
sdkbox.firebase.Analytics:setAnalyticsCollectionEnabled(enabled)
```
> Sets whether analytics collection is enabled for this app on this device.
This setting is persisted across app sessions. By default it is enabled. (Only for Android)


### Listeners

