## API Reference

### Methods
```lua
sdkbox.PluginAdColony:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginAdColony:show(name)
```
> play video ad using provided name that was specified in sdkbox_config.json

```lua
sdkbox.PluginAdColony:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginAdColony:zoneStatusForZone(zoneID)
```
> Returns the zone status for the specified zone.

```lua
sdkbox.PluginAdColony:getStatus(name)
```
> Check the availability of the adcolony ads by name

```lua
sdkbox.PluginAdColony:setCustomID(customID)
```
> Assigns your own custom identifier to the current app user.

```lua
sdkbox.PluginAdColony:getCustomID()
```
> Returns the device's current custom identifier.

```lua
sdkbox.PluginAdColony:getUniqueDeviceID()
```
> Returns an AdColony-defined device identifier.

```lua
sdkbox.PluginAdColony:getAdvertisingIdentifier()
```
> Returns the device's advertising identifier.

```lua
sdkbox.PluginAdColony:getVendorIdentifier()
```
> Returns the device's vendor identifier.

```lua
sdkbox.PluginAdColony:getVideosPerReward(currencyName)
```
> Returns the number of ads that the user must play to earn the designated reward.

```lua
sdkbox.PluginAdColony:getVideoCreditBalance(currencyName)
```
> Returns the number of ads that the user has seen towards their next reward.

```lua
sdkbox.PluginAdColony:cancelAd()
```
> Cancels any full-screen ad that is currently playing and returns control to the app.

```lua
sdkbox.PluginAdColony:videoAdCurrentlyRunning()
```
> Whether a full-screen AdColony ad is currently being played.

```lua
sdkbox.PluginAdColony:turnAllAdsOff()
```
> This method permanently turns off all AdColony ads for this app on the current device.

```lua
sdkbox.PluginAdColony:setUserMetadata(metadataType, value)
```
> Provide AdColony with per-user non personally-identifiable information for ad targeting purposes.

```lua
sdkbox.PluginAdColony:userInterestedIn(topic)
```
> Provide AdColony with real-time feedback about what a user is interested in.

```lua
sdkbox.PluginAdColony:notifyIAPComplete(transactionID,
                                         productID,
                                         quantity,
                                         price,
                                         currencyCode)
```
> Call this method to report IAPs within your application. Note that this API can be leveraged to report standard IAPs
as well as those triggered by AdColony’s IAP Promo (IAPP) advertisements and will improve overall ad targeting.


### Listeners
```lua
onAdColonyChange(info, available)
```
> called when AdColony is finished loading.

```lua
onAdColonyReward(info, currencyName, amount, success)
```
> reward was received.

```lua
onAdColonyStarted(info)
```
> showing an ad has started.

```lua
onAdColonyFinished(info)
```
> showing an ad has finished.


