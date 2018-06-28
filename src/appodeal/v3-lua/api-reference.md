## API Reference

### Methods
```lua
sdkbox.PluginAppodeal:init(adType)
```
>  initialize the plugin instance.

```lua
sdkbox.PluginAppodeal:setListener(listener)
```
> Set listener to listen for appodeal events

```lua
sdkbox.PluginAppodeal:getSDKVersion()
```

```lua
sdkbox.PluginAppodeal:disableNetworkForAdType(adType, networkName)
```
> deprecated

```lua
sdkbox.PluginAppodeal:disableLocationPermissionCheck()
```

```lua
sdkbox.PluginAppodeal:setAutocache(autocache, types)
```

```lua
sdkbox.PluginAppodeal:isAutocacheEnabled(types)
```

```lua
sdkbox.PluginAppodeal:confirmUsage(adTypes)
```

```lua
sdkbox.PluginAppodeal:setDebugEnabled(debugEnabled)
```

```lua
sdkbox.PluginAppodeal:showAd(style)
```

```lua
sdkbox.PluginAppodeal:cacheAd(type)
```

```lua
sdkbox.PluginAppodeal:hideBanner()
```

```lua
sdkbox.PluginAppodeal:isReadyForShowWithStyle(showStyle)
```

```lua
sdkbox.PluginAppodeal:setSmartBannersEnabled(smartBannerEnabled)
```

```lua
sdkbox.PluginAppodeal:setBannerBackgroundVisible(bannerBackgroundVisible)
```

```lua
sdkbox.PluginAppodeal:setBannerAnimationEnabled(bannerAnimationEnabled)
```

```lua
sdkbox.PluginAppodeal:setUserVkId(vkId)
```

```lua
sdkbox.PluginAppodeal:setUserFacebookId(facebookId)
```

```lua
sdkbox.PluginAppodeal:setUserEmail(email)
```

```lua
sdkbox.PluginAppodeal:setUserBirthday(birthday)
```

```lua
sdkbox.PluginAppodeal:setUserAge(age)
```

```lua
sdkbox.PluginAppodeal:setUserGender(gender)
```

```lua
sdkbox.PluginAppodeal:setUserOccupation(occupation)
```

```lua
sdkbox.PluginAppodeal:setUserRelationship(relationship)
```

```lua
sdkbox.PluginAppodeal:setUserSmokingAttitude(smokingAttitude)
```

```lua
sdkbox.PluginAppodeal:setUserAlcoholAttitude(alcoholAttitude)
```

```lua
sdkbox.PluginAppodeal:setUserInterests(interests)
```


### Listeners
```lua
onBannerDidLoadAd()
```
> trigger when banner ad load

```lua
onBannerDidFailToLoadAd()
```
> trigger when banner ad fail to load

```lua
onBannerDidClick()
```
> trigger when banner ad clicked

```lua
onBannerPresent()
```
> trigger when banner ad present

```lua
onInterstitialDidLoadAd()
```
> trigger when interstitial ad load

```lua
onInterstitialDidFailToLoadAd()
```
> trigger when interstitial ad fail to load

```lua
onInterstitialWillPresent()
```
> trigger when interstitial ad present

```lua
onInterstitialDidDismiss()
```
> trigger when interstitial dismiss

```lua
onInterstitialDidClick()
```
> trigger when interstitial ad clicked

```lua
onInterstitialDidFailToPresent()
```
> trigger when interstitial ad fail to present

```lua
onVideoDidLoadAd()
```
> trigger when video load
deprecated

```lua
onVideoDidFailToLoadAd()
```
> trigger when video fail to load
deprecated

```lua
onVideoDidPresent()
```
> trigger when video present
deprecated

```lua
onVideoWillDismiss()
```
> trigger when video dismiss
deprecated

```lua
onVideoDidFinish()
```
> trigger when video finish
deprecated

```lua
onRewardVideoDidLoadAd()
```
> trigger when reward video load

```lua
onRewardVideoDidFailToLoadAd()
```
> trigger when reward video fail to load

```lua
onRewardVideoDidPresent()
```
> trigger when reward video present

```lua
onRewardVideoWillDismiss()
```
> trigger when reward video dismiss

```lua
onRewardVideoDidFinish(amount, name)
```
> trigger when reward video finish

```lua
onRewardVideoDidFailToPresent()
```
> trigger when reward video fail to present

```lua
onSkippableVideoDidLoadAd()
```
> trigger when skippable video load

```lua
onSkippableVideoDidFailToLoadAd()
```
> trigger when skippable video fial to load

```lua
onSkippableVideoDidPresent()
```
> trigger when skippable video present

```lua
onSkippableVideoWillDismiss()
```
> trigger when skippable video dismiss

```lua
onSkippableVideoDidFinish()
```
> trigger when skippable video finish

```lua
onSkippableVideoDidClick()
```
> trigger when skippable video click

```lua
onNonSkippableVideoDidLoadAd()
```
> trigger when nonskippable video load

```lua
onNonSkippableVideoDidFailToLoadAd()
```
> trigger when nonskippable video fial to load

```lua
onNonSkippableVideoDidPresent()
```
> trigger when nonskippable video present

```lua
onNonSkippableVideoWillDismiss()
```
> trigger when nonskippable video dismiss

```lua
onNonSkippableVideoDidFinish()
```
> trigger when nonskippable video finish

```lua
onNonSkippableVideoDidClick()
```
> trigger when nonskippable video click

```lua
onNonSkippableVideoDidFailToPresent()
```
> trigger when nonskippable video fail to present


