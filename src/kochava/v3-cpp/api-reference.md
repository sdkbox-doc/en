## API Reference

### Methods
```cpp
static void init ( ) ;
```
> init the kochava service

```cpp
static void shutdown ( ) ;
```
> shutdown the kochava service

```cpp
static void enableLogging ( bool enabled ) ;
```
> enable kochava api logging

```cpp
static void trackEvent ( const char * event , const char * value ) ;
```
> track a single event

```cpp
static void spatialEvent ( const char * title , float x , float y , float z ) ;
```
> spatial event to help visualize data

```cpp
static void setLimitAdTracking ( bool limitAdTracking ) ;
```
> turn on/off ad tracking

```cpp
static const std::map <std::string , std::string> * retrieveAttribution ( ) ;
```
> returns the attribution data

```cpp
static void sendDeepLink ( const char * url , const char * application ) ;
```
> send a referral to where your app was opened from.

```cpp
static void setAttributionCallback ( kochavaCallbackDict callback ) ;
```
> specify callback for attribution

```cpp
static void setBeaconCallback ( kochavaCallbackString callback ) ;
```
> specify beacon transition callback


### Listeners

