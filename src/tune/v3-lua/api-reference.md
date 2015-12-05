## API Reference

### Methods
```lua
sdkbox.PluginTune:setListener(listener)
```
> set a listener to listen for event changes.

```lua
sdkbox.PluginTune:init()
```
> init the instance.

```lua
sdkbox.PluginTune:setDebugMode(enable)
```
> Specifies that the server responses should include debug information.

```lua
sdkbox.PluginTune:setAllowDuplicateRequests(allow)
```
> Set to YES to allow duplicate requests to be registered with the MAT server.

```lua
sdkbox.PluginTune:checkForDeferredDeeplinkWithTimeout(timeout)
```
> Check for a deferred deeplink entry point upon app installation.
This is safe to call at every app launch, since the function does nothing
unless this is the first launch.

```lua
sdkbox.PluginTune:automateIapEventMeasurement(automate)
```
> Enable automatic measurement of app store in-app-purchase events. When enabled, your code
should not explicitly measure events for successful purchases related to StoreKit to avoid event duplication.

```lua
sdkbox.PluginTune:setFacebookEventLogging(logging, limit)
```
> Set whether the MAT events should also be logged to the Facebook SDK. This flag is ignored
if the Facebook SDK is not present.

```lua
sdkbox.PluginTune:setExistingUser(existingUser)
```
> Set whether this is an existing user or a new one. This is generally used to
distinguish users who were using previous versions of the app, prior to
integration of the MAT SDK. The default is to assume a new user.

```lua
sdkbox.PluginTune:setAppleAdvertisingIdentifier(appleAdvertisingIdentifier,
                                                 adTrackingEnabled)
```
> Set the Apple Advertising Identifier available in iOS 6.

```lua
sdkbox.PluginTune:setAppleVendorIdentifier(appleVendorIdentifier)
```
> Set the Apple Vendor Identifier available in iOS 6.

```lua
sdkbox.PluginTune:setCurrencyCode(currencyCode)
```
> Sets the currency code.

```lua
sdkbox.PluginTune:setJailbroken(jailbroken)
```
> Sets the jailbroken device flag.

```lua
sdkbox.PluginTune:setPackageName(packageName)
```
> Sets the package name (bundle identifier).
Defaults to the Bundle Identifier of the app that is running the sdk.

```lua
sdkbox.PluginTune:setShouldAutoDetectJailbroken(autoDetect)
```
> Specifies if the sdk should auto detect if the iOS device is jailbroken.

```lua
sdkbox.PluginTune:setShouldAutoGenerateAppleVendorIdentifier(autoGenerate)
```
> Specifies if the sdk should pull the Apple Vendor Identifier from the device.
Note that setting to false will clear any previously set value for the property.

```lua
sdkbox.PluginTune:setSiteId(siteId)
```
> Sets the site ID.

```lua
sdkbox.PluginTune:setTRUSTeId(tpid)
```
> Set the TRUSTe Trusted Preference Identifier (TPID).

```lua
sdkbox.PluginTune:setUserEmail(userEmail)
```
> Sets the user's email address.

```lua
sdkbox.PluginTune:setUserId(userId)
```
> Sets the user ID.

```lua
sdkbox.PluginTune:setUserName(userName)
```
> Sets the user's name.

```lua
sdkbox.PluginTune:setPhoneNumber(phoneNumber)
```
> Sets the user's phone number.

```lua
sdkbox.PluginTune:setFacebookUserId(facebookUserId)
```
> Set user's Facebook ID.

```lua
sdkbox.PluginTune:setTwitterUserId(twitterUserId)
```
> Set user's Twitter ID.

```lua
sdkbox.PluginTune:setGoogleUserId(googleUserId)
```
> Set user's Google ID.

```lua
sdkbox.PluginTune:setAge(userAge)
```
> Sets the user's age.

```lua
sdkbox.PluginTune:setGender(userGender)
```
> Sets the user's gender.

```lua
sdkbox.PluginTune:setLatitude(latitude, longitude)
```
> Sets the user's location.

```lua
sdkbox.PluginTune:setLatitude(latitude, longitude, altitude)
```
> Sets the user's location including altitude.

```lua
sdkbox.PluginTune:setAppAdTracking(enable)
```
> Set app-level ad-tracking.

```lua
sdkbox.PluginTune:setPayingUser(isPayingUser)
```
> Set whether the user is generating revenue for the app or not.
If measureEvent is called with a non-zero revenue, this is automatically set to YES.

```lua
sdkbox.PluginTune:setPreloadData(preloadData)
```
> Sets publisher information for attribution.

```lua
sdkbox.PluginTune:matId()
```
> Get the MAT ID for this installation (mat_id).

```lua
sdkbox.PluginTune:tuneId()
```
> Get the Tune ID for this installation.

```lua
sdkbox.PluginTune:openLogId()
```
> Get the MAT log ID for the first app open (open_log_id).

```lua
sdkbox.PluginTune:isPayingUser()
```
> Get whether the user is revenue-generating.

```lua
sdkbox.PluginTune:measureSession()
```
> To be called when an app opens; typically in the AppDelegate::applicationWillEnterForeground() event.

```lua
sdkbox.PluginTune:measureEventName(eventName)
```
> Record an event for an Event Name.

```lua
sdkbox.PluginTune:measureEventId(eventId)
```
> Record an event by providing the equivalent Event ID defined on the MobileAppTracking dashboard.

```lua
sdkbox.PluginTune:measureEvent(event)
```
> Record an event with a MATEvent.

```lua
sdkbox.PluginTune:setUseCookieTracking(enable)
```
> Sets whether or not to use cookie based tracking.

```lua
sdkbox.PluginTune:setRedirectUrl(redirectUrl)
```
> Sets a url to be used with app-to-app tracking so that
the sdk can open the download (redirect) url. This is
used in conjunction with the setTracking:advertiserId:offerId:publisherId:redirect: method.

```lua
sdkbox.PluginTune:startAppToAppTracking(targetAppPackageName,
                                         targetAppAdvertiserId,
                                         targetAdvertiserOfferId,
                                         targetAdvertiserPublisherId,
                                         shouldRedirect)
```
> Start an app-to-app tracking session on the MAT server.

```lua
sdkbox.PluginTune:applicationDidOpenURL(urlString, sourceApplication)
```
> Record the URL and Source when an application is opened via a URL scheme.
This typically occurs during OAUTH or when an app exits and is returned
to via a URL. The data will be sent to the HasOffers server when the next
measureXXX method is called so that a Re-Engagement can be recorded.


### Listeners
```lua
onEnqueuedAction(referenceId)
```

```lua
onSucceed(data)
```

```lua
onFailed(errorString)
```

```lua
onReceiveDeeplink(deeplink, timeout)
```

```lua
onMobileAppTrackerDidFailDeeplinkWithError(errorString)
```


