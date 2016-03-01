## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( AdMobListener * listener ) ;
```
> Set listener to listen for admob events

```cpp
static AdMobListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static std::string getVersion ( ) ;
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```cpp
static void setTestDevices ( const std::string & devices ) ;
```
> Set test devices

```cpp
static void cache ( const std::string & name ) ;
```
> Cache ad with @name

```cpp
static void show ( const std::string & name ) ;
```
> show ad with @name

```cpp
static void hide ( const std::string & name ) ;
```
> hide ad with @name

```cpp
static bool isAvailable ( const std::string & name ) ;
```
> check whether ad available with @name

```cpp
static int getCurrBannerWidth ( ) ;
```
> get width of current banner

```cpp
static int getCurrBannerHeight ( ) ;
```
> get height of current banner


### Listeners
```cpp
void adViewDidReceiveAd ( const std::string & name ) {
```

```cpp
void adViewDidFailToReceiveAdWithError ( const std::string & name ,
                                         const std::string & msg ) {
```

```cpp
void adViewWillPresentScreen ( const std::string & name ) {
```

```cpp
void adViewDidDismissScreen ( const std::string & name ) {
```

```cpp
void adViewWillDismissScreen ( const std::string & name ) {
```

```cpp
void adViewWillLeaveApplication ( const std::string & name ) {
```


