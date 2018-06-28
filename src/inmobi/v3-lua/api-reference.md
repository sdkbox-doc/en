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

```lua
sdkbox.PluginInMobi:addIdForType(identifier, type)
```
> Register a user specific id with the SDK

```lua
sdkbox.PluginInMobi:removeIdType(type)
```
> Deregister a particular set of Ids

```lua
sdkbox.PluginInMobi:setAge(age)
```
> Provide the user's age to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setAreaCode(areaCode)
```
> Provide the user's area code to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setAgeGroup(ageGroup)
```
> Provide the user's age group to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setYearOfBirth(yearOfBirth)
```
> Provide a user's date of birth to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setEducation(education)
```
> Provide the user's education status to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setEthnicity(ethnicity)
```
> Provide the user's ethnicity to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setGender(gender)
```
> Provide the user's gender to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setHouseholdIncome(income)
```
> Provide the user's household income to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setIncome(income)
```
> Provide the user's income to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setInterests(interests)
```
> Provide the user's interests to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setLanguage(language)
```
> Provide the user's preferred language to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setLocation(city, state, country)
```
> Provide the user's location to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setLocation(latitude, longitude)
```
> Provide the user's location to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setNationality(nationality)
```
> Provide the user's nationality to the SDK for targeting purposes.

```lua
sdkbox.PluginInMobi:setPostalCode(postalcode)
```
> Provide the user's postal code to the SDK for targeting purposes.

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
sdkbox.PluginInMobi:hideBanner()
```
> Hide Banner

```lua
sdkbox.PluginInMobi:loadInterstitial(ad)
```
> Submit a request to load interstitial ad content.

```lua
sdkbox.PluginInMobi:isInterstitialReady(ad)
```
> Returns true if the interstitial was loaded successfully and in ready to be shown.

```lua
sdkbox.PluginInMobi:showInterstitial(ad)
```
> Displays the interstitial on the screen

```lua
sdkbox.PluginInMobi:showInterstitial(type, ad)
```
> Displays the interstitial on the screen
valid on ios

```lua
sdkbox.PluginInMobi:showInterstitial(enterAnimationResourcedId,
                                      exitAnimationResourceId,
                                      ad)
```
> Displays the interstitial on the screen
valid on android

```lua
sdkbox.PluginInMobi:disableHardwareAccelerationForInterstitial(ad)
```
> Disable hardware acceleration on the underlying views.
valid on android

```lua
sdkbox.PluginInMobi:setInterstitialKeywords(keywords, ad)
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


