## API Reference

### Methods
```cpp
static void setGDPR ( bool enabled ) ;
```
> Set GDPR

<pre>
>>NOTE>>: please call before 'init' function
</pre>

```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void show ( const std::string & name ) ;
```
> play video ad using provided name that was specified in sdkbox_config.json

```cpp
static void setListener ( AdColonyListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static AdColonyListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static int zoneStatusForZone ( const std::string & zoneID ) ;
```
> Returns the zone status for the specified zone.

<pre>
@deprecated please use getStatus(name) instead
</pre>

```cpp
static AdColonyAdStatus getStatus ( const std::string & name ) ;
```
> Check the availability of the adcolony ads by name

```cpp
static void setCustomID ( const std::string & customID ) ;
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

```cpp
static std::string getCustomID ( ) ;
```
> Returns the device's current custom identifier.

<pre>
@return The custom identifier string most recently set using `+ setCustomID:`.
@see setCustomID:
</pre>

```cpp
static std::string getUniqueDeviceID ( ) ;
```
> Returns an AdColony-defined device identifier.

<pre>
This identifier should remain constant across the lifetime of an iOS device.
The identifier is a SHA-1 hash of the lowercase colon-separated MAC address of the device's WiFi interface.
We do not recommend using this
identifier for new integrations. This method is provided for backwards compatibility.
@return The string representation of the device's AdColony identifier.
</pre>

```cpp
static std::string getAdvertisingIdentifier ( ) ;
```
> Returns the device's advertising identifier.

<pre>
This value can change if the user restores their device or resets ad tracking.
@return The string representation of the device's advertising identifier, introduced in iOS 6. Returns `nil` on iOS 5 or below.
@note this function only available on ios
</pre>

```cpp
static std::string getVendorIdentifier ( ) ;
```
> Returns the device's vendor identifier.

<pre>
@return As of version 2.3 of our iOS SDK, AdColony no longer collects the vendor identifier and this method will return `nil`. This method is provided for backwards compatibility.
@note this function only available on ios
</pre>

```cpp
static int getVideosPerReward ( const std::string & currencyName ) ;
```
> Returns the number of ads that the user must play to earn the designated reward.

<pre>
@note this function only available on ios
</pre>

```cpp
static int getVideoCreditBalance ( const std::string & currencyName ) ;
```
> Returns the number of ads that the user has seen towards their next reward.

<pre>
@note this function only available on ios
</pre>

```cpp
static void cancelAd ( ) ;
```
> Cancels any full-screen ad that is currently playing and returns control to the app.

<pre>
No earnings or V4VC rewards will occur if an ad is canceled programmatically by the app.
This should only be used by apps that must immediately respond to non-standard incoming events,
like a VoIP phone call. This should not be used for standard app interruptions such as
multitasking or regular phone calls.
</pre>

```cpp
static bool videoAdCurrentlyRunning ( ) ;
```
> Whether a full-screen AdColony ad is currently being played.

<pre>
@return A boolean indicating if AdColony is currently playing an ad.
@note this function only available on ios
</pre>

```cpp
static void turnAllAdsOff ( ) ;
```
> This method permanently turns off all AdColony ads for this app on the current device.

<pre>
After this method is called, no ads will be played unless the app is deleted and reinstalled.
This method could be used in the implementation of an In-App Purchase to disable ads;
make sure to allow In-App Purchases to be restored by the user in the case of deleting and reinstalling the app.
@note this function only available on ios
</pre>

```cpp
static void setUserMetadata ( const std::string & metadataType ,
                              const std::string & value ) ;
```
> Provide AdColony with per-user non personally-identifiable information for ad targeting purposes.

<pre>
Providing non personally-identifiable information using this API will improve targeting and unlock
improved earnings for your app. [This support article](http://support.adcolony.com/customer/portal/articles/700183-sdk-user-metadata-pass-through) contains usage guidelines.
@note this function only available on ios
</pre>

```cpp
static void userInterestedIn ( const std::string & topic ) ;
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

```cpp
static void notifyIAPComplete ( const std::string & transactionID ,
                                const std::string & productID ,
                                int quantity ,
                                float price ,
                                const std::string & currencyCode ) ;
```
> Call this method to report IAPs within your application. Note that this API can be leveraged to report standard IAPs
as well as those triggered by AdColony’s IAP Promo (IAPP) advertisements and will improve overall ad targeting.

<pre>
@see onAdColonyIAPRequest:quantity
</pre>

```cpp
static void requestAllAds ( ) ;
```
> Request all ads


### Listeners
```cpp
void onAdColonyChange ( const AdColonyAdInfo & info , bool available );
```
> called when AdColony is finished loading.

```cpp
void onAdColonyReward ( const AdColonyAdInfo & info ,
                        const std::string & currencyName ,
                        int amount ,
                        bool success );
```
> reward was received.

```cpp
void onAdColonyStarted ( const AdColonyAdInfo & info );
```
> showing an ad has started.

```cpp
void onAdColonyFinished ( const AdColonyAdInfo & info );
```
> showing an ad has finished.


