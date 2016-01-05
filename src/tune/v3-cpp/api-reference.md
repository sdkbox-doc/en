## API Reference

### Methods
```cpp
static void setListener ( TuneListener * listener ) ;
```
> set a listener to listen for event changes.

```cpp
static TuneListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> remove the listener, and can't listen to events anymore

```cpp
static void init ( ) ;
```
> init the instance.

```cpp
static void setDebugMode ( bool enable ) ;
```
> Specifies that the server responses should include debug information.

```cpp
static void setAllowDuplicateRequests ( bool allow ) ;
```
> Set to YES to allow duplicate requests to be registered with the MAT server.

```cpp
// use "checkForDeferredDeepLink"
static void checkForDeferredDeeplinkWithTimeout ( double timeout ) ;
```
> Check for a deferred deeplink entry point upon app installation.
This is safe to call at every app launch, since the function does nothing
unless this is the first launch.

```cpp
static void checkForDeferredDeepLink ( ) ;
```
> Check for a deferred deeplink entry point upon app installation.
This is safe to call at every app launch, since the function does nothing
unless this is the first launch.

```cpp
static void automateIapEventMeasurement ( bool automate ) ;
```
> Enable automatic measurement of app store in-app-purchase events. When enabled, your code
should not explicitly measure events for successful purchases related to StoreKit to avoid event duplication.

```cpp
static void setFacebookEventLogging ( bool logging , bool limit ) ;
```
> Set whether the MAT events should also be logged to the Facebook SDK. This flag is ignored
if the Facebook SDK is not present.

```cpp
static void setExistingUser ( bool existingUser ) ;
```
> Set whether this is an existing user or a new one. This is generally used to
distinguish users who were using previous versions of the app, prior to
integration of the MAT SDK. The default is to assume a new user.

```cpp
static void setAppleAdvertisingIdentifier ( const std::string & appleAdvertisingIdentifier ,
                                            bool adTrackingEnabled ) ;
```
> Set the Apple Advertising Identifier available in iOS 6.

```cpp
static void setAppleVendorIdentifier ( const std::string & appleVendorIdentifier ) ;
```
> Set the Apple Vendor Identifier available in iOS 6.

```cpp
static void setCurrencyCode ( const std::string & currencyCode ) ;
```
> Sets the currency code.

```cpp
static void setJailbroken ( bool jailbroken ) ;
```
> Sets the jailbroken device flag.

```cpp
static void setPackageName ( const std::string & packageName ) ;
```
> Sets the package name (bundle identifier).
Defaults to the Bundle Identifier of the app that is running the sdk.

```cpp
static void setShouldAutoDetectJailbroken ( bool autoDetect ) ;
```
> Specifies if the sdk should auto detect if the iOS device is jailbroken.

```cpp
static void setShouldAutoGenerateAppleVendorIdentifier ( bool autoGenerate ) ;
```
> Specifies if the sdk should pull the Apple Vendor Identifier from the device.
Note that setting to false will clear any previously set value for the property.

```cpp
// use "setPackageName"
static void setSiteId ( const std::string & siteId ) ;
```
> Sets the site ID.

```cpp
static void setTRUSTeId ( const std::string & tpid ) ;
```
> Set the TRUSTe Trusted Preference Identifier (TPID).

```cpp
static void setUserEmail ( const std::string & userEmail ) ;
```
> Sets the user's email address.

```cpp
static void setUserId ( const std::string & userId ) ;
```
> Sets the user ID.

```cpp
static void setUserName ( const std::string & userName ) ;
```
> Sets the user's name.

```cpp
static void setPhoneNumber ( const std::string & phoneNumber ) ;
```
> Sets the user's phone number.

```cpp
static void setFacebookUserId ( const std::string & facebookUserId ) ;
```
> Set user's Facebook ID.

```cpp
static void setTwitterUserId ( const std::string & twitterUserId ) ;
```
> Set user's Twitter ID.

```cpp
static void setGoogleUserId ( const std::string & googleUserId ) ;
```
> Set user's Google ID.

```cpp
static void setAge ( int userAge ) ;
```
> Sets the user's age.

```cpp
static void setGender ( Gender userGender ) ;
```
> Sets the user's gender.

```cpp
static void setLatitude ( double latitude , double longitude ) ;
```
> Sets the user's location.

```cpp
static void setLatitude ( double latitude ,
                          double longitude ,
                          double altitude ) ;
