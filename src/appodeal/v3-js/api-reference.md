## API Reference

### Methods
```javascript
sdkbox.PluginAppodeal.init(adType);
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginAppodeal.setListener(listener);
```
> Set listener to listen for appodeal events

```javascript
sdkbox.PluginAppodeal.getSDKVersion();
```

```javascript
sdkbox.PluginAppodeal.disableNetworkForAdType(adType, networkName);
```
> deprecated

```javascript
sdkbox.PluginAppodeal.disableLocationPermissionCheck();
```

```javascript
sdkbox.PluginAppodeal.setAutocache(autocache, types);
```

```javascript
sdkbox.PluginAppodeal.isAutocacheEnabled(types);
```

```javascript
sdkbox.PluginAppodeal.confirmUsage(adTypes);
```

```javascript
sdkbox.PluginAppodeal.setDebugEnabled(debugEnabled);
```

```javascript
sdkbox.PluginAppodeal.showAd(style);
```

```javascript
sdkbox.PluginAppodeal.cacheAd(type);
```

```javascript
sdkbox.PluginAppodeal.hideBanner();
```

```javascript
sdkbox.PluginAppodeal.isReadyForShowWithStyle(showStyle);
```

```javascript
sdkbox.PluginAppodeal.setSmartBannersEnabled(smartBannerEnabled);
```

```javascript
sdkbox.PluginAppodeal.setBannerBackgroundVisible(bannerBackgroundVisible);
```

```javascript
sdkbox.PluginAppodeal.setBannerAnimationEnabled(bannerAnimationEnabled);
```

```javascript
sdkbox.PluginAppodeal.setUserVkId(vkId);
```

```javascript
sdkbox.PluginAppodeal.setUserFacebookId(facebookId);
```

```javascript
sdkbox.PluginAppodeal.setUserEmail(email);
```

```javascript
sdkbox.PluginAppodeal.setUserBirthday(birthday);
```

```javascript
sdkbox.PluginAppodeal.setUserAge(age);
```

```javascript
sdkbox.PluginAppodeal.setUserGender(gender);
```

```javascript
sdkbox.PluginAppodeal.setUserOccupation(occupation);
```

```javascript
sdkbox.PluginAppodeal.setUserRelationship(relationship);
```

```javascript
sdkbox.PluginAppodeal.setUserSmokingAttitude(smokingAttitude);
```

```javascript
sdkbox.PluginAppodeal.setUserAlcoholAttitude(alcoholAttitude);
```

```javascript
sdkbox.PluginAppodeal.setUserInterests(interests);
```


### Listeners
```javascript
onBannerDidLoadAd();
```
> trigger when banner ad load

```javascript
onBannerDidFailToLoadAd();
```
> trigger when banner ad fail to load

```javascript
onBannerDidClick();
```
> trigger when banner ad clicked

```javascript
onBannerPresent();
```
> trigger when banner ad present

```javascript
onInterstitialDidLoadAd();
```
> trigger when interstitial ad load

```javascript
onInterstitialDidFailToLoadAd();
```
> trigger when interstitial ad fail to load

```javascript
onInterstitialWillPresent();
```
> trigger when interstitial ad present

```javascript
onInterstitialDidDismiss();
```
> trigger when interstitial dismiss

```javascript
onInterstitialDidClick();
```
> trigger when interstitial ad clicked

```javascript
onInterstitialDidFailToPresent();
```
> trigger when interstitial ad fail to present

```javascript
onVideoDidLoadAd();
```
> trigger when video load
deprecated

```javascript
onVideoDidFailToLoadAd();
```
> trigger when video fail to load
deprecated

```javascript
onVideoDidPresent();
```
> trigger when video present
deprecated

```javascript
onVideoWillDismiss();
```
> trigger when video dismiss
deprecated

```javascript
onVideoDidFinish();
```
> trigger when video finish
deprecated

```javascript
onRewardVideoDidLoadAd();
```
> trigger when reward video load

```javascript
onRewardVideoDidFailToLoadAd();
```
> trigger when reward video fail to load

```javascript
onRewardVideoDidPresent();
```
> trigger when reward video present

```javascript
onRewardVideoWillDismiss();
```
> trigger when reward video dismiss

```javascript
onRewardVideoDidFinish(amount, name);
```
> trigger when reward video finish

```javascript
onRewardVideoDidFailToPresent();
```
> trigger when reward video fail to present

```javascript
onSkippableVideoDidLoadAd();
```
> trigger when skippable video load

```javascript
onSkippableVideoDidFailToLoadAd();
```
> trigger when skippable video fial to load

```javascript
onSkippableVideoDidPresent();
```
> trigger when skippable video present

```javascript
onSkippableVideoWillDismiss();
```
> trigger when skippable video dismiss

```javascript
onSkippableVideoDidFinish();
```
> trigger when skippable video finish

```javascript
onSkippableVideoDidClick();
```
> trigger when skippable video click

```javascript
onNonSkippableVideoDidLoadAd();
```
> trigger when nonskippable video load

```javascript
onNonSkippableVideoDidFailToLoadAd();
```
> trigger when nonskippable video fial to load

```javascript
onNonSkippableVideoDidPresent();
```
> trigger when nonskippable video present

```javascript
onNonSkippableVideoWillDismiss();
```
> trigger when nonskippable video dismiss

```javascript
onNonSkippableVideoDidFinish();
```
> trigger when nonskippable video finish

```javascript
onNonSkippableVideoDidClick();
```
> trigger when nonskippable video click

```javascript
onNonSkippableVideoDidFailToPresent();
```
> trigger when nonskippable video fail to present


