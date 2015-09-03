## API Reference

### Methods
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

```cpp
static AdColonyAdStatus getStatus ( const std::string & name ) ;
```
> Check the availability of the adcolony ads by name

```cpp
static void setCustomID ( const std::string & customID ) ;
```
> Assigns your own custom identifier to the current app user.

```cpp
static std::string getCustomID ( ) ;
```
> Returns the device's current custom identifier.

```cpp
static std::string getUniqueDeviceID ( ) ;
```
> Returns an AdColony-defined device identifier.

```cpp
static std::string getAdvertisingIdentifier ( ) ;
```
> Returns the device's advertising identifier.

```cpp
static std::string getVendorIdentifier ( ) ;
```
> Returns the device's vendor identifier.

```cpp
static int getVideosPerReward ( const std::string & currencyName ) ;
```
> Returns the number of ads that the user must play to earn the designated reward.

```cpp
static int getVideoCreditBalance ( const std::string & currencyName ) ;
```
> Returns the number of ads that the user has seen towards their next reward.

```cpp
static void cancelAd ( ) ;
```
> Cancels any full-screen ad that is currently playing and returns control to the app.

```cpp
static bool videoAdCurrentlyRunning ( ) ;
```
> Whether a full-screen AdColony ad is currently being played.

```cpp
static void turnAllAdsOff ( ) ;
```
> This method permanently turns off all AdColony ads for this app on the current device.

```cpp
static void setUserMetadata ( const std::string & metadataType ,
                              const std::string & value ) ;
```
> Provide AdColony with per-user non personally-identifiable information for ad targeting purposes.

```cpp
static void userInterestedIn ( const std::string & topic ) ;
```
> Provide AdColony with real-time feedback about what a user is interested in.

```cpp
static void notifyIAPComplete ( const std::string & transactionID ,
                                const std::string & productID ,
                                int quantity ,
                                float price ,
                                const std::string & currencyCode ) ;
```
> Call this method to report IAPs within your application. Note that this API can be leveraged to report standard IAPs
as well as those triggered by AdColony’s IAP Promo (IAPP) advertisements and will improve overall ad targeting.


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


