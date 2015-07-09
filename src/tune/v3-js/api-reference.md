## API Reference

### Methods
```javascript
sdkbox.PluginTune.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginTune.setDebugMode(enable);
```
> Specifies that the server responses should include debug information.

```javascript
sdkbox.PluginTune.setAllowDuplicateRequests(allow);
```
> Set to YES to allow duplicate requests to be registered with the MAT server.

```javascript
sdkbox.PluginTune.checkForDeferredDeeplinkWithTimeout(timeout);
```
> Check for a deferred deeplink entry point upon app installation.

```javascript
sdkbox.PluginTune.automateIapEventMeasurement(automate);
```
> Enable automatic measurement of app store in-app-purchase events. When enabled, your code should not explicitly measure events for successful purchases related to StoreKit to avoid event duplication.

```javascript
sdkbox.PluginTune.setFacebookEventLogging(logging, limit);
```
> Set whether the MAT events should also be logged to the Facebook SDK. This flag is ignored if the Facebook SDK is not present.

```javascript
sdkbox.PluginTune.setExistingUser(existingUser);
```
> Set whether this is an existing user or a new one. This is generally used to
distinguish users who were using previous versions of the app, prior to
integration of the MAT SDK. The default is to assume a new user.

```javascript
sdkbox.PluginTune.setAppleAdvertisingIdentifier(appleAdvertisingIdentifier, adTrackingEnabled);
```
> Set the Apple Advertising Identifier available in iOS 6.

```javascript
sdkbox.PluginTune.setAppleVendorIdentifier(appleVendorIdentifier);
```
> Set the Apple Vendor Identifier available in iOS 6.

```javascript
sdkbox.PluginTune.setCurrencyCode(currencyCode);
```
> Sets the currency code.

```javascript
sdkbox.PluginTune.setJailbroken(jailbroken);
```
> Sets the jailbroken device flag.

```javascript
sdkbox.PluginTune.setPackageName(packageName);
```
> Sets the package name (bundle identifier).

```javascript
sdkbox.PluginTune.setShouldAutoDetectJailbroken(autoDetect);
```
> Specifies if the sdk should auto detect if the iOS device is jailbroken.

```javascript
sdkbox.PluginTune.setShouldAutoGenerateAppleVendorIdentifier(autoGenerate);
```
> Specifies if the sdk should pull the Apple Vendor Identifier from the device. Note that setting to false will clear any previously set value for the property.

```javascript
sdkbox.PluginTune.setSiteId(siteId);
```
> Sets the site ID.

```javascript
sdkbox.PluginTune.setTRUSTeId(tpid);
```
> Set the TRUSTe Trusted Preference Identifier (TPID).

```javascript
sdkbox.PluginTune.setUserEmail(userEmail);
```
> Sets the user's email address.

```javascript
sdkbox.PluginTune.setUserId(userId);
```
> Sets the user ID.

```javascript
sdkbox.PluginTune.setUserName(userName);
```
> Sets the user's name.

```javascript
sdkbox.PluginTune.setPhoneNumber(phoneNumber);
```
> Sets the user's phone number.

```javascript
sdkbox.PluginTune.setFacebookUserId(facebookUserId);
```
> Set user's Facebook ID.

```javascript
sdkbox.PluginTune.setTwitterUserId(twitterUserId);
```
> Set user's Twitter ID.

```javascript
sdkbox.PluginTune.setGoogleUserId(googleUserId);
```
> Set user's Google ID.

```javascript
sdkbox.PluginTune.setAge(long userAge);
```
> Sets the user's age.

```javascript
sdkbox.PluginTune.setGender(Gender userGender);
```
> Sets the user's gender.

```javascript
sdkbox.PluginTune.setLatitude(latitude, longitude);
```
> Sets the user's location.

```javascript
sdkbox.PluginTune.setLatitude(latitude, longitude, altitude);
```
> Sets the user's location including altitude.

```javascript
sdkbox.PluginTune.setAppAdTracking(enable);
```
> Set app-level ad-tracking.

```javascript
sdkbox.PluginTune.setPayingUser(isPayingUser);
```
> Set whether the user is generating revenue for the app or not. If measureEvent is called with a non-zero revenue, this is automatically set to YES.

```javascript
sdkbox.PluginTune.setPreloadDataForScript(jsonString);
sdkbox.PluginTune.setPreloadData(preloadData);
```
> Sets publisher information for attribution.

```javascript
sdkbox.PluginTune.matId();
```
> Get the MAT ID for this installation (mat_id).

```javascript
sdkbox.PluginTune.openLogId();
```
> Get the MAT log ID for the first app open (open_log_id).

```javascript
sdkbox.PluginTune.isPayingUser();
```
> Get whether the user is revenue-generating.

```javascript
sdkbox.PluginTune.measureSession();
```
> To be called when an app opens; typically in the AppDelegate::applicationWillEnterForeground() event.

```javascript
sdkbox.PluginTune.measureEventName(eventName);
```
> Record an event for an Event Name.

```javascript
sdkbox.PluginTune.measureEventId(eventId);
```
> Record an event by providing the equivalent Event ID defined on the MobileAppTracking dashboard.

```javascript
sdkbox.PluginTune.measureEventForScript(jsonString);
sdkbox.PluginTune.measureEvent(event);
```
> Record an event with a MATEvent.

```javascript
sdkbox.PluginTune.setUseCookieTracking(enable);
```
> Sets whether or not to use cookie based tracking.

```javascript
sdkbox.PluginTune.setRedirectUrl(redirectUrl);
```
> Sets a url to be used with app-to-app tracking so that the sdk can open the download (redirect) url. This is used in conjunction with the setTracking:advertiserId:offerId:publisherId:redirect: method.

```javascript
sdkbox.PluginTune.startAppToAppTracking(targetAppPackageName,
                                 targetAppAdvertiserId,
                                 targetAdvertiserOfferId,
                                 targetAdvertiserPublisherId,
                                 shouldRedirect);
```
> Start an app-to-app tracking session on the MAT server.

```javascript
sdkbox.PluginTune.applicationDidOpenURL(urlString, sourceApplication);
```
> Record the URL and Source when an application is opened via a URL scheme.
This typically occurs during OAUTH or when an app exits and is returned
to via a URL. The data will be sent to the HasOffers server when the next
measureXXX method is called so that a Re-Engagement can be recorded.
