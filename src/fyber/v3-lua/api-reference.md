## API Reference

### Methods
```lua
sdkbox.PluginFyber:init(userID)
```
> initialize the fyber plugin.

```lua
sdkbox.PluginFyber:showOfferWall(placementId)
```
> Presents the Fyber Mobile OfferWall as a child view controller of your own view controller.

```lua
sdkbox.PluginFyber:requestOffers(placementId)
```
> Request the server for rewarded video availability.

```lua
sdkbox.PluginFyber:showOffers(placementId)
```
> Show an available rewarded video.

```lua
sdkbox.PluginFyber:requestInterstitial()
```
> Check if interstitial ads are available

```lua
sdkbox.PluginFyber:showInterstitial()
```
> Shows an interstitial ad. Check first that one is ready to be shown with requestInterstitial.

```lua
sdkbox.PluginFyber:requestDeltaOfCoins(currencyId)
```
> Fetches the amount of a given currency earned since the last time this method was
invoked for the current user ID / app ID combination.

```lua
sdkbox.PluginFyber:setAge(age)
```
>  Sets the user's age

```lua
-- "2000-02-03"
sdkbox.PluginFyber:setBirthdate(data)
```
>  Sets the user's date of birth, format (yyyy-MM-dd)

```lua
-- sdkbox.PluginFyber.UserGender.Undefined
-- sdkbox.PluginFyber.UserGender.Male
-- sdkbox.PluginFyber.UserGender.Female
-- sdkbox.PluginFyber.UserGender.Other
sdkbox.PluginFyber:setGender(gender)
```
>  Sets the user's gender

```lua
-- sdkbox.PluginFyber.UserSexualOrientation.Undefined
-- sdkbox.PluginFyber.UserSexualOrientation.Straight
-- sdkbox.PluginFyber.UserSexualOrientation.Bisexual
-- sdkbox.PluginFyber.UserSexualOrientation.Gay
-- sdkbox.PluginFyber.UserSexualOrientation.Unknown
sdkbox.PluginFyber:setSexualOrientation(sexualOrientation)
```
>  Sets the user's sexual orientation

```lua
-- sdkbox.PluginFyber.UserEthnicity.Undefined
-- sdkbox.PluginFyber.UserEthnicity.Asian
-- sdkbox.PluginFyber.UserEthnicity.Black
-- sdkbox.PluginFyber.UserEthnicity.Hispanic
-- sdkbox.PluginFyber.UserEthnicity.Indian
-- sdkbox.PluginFyber.UserEthnicity.MiddleEastern
-- sdkbox.PluginFyber.UserEthnicity.NativeAmerican
-- sdkbox.PluginFyber.UserEthnicity.PacificIslander
-- sdkbox.PluginFyber.UserEthnicity.White
-- sdkbox.PluginFyber.UserEthnicity.Other
sdkbox.PluginFyber:setEthnicity(ethnicity)
```
>  Sets the user's ethnicity

```lua
sdkbox.PluginFyber:setLocation(latitude, longitude)
```
>  Set the user's location

```lua
sdkbox.PluginFyber:cleanLocation()
```
> Clean the user's location

```lua
-- sdkbox.PluginFyber.UserMaritalStatus.Undefined
-- sdkbox.PluginFyber.UserMartialStatus.Single
-- sdkbox.PluginFyber.UserMartialStatus.Relationship
-- sdkbox.PluginFyber.UserMartialStatus.Married
-- sdkbox.PluginFyber.UserMartialStatus.Divorced
-- sdkbox.PluginFyber.UserMartialStatus.Engaged
sdkbox.PluginFyber:setMaritalStatus(status)
```
>  Sets the user's marital status

```lua
sdkbox.PluginFyber:setNumberOfChildren(numberOfChildren)
```
>  Sets the user's number of children

```lua
sdkbox.PluginFyber:setAnnualHouseholdIncome(income)
```
>  Sets the user's annual household income

```lua
-- sdkbox.PluginFyber.UserEducation.Undefined
-- sdkbox.PluginFyber.UserEducation.Other
-- sdkbox.PluginFyber.UserEducation.None
-- sdkbox.PluginFyber.UserEducation.HighSchool
-- sdkbox.PluginFyber.UserEducation.InCollege
-- sdkbox.PluginFyber.UserEducation.SomeCollege
-- sdkbox.PluginFyber.UserEducation.Associates
-- sdkbox.PluginFyber.UserEducation.Bachelors
-- sdkbox.PluginFyber.UserEducation.Masters
-- sdkbox.PluginFyber.UserEducation.Doctorate
sdkbox.PluginFyber:setEducation(education)
```
>  Sets the user's educational background

```lua
sdkbox.PluginFyber:setZipcode(zipcode)
```
>  Sets the user's zipcode

```lua
sdkbox.PluginFyber:setInterests(interests)
```
>  Set the user's list of interests

```lua
sdkbox.PluginFyber:setIap(flag)
```
>  Sets if in-app purchases are enabled.

```lua
sdkbox.PluginFyber:setIapAmount(amount)
```
>  Sets the amount that the user has already spent on in-app purchases

```lua
sdkbox.PluginFyber:setNumberOfSessions(numberOfSessions)
```
>  Sets the number of sessions

```lua
sdkbox.PluginFyber:setPsTime(timestamp)
```
>  Sets the time spent on the current session

```lua
sdkbox.PluginFyber:setLastSession(session)
```
>  Sets the duration of the last session

```lua
-- sdkbox.PluginFyber.UserConnectionType.Undefined
-- sdkbox.PluginFyber.UserConnectionType.WiFi
-- sdkbox.PluginFyber.UserConnectionType.3G
-- sdkbox.PluginFyber.UserConnectionType.LTE
-- sdkbox.PluginFyber.UserConnectionType.Edge
sdkbox.PluginFyber:setConnectionType(connectionType)
```
>  Sets the connection type used by the user

```lua
-- predefine values
-- sdkbox.PluginFyber.UserDevice.Undefined
-- sdkbox.PluginFyber.UserDevice.IPhone
-- sdkbox.PluginFyber.UserDevice.IPad
-- sdkbox.PluginFyber.UserDevice.IPod
-- sdkbox.PluginFyber.UserDevice.Android
sdkbox.PluginFyber:setDevice(device)
```
>  Sets the device used by the user

```lua
sdkbox.PluginFyber:setVersion(version)
```
>  Sets the app version

```lua
sdkbox.PluginFyber:cleanCustomParameters()
```
> Clean custom parameters, iOS only

```lua
sdkbox.PluginFyber:addCustomParameters(key, value)
```
>  Sets custom parameters to be sent along with the standard parameters


### Listeners
```lua
onVirtualCurrencyConnectorFailed(error, errorCode, errorMsg)
```

```lua
onVirtualCurrencyConnectorSuccess(deltaOfCoins,
                                   currencyId,
                                   currencyName,
                                   transactionId)
```

```lua
onCanShowInterstitial(canShowInterstitial)
```

```lua
onInterstitialDidShow()
```

```lua
onInterstitialDismiss(reason)
```

```lua
onInterstitialFailed()
```

```lua
onBrandEngageClientReceiveOffers(areOffersAvailable)
```

```lua
onBrandEngageClientChangeStatus(status, msg)
```

```lua
onOfferWallFinish(status)
```


