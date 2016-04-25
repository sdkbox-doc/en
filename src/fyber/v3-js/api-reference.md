## API Reference

### Methods
```javascript
sdkbox.PluginFyber.init(userID);
```
> initialize the fyber plugin.

```javascript
sdkbox.PluginFyber.showOfferWall(placementId);
```
> Presents the Fyber Mobile OfferWall as a child view controller of your own view controller.

```javascript
sdkbox.PluginFyber.requestOffers(placementId);
```
> Request the server for rewarded video availability.

```javascript
sdkbox.PluginFyber.showOffers(placementId);
```
> Show an available rewarded video.

```javascript
sdkbox.PluginFyber.requestInterstitial();
```
> Check if interstitial ads are available

```javascript
sdkbox.PluginFyber.showInterstitial();
```
> Shows an interstitial ad. Check first that one is ready to be shown with requestInterstitial.

```javascript
sdkbox.PluginFyber.requestDeltaOfCoins(currencyId);
```
> Fetches the amount of a given currency earned since the last time this method was
invoked for the current user ID / app ID combination.

```javascript
sdkbox.PluginFyber.setAge(age);
```
>  Sets the user's age

```javascript
// "2000-02-03"
sdkbox.PluginFyber.setBirthdate(data);
```
>  Sets the user's date of birth, format (yyyy-MM-dd)

```javascript
// sdkbox.PluginFyber.UserGender.Undefined
// sdkbox.PluginFyber.UserGender.Male
// sdkbox.PluginFyber.UserGender.Female
// sdkbox.PluginFyber.UserGender.Other
sdkbox.PluginFyber.setGender(gender);
```
>  Sets the user's gender

```javascript
// sdkbox.PluginFyber.UserEthnicity.Undefined
// sdkbox.PluginFyber.UserEthnicity.Asian
// sdkbox.PluginFyber.UserEthnicity.Black
// sdkbox.PluginFyber.UserEthnicity.Hispanic
// sdkbox.PluginFyber.UserEthnicity.Indian
// sdkbox.PluginFyber.UserEthnicity.MiddleEastern
// sdkbox.PluginFyber.UserEthnicity.NativeAmerican
// sdkbox.PluginFyber.UserEthnicity.PacificIslander
// sdkbox.PluginFyber.UserEthnicity.White
// sdkbox.PluginFyber.UserEthnicity.Other
sdkbox.PluginFyber.setSexualOrientation(sexualOrientation);
```
>  Sets the user's sexual orientation

```javascript
sdkbox.PluginFyber.setEthnicity(ethnicity);
```
>  Sets the user's ethnicity

```javascript
sdkbox.PluginFyber.setLocation(latitude, longitude);
```
>  Set the user's location

```javascript
sdkbox.PluginFyber.cleanLocation();
```
> Clean the user's location

```javascript
// sdkbox.PluginFyber.UserMaritalStatus.Undefined
// sdkbox.PluginFyber.UserMartialStatus.Single
// sdkbox.PluginFyber.UserMartialStatus.Relationship
// sdkbox.PluginFyber.UserMartialStatus.Married
// sdkbox.PluginFyber.UserMartialStatus.Divorced
// sdkbox.PluginFyber.UserMartialStatus.Engaged
sdkbox.PluginFyber.setMaritalStatus(status);
```
>  Sets the user's marital status

```javascript
sdkbox.PluginFyber.setNumberOfChildren(numberOfChildren);
```
>  Sets the user's number of children

```javascript
sdkbox.PluginFyber.setAnnualHouseholdIncome(income);
```
>  Sets the user's annual household income

```javascript
// sdkbox.PluginFyber.UserEducation.Undefined
// sdkbox.PluginFyber.UserEducation.Other
// sdkbox.PluginFyber.UserEducation.None
// sdkbox.PluginFyber.UserEducation.HighSchool
// sdkbox.PluginFyber.UserEducation.InCollege
// sdkbox.PluginFyber.UserEducation.SomeCollege
// sdkbox.PluginFyber.UserEducation.Associates
// sdkbox.PluginFyber.UserEducation.Bachelors
// sdkbox.PluginFyber.UserEducation.Masters
// sdkbox.PluginFyber.UserEducation.Doctorate
sdkbox.PluginFyber.setEducation(education);
```
>  Sets the user's educational background

```javascript
sdkbox.PluginFyber.setZipcode(zipcode);
```
>  Sets the user's zipcode

```javascript
sdkbox.PluginFyber.setInterests(interests);
```
>  Set the user's list of interests

```javascript
sdkbox.PluginFyber.setIap(flag);
```
>  Sets if in-app purchases are enabled.

```javascript
sdkbox.PluginFyber.setIapAmount(amount);
```
>  Sets the amount that the user has already spent on in-app purchases

```javascript
sdkbox.PluginFyber.setNumberOfSessions(numberOfSessions);
```
>  Sets the number of sessions

```javascript
sdkbox.PluginFyber.setPsTime(timestamp);
```
>  Sets the time spent on the current session

```javascript
sdkbox.PluginFyber.setLastSession(session);
```
>  Sets the duration of the last session

```javascript
// sdkbox.PluginFyber.UserConnectionType.Undefined
// sdkbox.PluginFyber.UserConnectionType.WiFi
// sdkbox.PluginFyber.UserConnectionType.3G
// sdkbox.PluginFyber.UserConnectionType.LTE
// sdkbox.PluginFyber.UserConnectionType.Edge
sdkbox.PluginFyber.setConnectionType(connectionType);
```
>  Sets the connection type used by the user

```javascript
// predefine values
// sdkbox.PluginFyber.UserDevice.Undefined
// sdkbox.PluginFyber.UserDevice.IPhone
// sdkbox.PluginFyber.UserDevice.IPad
// sdkbox.PluginFyber.UserDevice.IPod
// sdkbox.PluginFyber.UserDevice.Android
sdkbox.PluginFyber.setDevice(device);
```
>  Sets the device used by the user

```javascript
sdkbox.PluginFyber.setVersion(version);
```
>  Sets the app version

```javascript
sdkbox.PluginFyber.cleanCustomParameters();
```
> Clean custom parameters, iOS only

```javascript
sdkbox.PluginFyber.addCustomParameters(key, value);
```
>  Sets custom parameters to be sent along with the standard parameters


### Listeners
```javascript
onVirtualCurrencyConnectorFailed(error, errorCode, errorMsg);
```

```javascript
onVirtualCurrencyConnectorSuccess(deltaOfCoins,
                                   currencyId,
                                   currencyName,
                                   transactionId);
```

```javascript
onCanShowInterstitial(canShowInterstitial);
```

```javascript
onInterstitialDidShow();
```

```javascript
onInterstitialDismiss(reason);
```

```javascript
onInterstitialFailed();
```

```javascript
onBrandEngageClientReceiveOffers(areOffersAvailable);
```

```javascript
onBrandEngageClientChangeStatus(status, msg);
```

```javascript
onOfferWallFinish(status);
```


