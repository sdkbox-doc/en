## API Reference

### Methods
```lua
sdkbox.PluginFyber:init(userID, jsonconfig)
```
> initialize the fyber plugin.

```lua
sdkbox.PluginFyber:showOfferWall(placementId)
```
> Presents the Fyber Mobile OfferWall as a child view controller of your own view controller.

<pre>
@placementId (deprecated)
</pre>

```lua
sdkbox.PluginFyber:requestOffers(placementId)
```
> Request the server for rewarded video availability.

```lua
sdkbox.PluginFyber:showOffers(placementId)
```
> Show an available rewarded video.

<pre>
@placementId (deprecated)
</pre>

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

<pre>
 @param age Age of the user. Pass `FYBEntryIgnore` if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setBirthdate(data)
```
>  Sets the user's date of birth, format (yyyy-MM-dd)

<pre>
 @param date Date of birth of the user. Pass `""` if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setGender(gender)
```
>  Sets the user's gender

<pre>
 @param gender Gender of the user. Pass FYB_UserGenderUndefined if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setSexualOrientation(sexualOrientation)
```
>  Sets the user's sexual orientation

<pre>
 @param sexualOrientation Sexual orientation of the user. Pass FYB_UserSexualOrientationUndefined if value needs to be ignored or to be removed, if already exists.
</pre>

```lua
sdkbox.PluginFyber:setEthnicity(ethnicity)
```
>  Sets the user's ethnicity

<pre>
 @param ethnicity Ethnicity of the user. Pass FYB_UserEthnicityUndefined if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setLocation(latitude, longitude)
```
>  Set the user's location

```lua
sdkbox.PluginFyber:cleanLocation()
```
> Clean the user's location

```lua
sdkbox.PluginFyber:setMaritalStatus(status)
```
>  Sets the user's marital status

<pre>
 @param status Marital status of the user. Pass FYB_UserMaritalStatusUndefined if value needs to be ignored or to be removed if already exists
</pre>

```lua
sdkbox.PluginFyber:setNumberOfChildren(numberOfChildren)
```
>  Sets the user's number of children

<pre>
 @param numberOfChildren The number of children
</pre>

```lua
sdkbox.PluginFyber:setAnnualHouseholdIncome(income)
```
>  Sets the user's annual household income

<pre>
 @param income Annual household income of the user. Pass `FYB_EntryIgnore` if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setEducation(education)
```
>  Sets the user's educational background

<pre>
 @param education Education of the user. Pass FYB_UserEducationUndefined if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setZipcode(zipcode)
```
>  Sets the user's zipcode

<pre>
 @param zipcode Zipcode of the current living place of the user. Pass `""` if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setInterests(interests)
```
>  Set the user's list of interests

<pre>
 @param interests List of interests of the user. Pass `{}` if value needs to be ignored or to be removed, if already exists
</pre>

```lua
sdkbox.PluginFyber:setIap(flag)
```
>  Sets if in-app purchases are enabled.

<pre>
 @param flag Sets if in-app purchases are enabled
</pre>

```lua
sdkbox.PluginFyber:setIapAmount(amount)
```
>  Sets the amount that the user has already spent on in-app purchases

<pre>
 @param amount The amount of money that the user has spent
</pre>

```lua
sdkbox.PluginFyber:setNumberOfSessions(numberOfSessions)
```
>  Sets the number of sessions

<pre>
 @param numberOfSessions The number of sessions that has already been started
</pre>

```lua
sdkbox.PluginFyber:setPsTime(timestamp)
```
>  Sets the time spent on the current session

<pre>
 @param timestamp The time spent on the current session
</pre>

```lua
sdkbox.PluginFyber:setLastSession(session)
```
>  Sets the duration of the last session

<pre>
 @param session The duration of the last session
</pre>

```lua
sdkbox.PluginFyber:setConnectionType(connectionType)
```
>  Sets the connection type used by the user

<pre>
 @param connectionType The connection type used by the user
</pre>

```lua
sdkbox.PluginFyber:setDevice(device)
```
>  Sets the device used by the user

<pre>
 @param device The device used by the user
</pre>

```lua
sdkbox.PluginFyber:setVersion(version)
```
>  Sets the app version

<pre>
 @param version The version of the app currently executed
</pre>

```lua
sdkbox.PluginFyber:cleanCustomParameters()
```
> Clean custom parameters, iOS only

```lua
sdkbox.PluginFyber:addCustomParameters(key, value)
```
>  Sets custom parameters to be sent along with the standard parameters

<pre>
 @param parameters The custom parameters that must be set
</pre>


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


