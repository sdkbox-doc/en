## API Reference

### Methods
```lua
sdkbox.PluginInMobi:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginInMobi:setListener(listener)
```
> Set listener to listen for inmobi events

```lua
sdkbox.PluginInMobi:getVersion()
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```lua
sdkbox.PluginInMobi:setLogLevel(desiredLogLevel)
```
> Set the log level for SDK's logs
@param desiredLogLevel The desired level of logs.

```lua
sdkbox.PluginInMobi:addIdForType(identifier, type)
```
> Register a user specific id with the SDK
@param identifier The user Id.
@param type The user Id type.

```lua
sdkbox.PluginInMobi:removeIdType(type)
```
> Deregister a particular set of Ids
@param type The user Id type.

```lua
sdkbox.PluginInMobi:setAge(age)
```
> Provide the user's age to the SDK for targetting purposes.
@param age The user's age.

```lua
sdkbox.PluginInMobi:setAreaCode(areaCode)
```
> Provide the user's area code to the SDK for targetting purposes.
@param areaCode The user's area code.

```lua
sdkbox.PluginInMobi:setAgeGroup(ageGroup)
```
> Provide the user's age group to the SDK for targetting purposes.
@param ageGroup The user's age group.

```lua
sdkbox.PluginInMobi:setYearOfBirth(yearOfBirth)
```
> Provide a user's date of birth to the SDK for targetting purposes.
@param dateOfBirth The user's date of birth.

```lua
sdkbox.PluginInMobi:setEducation(education)
```
> Provide the user's education status to the SDK for targetting purposes.
@param education The user's education status.

```lua
sdkbox.PluginInMobi:setEthnicity(ethnicity)
```
> Provide the user's ethnicity to the SDK for targetting purposes.
@param ethnicity The user's ethnicity.

```lua
sdkbox.PluginInMobi:setGender(gender)
```
> Provide the user's gender to the SDK for targetting purposes.
@param gender The user's gender.

```lua
sdkbox.PluginInMobi:setHouseholdIncome(income)
```
> Provide the user's household income to the SDK for targetting purposes.
@param income The user's household income.

```lua
sdkbox.PluginInMobi:setIncome(income)
```
> Provide the user's income to the SDK for targetting purposes.
@param income The user's income.

```lua
sdkbox.PluginInMobi:setInterests(interests)
```
> Provide the user's interests to the SDK for targetting purposes.
@param interests The user's interests.

```lua
sdkbox.PluginInMobi:setLanguage(language)
```
> Provide the user's preferred language to the SDK for targetting purposes.
@param language The user's language.

```lua
sdkbox.PluginInMobi:setLocation(city, state, country)
```
> Provide the user's location to the SDK for targetting purposes.
@param city The user's city.
@param state The user's state.
@param country The user's country.

```lua
sdkbox.PluginInMobi:setLocation(latitude, longitude)
```
> Provide the user's location to the SDK for targetting purposes.
@param location: The location of the user

```lua
sdkbox.PluginInMobi:setNationality(nationality)
```
> Provide the user's nationality to the SDK for targetting purposes.
@param nationality The user's nationality.

```lua
sdkbox.PluginInMobi:setPostalCode(postalcode)
```
> Provide the user's postal code to the SDK for targetting purposes.
@param postalcode The user's postalcode.

```lua
sdkbox.PluginInMobi:shouldAutoRefresh(refresh)
```
> Control if the banner should auto-refresh ad content.

```lua
sdkbox.PluginInMobi:setRefreshInterval(interval)
```
> Specify the refresh interval for the banner ad.

```lua
sdkbox.PluginInMobi:loadBanner()
```
> Submit a request to load banner ad content.

```lua
sdkbox.PluginInMobi:disableHardwareAccelerationForBanner()
```
> Turn off hardware acceleration on the underlying views.
vaild on android

```lua
sdkbox.PluginInMobi:setBannerAnimationType(animationType)
```
> Set the animation preference on the banner views during ad refresh.

```lua
sdkbox.PluginInMobi:setBannerKeywords(keywords)
```
> Set comma delimited keywords for targeting purpose

```lua
sdkbox.PluginInMobi:loadInterstitial()
```
> Submit a request to load interstitial ad content.

```lua
sdkbox.PluginInMobi:isInterstitialReady()
```
> Returns true if the interstitial was loaded successfully and in ready to be shown.

```lua
sdkbox.PluginInMobi:showInterstitial()
```
> Displays the interstitial on the screen

```lua
sdkbox.PluginInMobi:showInterstitial(type)
```
> Displays the interstitial on the screen
valid on ios

```lua
sdkbox.PluginInMobi:showInterstitial(enterAnimationResourcedId,
                                      exitAnimationResourceId)
```
> Displays the interstitial on the screen
valid on android

```lua
sdkbox.PluginInMobi:disableHardwareAccelerationForInterstitial()
```
> Disable hardware acceleration on the underlying views.
valid on android

```lua
sdkbox.PluginInMobi:setInterstitialKeywords(keywords)
```
> Set comma delimited keywords for targeting purpose


### Listeners
```lua
bannerDidFinishLoading()
```
> Notifies the delegate that the banner has finished loading

```lua
bannerDidFailToLoadWithError(code, description)
```
> Notifies the delegate that the banner has failed to load with some error.

```lua
bannerDidInteractWithParams(params)
```
> Notifies the delegate that the banner was interacted with.

```lua
userWillLeaveApplicationFromBanner()
```
> Notifies the delegate that the user would be taken out of the application context.

```lua
bannerWillPresentScreen()
```
> Notifies the delegate that the banner would be presenting a full screen content.

```lua
bannerDidPresentScreen()
```
> Notifies the delegate that the banner has finished presenting screen.

```lua
bannerWillDismissScreen()
```
> Notifies the delegate that the banner will start dismissing the presented screen.

```lua
bannerDidDismissScreen()
```
> Notifies the delegate that the banner has dismissed the presented screen.

```lua
bannerRewardActionCompletedWithRewards(rewards)
```
> Notifies the delegate that the user has completed the action to be incentivised with.

```lua
interstitialDidFinishLoading()
```
> Notifies the delegate that the interstitial has finished loading

```lua
interstitialDidFailToLoadWithError(code, description)
```
> Notifies the delegate that the interstitial has failed to load with some error.

```lua
interstitialWillPresent()
```
> Notifies the delegate that the interstitial would be presented.

```lua
interstitialDidPresent()
```
> Notifies the delegate that the interstitial has been presented.

```lua
interstitialDidFailToPresentWithError(code, description)
```
> Notifies the delegate that the interstitial has failed to present with some error.

```lua
interstitialWillDismiss()
```
> Notifies the delegate that the interstitial will be dismissed.

```lua
interstitialDidDismiss()
```
> Notifies the delegate that the interstitial has been dismissed.

```lua
interstitialDidInteractWithParams(params)
```
> Notifies the delegate that the interstitial has been interacted with.

```lua
interstitialRewardActionCompletedWithRewards(rewards)
```
> Notifies the delegate that the user has performed the action to be incentivised with.

```lua
userWillLeaveApplicationFromInterstitial()
```
> Notifies the delegate that the user will leave application context.


