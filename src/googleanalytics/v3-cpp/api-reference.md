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
static void logScreen ( string title ) ;
```
> Log screen info. title is the title of a screen. Screens are logical units
inside your app you'd like to identify at analytics panel.

```cpp
static void logEvent ( string eventCategory ,
                       string eventAction ,
                       string eventLabel ,
                       int value ) ;
```
> GoogleAnalytics::logEvent("Achievement", "Unlocked", "Slay 10 dragons", 5);

```cpp
static void logException ( string exceptionDescription , bool isFatal ) ;
```
> Log an exception. It is a basic support for in-app events.

```cpp
static void logTiming ( string timingCategory ,
                        int timingInterval ,
                        string timingName ,
                        string timingLabel ) ;
```
> Measure a time inside the application.

```cpp
static void logSocial ( string socialNetwork ,
                        string socialAction ,
                        string socialTarget ) ;
```
> Log a social event.

```cpp
static void setDryRun ( bool dr ) ;
```
> While running on dry run, the tracked events won't be sent to the actual
analytics account.

```cpp
static void enableAdvertisingTracking ( bool e ) ;
```
> Enable advertising tracking when in google's ad vendors.

```cpp
static void createTracker ( string trackerId ) ;
```
> Create a tracker identified by the google analytics tracker id XX-YYYYYYYY-Z.
If the tracker already existed, no new tracker will be created. In any case, the
tracker associated with tracker id will be set as default tracker for  analytics
operations.

```cpp
static void enableTracker ( string trackerId ) ;
```
> Enable a tracker identified by a trackerId. If the tracker does not exist,
nothing will happen.


### Listeners