```
> Sets the user's location including altitude.

```cpp
static void setAppAdTracking ( bool enable ) ;
```
> Set app-level ad-tracking.

```cpp
static void setPayingUser ( bool isPayingUser ) ;
```
> Set whether the user is generating revenue for the app or not.
If measureEvent is called with a non-zero revenue, this is automatically set to YES.

```cpp
static void setPreloadData ( const TunePreloadData & preloadData ) ;
```
> Sets publisher information for attribution.

```cpp
static void setPreloadDataForScript ( const std::string & jsonString ) ;
```

```cpp
// use "tuneId"
static std::string matId ( ) ;
```
> Get the MAT ID for this installation (mat_id).

```cpp
static std::string tuneId ( ) ;
```
> Get the Tune ID for this installation.

```cpp
static std::string openLogId ( ) ;
```
> Get the MAT log ID for the first app open (open_log_id).

```cpp
static bool isPayingUser ( ) ;
```
> Get whether the user is revenue-generating.

```cpp
static void measureSession ( ) ;
```
> To be called when an app opens; typically in the AppDelegate::applicationWillEnterForeground() event.

```cpp
static void measureEventName ( const std::string & eventName ) ;
```
> Record an event for an Event Name.

```cpp
static void measureEventId ( int eventId ) ;
```
> Record an event by providing the equivalent Event ID defined on the MobileAppTracking dashboard.

```cpp
static void measureEvent ( const TuneEvent & event ) ;
```
> Record an event with a MATEvent.

```cpp
static void measureEventForScript ( const std::string & jsonString ) ;
```

```cpp
static void setUseCookieTracking ( bool enable ) ;
```
> Sets whether or not to use cookie based tracking.

```cpp
static void setRedirectUrl ( const std::string & redirectUrl ) ;
```
> Sets a url to be used with app-to-app tracking so that
the sdk can open the download (redirect) url. This is
used in conjunction with the setTracking:advertiserId:offerId:publisherId:redirect: method.

```cpp
static void startAppToAppTracking ( const std::string & targetAppPackageName ,
                                    const std::string & targetAppAdvertiserId ,
                                    const std::string & targetAdvertiserOfferId ,
                                    const std::string & targetAdvertiserPublisherId ,
                                    bool shouldRedirect ) ;
```
> Start an app-to-app tracking session on the MAT server.

```cpp
static void applicationDidOpenURL ( const std::string & urlString ,
                                    const std::string & sourceApplication ) ;
```
> Record the URL and Source when an application is opened via a URL scheme.
This typically occurs during OAUTH or when an app exits and is returned
to via a URL. The data will be sent to the HasOffers server when the next
measureXXX method is called so that a Re-Engagement can be recorded.

```cpp
static void setDeepLink ( const std::string & deepLinkUrl ) ;
```
> Record the URL and Source when an application is opened via a URL scheme.


### Listeners
```cpp
void onMobileAppTrackerEnqueuedActionWithReferenceId ( const std::string & referenceId );
```

```cpp
void onMobileAppTrackerDidSucceedWithData ( const std::string & data );
```

```cpp
void onMobileAppTrackerDidFailWithError ( const std::string & errorString );
```

```cpp
void onMobileAppTrackerDidReceiveDeeplink ( const std::string & deeplink ,
                                            bool timeout );
```

```cpp
void onMobileAppTrackerDidFailDeeplinkWithError ( const std::string & errorString );
```


