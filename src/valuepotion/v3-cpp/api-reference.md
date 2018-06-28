## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( ValuePotionListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static ValuePotionListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void setTest ( bool isTest ) ;
```
> for intergation test

```cpp
static bool hasCachedInterstitial ( const char * placement ) ;
```
> check if ad is cached

```cpp
static void cacheInterstitial ( const char * placement ) ;
```
> cached ad

```cpp
static void openInterstitial ( const char * placement ) ;
```
> show ad

```cpp
static void trackEvent ( const char * eventName ) ;
```
> track game event

```cpp
static void trackEvent ( const char * eventName , double eventValue ) ;
```

```cpp
static void trackEvent ( const char * category ,
                         const char * eventName ,
                         const char * label ,
                         double eventValue ) ;
```

```cpp
static void trackPurchaseEvent ( const char * eventName ,
                                 double revenueAmount ,
                                 const char * currency ,
                                 const char * orderId ,
                                 const char * productId ) ;
```
> track purchase event

```cpp
static void trackPurchaseEvent ( const char * eventName ,
                                 double revenueAmount ,
                                 const char * currency ,
                                 const char * orderId ,
                                 const char * productId ,
                                 const char * campaignId ,
                                 const char * contentId ) ;
```

```cpp
static void trackPurchaseEvent ( const char * category ,
                                 const char * eventName ,
                                 const char * label ,
                                 double revenueAmount ,
                                 const char * currency ,
                                 const char * orderId ,
                                 const char * productId ,
                                 const char * campaignId ,
                                 const char * contentId ) ;
```

```cpp
static void userinfo ( const char * attribute , const char * value ) ;
```
> set user info

<pre>
Field              Description
userId             User account id used in game
serverId           If you need to distinguish users by server which they belong to, you should set serverId. Then you can get statistics based on serverId.
birth              Date of birth in YYYYMMDD. If you know only year of birth, fill last four digits with "0" like "19840000". If you know only date of birth(but not year), fill first four digits with "0" like "00001109".
gender             "M" for male, "F" for female.
level              Level of user in game.
friends            Number of user's friends.
accountType        Type of user's account type. (facebook, google, guest, etc)
</pre>


### Listeners
```cpp
void onCacheInterstitial ( const char * placement ) 
```

```cpp
void onFailToCacheInterstitial ( const char * placement ,
                                 const char * errorMessage ) 
```

```cpp
void onOpenInterstitial ( const char * placement ) 
```

```cpp
void onFailToOpenInterstitial ( const char * placement ,
                                const char * errorMessage ) 
```

```cpp
void onCloseInterstitial ( const char * placement ) 
```

```cpp
void onRequestOpenURL ( const char * placement , const char * URL ) 
```

```cpp
void onRequestPurchase ( const char * placement ,
                         const char * name ,
                         const char * productId ,
                         int quantity ,
                         const char * campaignId ,
                         const char * contentId ) 
```

```cpp
void onRequestRewards ( const char * placement ,
                        std::vector <ValuePotionReward> rewards ) 
```


