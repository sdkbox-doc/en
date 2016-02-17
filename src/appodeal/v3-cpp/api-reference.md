## API Reference

### Methods
```cpp
static bool init ( ) ;
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
static void disableNetworkForAdType ( AdType adType ,
                                      const std::string & networkName ) ;
```

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
void onBannerDidLoadAd ( );
```
> trigger when banner ad load

```cpp
void onBannerDidFailToLoadAd ( );
```
> trigger when banner ad fail to load

```cpp
void onBannerDidClick ( );
```
> trigger when banner ad clicked

```cpp
void onBannerPresent ( );
```
> trigger when banner ad present

```cpp
void onInterstitialDidLoadAd ( );
```
> trigger when interstitial ad load

```cpp
void onInterstitialDidFailToLoadAd ( );
```
> trigger when interstitial ad fail to load

```cpp
void onInterstitialWillPresent ( );
```
> trigger when interstitial ad present

```cpp
void onInterstitialDidDismiss ( );
```
> trigger when interstitial dismiss

```cpp
void onInterstitialDidClick ( );
```
> trigger when interstitial ad clicked

```cpp
void onVideoDidLoadAd ( );
```
> trigger when video load

```cpp
void onVideoDidFailToLoadAd ( );
```
> trigger when video fail to load

```cpp
void onVideoDidPresent ( );
```
> trigger when video present

```cpp
void onVideoWillDismiss ( );
```
> trigger when video dismiss

```cpp
void onVideoDidFinish ( );
```
> trigger when video finish

```cpp
void onRewardVideoDidLoadAd ( );
```
> trigger when reward video load

```cpp
void onRewardVideoDidFailToLoadAd ( );
```
> trigger when reward video fail to load

```cpp
void onRewardVideoDidPresent ( );
```
> trigger when reward video present

```cpp
void onRewardVideoWillDismiss ( );
```
> trigger when reward video dismiss

```cpp
void onRewardVideoDidFinish ( int amount , const std::string & name );
```
> trigger when reward video finish


