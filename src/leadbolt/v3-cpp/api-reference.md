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
static void loadModule ( const std::string & placement ,
                         const std::string & userData = "" ) ;
```
> load module

```cpp
static void loadModuleToCache ( const std::string & placement ,
                                const std::string & userData = "" ) ;
```
> load module to cache

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
static bool isAdReady ( const std::string & placement ) ;
```
> is ad ready

```cpp
static void setAgeRange ( const std::string & range ) ;
```
> setAgeRange
accepted values "13-17", "18-25", "26-35", "36-45", "46+"

```cpp
static void setGender ( const std::string & gender ) ;
```
> setGender
accepted valued "Male", "Female"

```cpp
static void setFramework ( const std::string & f ) ;
```
> setFramework


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


