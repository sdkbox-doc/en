## API Reference

### Methods
```javascript
sdkbox.PluginAppodeal.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginAppodeal.setListener(listener);
```
> Set listener to listen for Appodeal events

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
onVideoDidLoadAd();
```
> trigger when video load

```javascript
onVideoDidFailToLoadAd();
```
> trigger when video fail to load

```javascript
onVideoDidPresent();
```
> trigger when video present

```javascript
onVideoWillDismiss();
```
> trigger when video dismiss

```javascript
onVideoDidFinish();
```
> trigger when video finish
