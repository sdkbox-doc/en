## API Reference

### Methods
```lua
sdkbox.PluginAppodeal:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginAppodeal:setListener(listener)
```
> Set listener to listen for Appodeal events

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
onVideoDidLoadAd()
```
> trigger when video load

```lua
onVideoDidFailToLoadAd()
```
> trigger when video fail to load

```lua
onVideoDidPresent()
```
> trigger when video present

```lua
onVideoWillDismiss()
```
> trigger when video dismiss

```lua
onVideoDidFinish()
```
> trigger when video finish
