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
static void loadModuleToCache ( const std::string & placement ,
                                const std::string & userData = "" ) ;
```
> Cache Ad with name @placement (referenced from your json config file)

```cpp
static bool isAdReady ( const std::string & placement ) ;
```
> Check if Ad with name @placement (referenced from your json config file) is available for display

```cpp
static void loadModule ( const std::string & placement ,
                         const std::string & userData = "" ) ;
```
> Load/Display Ad with name @placement (referenced from your json config file)

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
> event

```cpp
static void event ( const std::string & name , float floatValue ) ;
```
> event with float value

```cpp
static void transaction ( const std::string & name ,
                          float floatValue ,
                          const std::string & currencyCode ,
                          const std::string & ref = "" ,
                          bool instant = false ) ;
```
> Transaction Events

```cpp
static void destroyModule ( ) ;
```
> destroy module

```cpp
static void setCrashHandlerStatus ( bool enable ) ;
```
> Crash Reporting

```cpp
static void crashWithName ( const std::string & crashName ,
                            const std::string & description ) ;
```
> Crash Reporting

```cpp
static void fixAdOrientation ( AdOrientation orientation ) ;
```
> force Ad Orientation

```cpp
static void setAgeRange ( const std::string & range ) ;
```
> setAgeRange
You can increase your App's performance by optionally including the additional information above. This allows selected premium advertisers to display their Ads to your users. To pass this additional information, use the following methods BEFORE calling loadModuleToCache.
accepted values "13-17", "18-25", "26-35", "36-45", "46+"

```cpp
static void setGender ( const std::string & gender ) ;
```
> setGender
You can increase your App's performance by optionally including the additional information above. This allows selected premium advertisers to display their Ads to your users. To pass this additional information, use the following methods BEFORE calling loadModuleToCache.
accepted valued "Male", "Female"

```cpp
static void setFramework ( const std::string & f ) ;
```
> setFramework


### Listeners
```cpp
void onModuleLoaded ( const std::string & placement )
```
> Notifies the delegate that the module has finished loading

```cpp
void onModuleClosed ( const std::string & placement )
```
> Notifies the delegate that the module has closed

```cpp
void onModuleClicked ( const std::string & placement )
```
> Notifies the delegate that the module has clicked

```cpp
void onModuleCached ( const std::string & placement )
```
> Notifies the delegate that the module has cached

```cpp
void onModuleFailed ( const std::string & placement ,
                      const std::string & error ,
                      bool iscached )
```
> Notifies the delegate that the module has fail

```cpp
void onMediaFinished ( bool viewCompleted )
```
> Notifies the delegate that the rewarded video has finished playing.


