## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( AppnextListener * listener ) ;
```
> Set listener to listen for appnext events

```cpp
static AppnextListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void hideAd ( ) ;
```
> Hide advertisement

```cpp
static void showAd ( ) ;
```
> Show advertisement

```cpp
static void refreshAds ( ) ;
```
> Refresh advertisement

```cpp
static void cacheAd ( const std::string & name ) ;
```
> Cache advertisement

```cpp
static bool isAdReady ( ) ;
```
> Check if advertisement is ready

```cpp
static void cacheVideo ( const std::string & name ) ;
```
> Cache video with @name

```cpp
static void showVideo ( const std::string & name ) ;
```
> show video with @name

```cpp
static void refreshVideo ( const std::string & name ) ;
```
> Refresh video with @name

```cpp
static bool isVideoReady ( const std::string & name ) ;
```
> Check if video is ready with @name

```cpp
static void setRewardsTransactionId ( const std::string & transactionId ) ;
```
> Set reward video transaction id

```cpp
static void setRewardsUserId ( const std::string & userId ) ;
```
> Set reward video user id

```cpp
static void setRewardsRewardTypeCurrency ( const std::string & currency ) ;
```
> Set type of reward, such as life / credit / points.

```cpp
static void setRewardsAmountRewarded ( const std::string & amount ) ;
```
> Set the amount of currency that was rewarded.

```cpp
static void setRewardsCustomParameter ( const std::string & parameter ) ;
```
> Set reward video custom parameter.


### Listeners
```cpp
void onAdError ( const std::string & msg )
```

```cpp
void onAdLoaded ( )
```

```cpp
void onAdOpened ( )
```

```cpp
void onAdClosed ( )
```

```cpp
void onAdClicked ( )
```

```cpp
void onVideoLoaded ( const std::string & name )
```

```cpp
void onVideoClicked ( const std::string & name )
```

```cpp
void onVideoClosed ( const std::string & name )
```

```cpp
void onVideoEnded ( const std::string & name )
```

```cpp
void onVideoError ( const std::string & name , const std::string & msg )
```


