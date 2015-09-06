## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( FyberListener * listener ) ;
```
> Set listener to listen for fyber events

```cpp
static FyberListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void showOfferWall ( const std::string & placementId = "" ) ;
```
> Presents the SponsorPay Mobile OfferWall as a child view controller of your own view controller.

```cpp
static void requestOffers ( const std::string & placementId = "" ) ;
```
> Queries the server for BrandEngage offers availability.

```cpp
static void showOffers ( ) ;
```
> Starts running an available engagement.

```cpp
static void requestInterstitial ( ) ;
```
> Check if interstitial ads are available

```cpp
static void showInterstitial ( ) ;
```
> Shows an interstitial ad. Check first that one is ready to be shown with requestInterstitial.

```cpp
static void requestDeltaOfCoins ( const std::string & currencyId = "" ) ;
```
> Fetches the amount of a given currency earned since the last time this method was
invoked for the current user ID / app ID combination.


### Listeners
```cpp
void onVirtualCurrencyConnectorFailed ( int error ,
                                        const std::string & errorCode ,
                                        const std::string & errorMsg );
```

```cpp
void onVirtualCurrencyConnectorSuccess ( double deltaOfCoins ,
                                         const std::string & currencyId ,
                                         const std::string & currencyName ,
                                         const std::string & transactionId );
```

```cpp
void onCanShowInterstitial ( bool canShowInterstitial );
```

```cpp
void onInterstitialDidShow ( );
```

```cpp
void onInterstitialDismiss ( const std::string & reason );
```

```cpp
void onInterstitialFailed ( );
```

```cpp
void onBrandEngageClientReceiveOffers ( bool areOffersAvailable );
```

```cpp
void onBrandEngageClientChangeStatus ( int status , const std::string & msg );
```

```cpp
void onOfferWallFinish ( int status );
```


