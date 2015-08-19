## API Reference

### Methods
```javascript
sdkbox.PluginAdColony.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginAdColony.show(name);
```
> play video ad using provided name that was specified in sdkbox_config.json

```javascript
sdkbox.PluginAdColony.setListener(listener);
```
> Set listener to listen for adcolony events

```javascript
sdkbox.PluginAdColony.zoneStatusForZone(zoneID);
```
> Returns the zone status for the specified zone.

```javascript
sdkbox.PluginAdColony.getStatus(name);
```
> Check the availability of the adcolony ads by name

```javascript
sdkbox.PluginAdColony.setCustomID(customID);
```
> Assigns your own custom identifier to the current app user.

```javascript
sdkbox.PluginAdColony.getCustomID();
```
> Returns the device's current custom identifier.

```javascript
sdkbox.PluginAdColony.getUniqueDeviceID();
```
> Returns an AdColony-defined device identifier.

```javascript
sdkbox.PluginAdColony.getAdvertisingIdentifier();
```
> Returns the device's advertising identifier.

```javascript
sdkbox.PluginAdColony.getVendorIdentifier();
```
> Returns the device's vendor identifier.

```javascript
sdkbox.PluginAdColony.getVideosPerReward(currencyName);
```
> Returns the number of ads that the user must play to earn the designated reward.

```javascript
sdkbox.PluginAdColony.getVideoCreditBalance(currencyName);
```
> Returns the number of ads that the user has seen towards their next reward.

```javascript
sdkbox.PluginAdColony.cancelAd();
```
> Cancels any full-screen ad that is currently playing and returns control to the app.

```javascript
sdkbox.PluginAdColony.videoAdCurrentlyRunning();
```
> Whether a full-screen AdColony ad is currently being played.

```javascript
sdkbox.PluginAdColony.turnAllAdsOff();
```
> This method permanently turns off all AdColony ads for this app on the current device.

```javascript
sdkbox.PluginAdColony.setUserMetadata(metadataType, value);
```
> Provide AdColony with per-user non personally-identifiable information for ad targeting purposes.

```javascript
sdkbox.PluginAdColony.userInterestedIn(topic);
```
> Provide AdColony with real-time feedback about what a user is interested in.

```javascript
sdkbox.PluginAdColony.notifyIAPComplete(transactionID,
                                         productID,
                                         quantity,
                                         price,
                                         currencyCode);
```
> Call this method to report IAPs within your application. Note that this API can be leveraged to report standard IAPs
as well as those triggered by AdColony’s IAP Promo (IAPP) advertisements and will improve overall ad targeting.


### Listeners
```javascript
onAdColonyChange(info, available);
```
> called when AdColony is finished loading.

```javascript
onAdColonyReward(info, currencyName, amount, success);
```
> reward was received.

```javascript
onAdColonyStarted(info);
```
> showing an ad has started.

```javascript
onAdColonyFinished(info);
```
> showing an ad has finished.


