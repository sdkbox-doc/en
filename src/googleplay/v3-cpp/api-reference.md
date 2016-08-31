## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void startSession ( ) ;
```
> The analytics session is being explicitly started at plugin initialization time.

```cpp
static void stopSession ( ) ;
```
> You normally will never stop a session manually.

```cpp
static void dispatchHits ( ) ;
```
> Manually request dispatch of hits. By default, data is dispatched from the
Google Analytics SDK for Android every 5 minutes.

```cpp
static void dispatchPeriodically ( int seconds ) ;
```
> Change the dispatch info time period to the desired amount of seconds.

```cpp
static void stopPeriodicalDispatch ( ) ;
```
> Stop periodically sending info. Then manually the <code>dispatchPeridically</code>
or <code>dispatchHits</code> should be called.

```cpp
static void setUser ( const std::string & userID ) ;
```
> Set user ID for this tracking session

```cpp
static void setDimension ( int index , const std::string & value ) ;
```
> Set value to custom dimension

```cpp
static void setMetric ( int index , const std::string & value ) ;
```
> Set value to custom metric

```cpp
static void logScreen ( const std::string & title ) ;
```
> Log screen info. title is the title of a screen. Screens are logical units
inside your app you'd like to identify at analytics panel.

```cpp
static void logEvent ( const std::string & eventCategory ,
                       const std::string & eventAction ,
                       const std::string & eventLabel ,
                       int value ) ;
```
> GoogleAnalytics::logEvent("Achievement", "Unlocked", "Slay 10 dragons", 5);

```cpp
static void logException ( const std::string & exceptionDescription ,
                           bool isFatal ) ;
```
> Log an exception. It is a basic support for in-app events.

```cpp
static void logTiming ( const std::string & timingCategory ,
                        int timingInterval ,
                        const std::string & timingName ,
                        const std::string & timingLabel ) ;
```
> Measure a time inside the application.

```cpp
static void logSocial ( const std::string & socialNetwork ,
                        const std::string & socialAction ,
                        const std::string & socialTarget ) ;
```
> Log a social event.

```cpp
static void setDryRun ( bool enable ) ;
```
> While running on dry run, the tracked events won't be sent to the actual
analytics account.

```cpp
static void enableAdvertisingTracking ( bool enable ) ;
```
> Enable advertising tracking when in google's ad vendors.

```cpp
static void createTracker ( const std::string & trackerId ) ;
```
> Create a tracker identified by the google analytics tracker id XX-YYYYYYYY-Z.
If the tracker already existed, no new tracker will be created. In any case, the
tracker associated with tracker id will be set as default tracker for  analytics
operations.

```cpp
static void enableTracker ( const std::string & trackerId ) ;
```
> Enable a tracker identified by a trackerId. If the tracker does not exist,
nothing will happen.


### Listeners

