## API Reference

### Methods
```cpp
static bool init ( AdType adType = AdType::AppodealAdTypeAll ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( AppodealListener * listener ) ;
```
> Set listener to listen for appodeal events

```cpp
static AppodealListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static std::string getSDKVersion ( ) ;
```

```cpp
static void disableNetworkForAdType ( AdType adType ,
                                      const std::string & networkName ) ;
```
> deprecated

```cpp
static void disableLocationPermissionCheck ( ) ;
```

```cpp
static void setAutocache ( bool autocache , AdType types ) ;
```

```cpp
static bool isAutocacheEnabled ( AdType types ) ;
```

```cpp
static void confirmUsage ( AdType adTypes ) ;
```

```cpp
static void setDebugEnabled ( bool debugEnabled ) ;
```

```cpp
static bool showAd ( ShowStyle style ) ;
```

```cpp
static void cacheAd ( AdType type ) ;
```

```cpp
static void hideBanner ( ) ;
```

```cpp
static bool isReadyForShowWithStyle ( ShowStyle showStyle ) ;
```

```cpp
static void setSmartBannersEnabled ( bool smartBannerEnabled ) ;
```

```cpp
static void setBannerBackgroundVisible ( bool bannerBackgroundVisible ) ;
```

```cpp
static void setBannerAnimationEnabled ( bool bannerAnimationEnabled ) ;
```

```cpp
static void setUserVkId ( const std::string & vkId ) ;
```

```cpp
static void setUserFacebookId ( const std::string & facebookId ) ;
```

```cpp
static void setUserEmail ( const std::string & email ) ;
```

```cpp
static void setUserBirthday ( const std::string & birthday ) ;
```

```cpp
static void setUserAge ( int age ) ;
```

```cpp
static void setUserGender ( Gender gender ) ;
```

```cpp
static void setUserOccupation ( Occupation occupation ) ;
```

```cpp
static void setUserRelationship ( Relationship relationship ) ;
```

```cpp
static void setUserSmokingAttitude ( SmokingAttitude smokingAttitude ) ;
```

```cpp
static void setUserAlcoholAttitude ( AlcoholAttitude alcoholAttitude ) ;
```

```cpp
static void setUserInterests ( const std::string & interests ) ;
```


### Listeners
```cpp
void onBannerDidLoadAd ( ) 
```
> trigger when banner ad load

```cpp
void onBannerDidFailToLoadAd ( ) 
```
> trigger when banner ad fail to load

```cpp
void onBannerDidClick ( ) 
```
> trigger when banner ad clicked

```cpp
void onBannerPresent ( ) 
```
> trigger when banner ad present

```cpp
void onInterstitialDidLoadAd ( ) 
```
> trigger when interstitial ad load

```cpp
void onInterstitialDidFailToLoadAd ( ) 
```
> trigger when interstitial ad fail to load

```cpp
void onInterstitialWillPresent ( ) 
```
> trigger when interstitial ad present

```cpp
void onInterstitialDidDismiss ( ) 
```
> trigger when interstitial dismiss

```cpp
void onInterstitialDidClick ( ) 
```
> trigger when interstitial ad clicked

```cpp
void onInterstitialDidFailToPresent ( ) 
```
> trigger when interstitial ad fail to present

```cpp
void onVideoDidLoadAd ( ) 
```
> trigger when video load
deprecated

```cpp
void onVideoDidFailToLoadAd ( ) 
```
> trigger when video fail to load
deprecated

```cpp
void onVideoDidPresent ( ) 
```
> trigger when video present
deprecated

```cpp
void onVideoWillDismiss ( ) 
```
> trigger when video dismiss
deprecated

```cpp
void onVideoDidFinish ( ) 
```
> trigger when video finish
deprecated

```cpp
void onRewardVideoDidLoadAd ( ) 
```
> trigger when reward video load

```cpp
void onRewardVideoDidFailToLoadAd ( ) 
```
> trigger when reward video fail to load

```cpp
void onRewardVideoDidPresent ( ) 
```
> trigger when reward video present

```cpp
void onRewardVideoWillDismiss ( ) 
```
> trigger when reward video dismiss

```cpp
void onRewardVideoDidFinish ( int amount , const std::string & name ) 
```
> trigger when reward video finish

```cpp
void onRewardVideoDidFailToPresent ( ) 
```
> trigger when reward video fail to present

```cpp
void onSkippableVideoDidLoadAd ( ) 
```
> trigger when skippable video load

```cpp
void onSkippableVideoDidFailToLoadAd ( ) 
```
> trigger when skippable video fial to load

```cpp
void onSkippableVideoDidPresent ( ) 
```
> trigger when skippable video present

```cpp
void onSkippableVideoWillDismiss ( ) 
```
> trigger when skippable video dismiss

```cpp
void onSkippableVideoDidFinish ( ) 
```
> trigger when skippable video finish

```cpp
void onSkippableVideoDidClick ( ) 
```
> trigger when skippable video click

```cpp
void onNonSkippableVideoDidLoadAd ( ) 
```
> trigger when nonskippable video load

```cpp
void onNonSkippableVideoDidFailToLoadAd ( ) 
```
> trigger when nonskippable video fial to load

```cpp
void onNonSkippableVideoDidPresent ( ) 
```
> trigger when nonskippable video present

```cpp
void onNonSkippableVideoWillDismiss ( ) 
```
> trigger when nonskippable video dismiss

```cpp
void onNonSkippableVideoDidFinish ( ) 
```
> trigger when nonskippable video finish

```cpp
void onNonSkippableVideoDidClick ( ) 
```
> trigger when nonskippable video click

```cpp
void onNonSkippableVideoDidFailToPresent ( ) 
```
> trigger when nonskippable video fail to present


