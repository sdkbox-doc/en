## API Reference

### Methods
```javascript
sdkbox.PluginAdColony.setGDPR(enabled);
```
> Set GDPR

<pre>
>>NOTE>>: please call before 'init' function
</pre>

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

<pre>
@deprecated please use getStatus(name) instead
</pre>

```javascript
sdkbox.PluginAdColony.getStatus(name);
```
> Check the availability of the adcolony ads by name

```javascript
sdkbox.PluginAdColony.setCustomID(customID);
```
> Assigns your own custom identifier to the current app user.

<pre>
Once you've provided an identifier, AdColony will persist it across app
restarts (stored on disk only) until you update it. If using this method,
call it before `+ configureWithAppID:zoneIDs:delegate:logging:` so that the
identifier is used consistently across all server communications. The
identifier will also pass through to server-side V4VC callbacks.
@see getCustomID
</pre>

```javascript
sdkbox.PluginAdColony.getCustomID();
```
> Returns the device's current custom identifier.

<pre>
@return The custom identifier string most recently set using `+ setCustomID:`.
@see setCustomID:
</pre>

```javascript
sdkbox.PluginAdColony.getUniqueDeviceID();
```
> Returns an AdColony-defined device identifier.

<pre>
This identifier should remain constant across the lifetime of an iOS device.
The identifier is a SHA-1 hash of the lowercase colon-separated MAC address of the device's WiFi interface.
We do not recommend using this
identifier for new integrations. This method is provided for backwards compatibility.
@return The string representation of the device's AdColony identifier.
</pre>

```javascript
sdkbox.PluginAdColony.getAdvertisingIdentifier();
```
> Returns the device's advertising identifier.

<pre>
This value can change if the user restores their device or resets ad tracking.
@return The string representation of the device's advertising identifier, introduced in iOS 6. Returns `nil` on iOS 5 or below.
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.getVendorIdentifier();
```
> Returns the device's vendor identifier.

<pre>
@return As of version 2.3 of our iOS SDK, AdColony no longer collects the vendor identifier and this method will return `nil`. This method is provided for backwards compatibility.
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.getVideosPerReward(currencyName);
```
> Returns the number of ads that the user must play to earn the designated reward.

<pre>
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.getVideoCreditBalance(currencyName);
```
> Returns the number of ads that the user has seen towards their next reward.

<pre>
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.cancelAd();
```
> Cancels any full-screen ad that is currently playing and returns control to the app.

<pre>
No earnings or V4VC rewards will occur if an ad is canceled programmatically by the app.
This should only be used by apps that must immediately respond to non-standard incoming events,
like a VoIP phone call. This should not be used for standard app interruptions such as
multitasking or regular phone calls.
</pre>

```javascript
sdkbox.PluginAdColony.videoAdCurrentlyRunning();
```
> Whether a full-screen AdColony ad is currently being played.

<pre>
@return A boolean indicating if AdColony is currently playing an ad.
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.turnAllAdsOff();
```
> This method permanently turns off all AdColony ads for this app on the current device.

<pre>
After this method is called, no ads will be played unless the app is deleted and reinstalled.
This method could be used in the implementation of an In-App Purchase to disable ads;
make sure to allow In-App Purchases to be restored by the user in the case of deleting and reinstalling the app.
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.setUserMetadata(metadataType, value);
```
> Provide AdColony with per-user non personally-identifiable information for ad targeting purposes.

<pre>
Providing non personally-identifiable information using this API will improve targeting and unlock
improved earnings for your app. [This support article](http://support.adcolony.com/customer/portal/articles/700183-sdk-user-metadata-pass-through) contains usage guidelines.
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.userInterestedIn(topic);
```
> Provide AdColony with real-time feedback about what a user is interested in.

<pre>
Providing non personally-identifiable information using this API will improve targeting and unlock
improved earnings for your app. [This support article](http://support.adcolony.com/customer/portal/articles/700183-sdk-user-metadata-pass-through) contains usage guidelines.
You can call this as often as you want with various topics that the user has engaged in
within your app or as the user engages in them. For example, if the user has started browsing
the finance section of a news app, a developer should call: `[AdColony userInterestedIn:@"finance"]`.
@note this function only available on ios
</pre>

```javascript
sdkbox.PluginAdColony.notifyIAPComplete(transactionID,
                                         productID,
                                         quantity,
                                         price,
                                         currencyCode);
```
> Call this method to report IAPs within your application. Note that this API can be leveraged to report standard IAPs
as well as those triggered by AdColony's IAP Promo (IAPP) advertisements and will improve overall ad targeting.

<pre>
@see onAdColonyIAPRequest:quantity
</pre>

```javascript
sdkbox.PluginAdColony.requestAllAds();
```
> Request all ads


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


