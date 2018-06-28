## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static std::string getVersion ( ) ;
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```cpp
static void setUserProperty ( const std::string & name ,
                              const std::string & value ) ;
```

```cpp
static void setUserID ( const std::string & userID ) ;
```

```cpp
static void setScreenName ( const std::string & screen ,
                            const std::string & screenClass ) ;
```

```cpp
static void logEvent ( const std::string & event ,
                       const std::map <std::string ,
                       std::string> & params ) ;
```

```cpp
static void resetAnalyticsData ( ) ;
```
> Clears all analytics data for this instance from the device and resets the app instance ID.
FIRAnalyticsConfiguration values will be reset to the default values.

```cpp
static void setAnalyticsCollectionEnabled ( bool enabled ) ;
```
> Sets whether analytics collection is enabled for this app on this device.
This setting is persisted across app sessions. By default it is enabled. (Only for Android)


### Listeners

