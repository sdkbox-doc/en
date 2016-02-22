## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( LeadBoltListener * listener ) ;
```
> Set listener to listen for leadbolt events

```cpp
static LeadBoltListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void startSession ( const std::string & apiKey ) ;
```
> start session

```cpp
static void closeSession ( ) ;
```
> close session

```cpp
static void setSyncDataPeriodInSecond ( int periodInSecond ) ;
```
> sync data second, just valid on ios

```cpp
static void sync ( ) ;
```
> sync data

```cpp
static void event ( const std::string & name ) ;
```

```cpp
static void event ( const std::string & name , float floatValue ) ;
```

```cpp
static void transaction ( const std::string & name ,
                          float floatValue ,
                          const std::string & currencyCode ) ;
```

```cpp
static void transaction ( const std::string & name ,
                          float floatValue ,
                          const std::string & currencyCode ,
                          bool instant ) ;
```

```cpp
static void transaction ( const std::string & name ,
                          float floatValue ,
                          const std::string & currencyCode ,
                          const std::string & ref ) ;
```

```cpp
static void transaction ( const std::string & name ,
                          float floatValue ,
                          const std::string & currencyCode ,
                          const std::string & ref ,
                          bool instant ) ;
```

```cpp
static void loadModule ( const std::string & placement ) ;
```

```cpp
static void loadModule ( const std::string & placement ,
                         const std::string & userData ) ;
```

```cpp
static void loadModuleToCache ( const std::string & placement ) ;
```

```cpp
static void loadModuleToCache ( const std::string & placement ,
                                const std::string & userData ) ;
```

```cpp
static void destroyModule ( ) ;
```

```cpp
static void setCrashHandlerStatus ( bool enable ) ;
```

```cpp
static void crashWithName ( const std::string & crashName ,
                            const std::string & description ) ;
```

```cpp
static void fixAdOrientation ( AdOrientation orientation ) ;
```

```cpp
static bool isAdReady ( const std::string & placement ) ;
```

```cpp
static void setAgeRange ( const std::string & range ) ;
```

```cpp
static void setGender ( const std::string & gender ) ;
```

```cpp
static void setFramework ( const std::string & f ) ;
```


### Listeners
```cpp
void onModuleLoaded ( const std::string & placement ) {
```
> Notifies the delegate that the module has finished loading

```cpp
void onModuleClosed ( const std::string & placement ) {
```
> Notifies the delegate that the module has closed

```cpp
void onModuleClicked ( const std::string & placement ) {
```
> Notifies the delegate that the module has clicked

```cpp
void onModuleCached ( const std::string & placement ) {
```
> Notifies the delegate that the module has cached

```cpp
void onModuleFailed ( const std::string & placement ,
                      const std::string & error ,
                      bool iscached ) {
```
> Notifies the delegate that the module has fail

```cpp
void onMediaFinished ( bool viewCompleted ) {
```
> Notifies the delegate that the module has finished
