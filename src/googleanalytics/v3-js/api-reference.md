## API Reference

### Methods

#### Dispatch Methods. Dispatches hits (view, events, etc.) to Google Analytics if a network connection is available.

```cpp
sdkbox.PluginGoogleAnalytics.init();
```
> initialize the plugin instance.

```cpp
sdkbox.PluginGoogleAnalytics.dispatchHits();
```
> Manually request dispatch of hits. By default, data is dispatched from the
Google Analytics SDK for Android every 5 minutes.

```cpp
sdkbox.PluginGoogleAnalytics.dispatchPeriodically(numberOfSeconds);
```
> Change the dispatch info time period to the desired amount of seconds.

```cpp
sdkbox.PluginGoogleAnalytics.stopPeriodicalDispatch();
```
> Stop periodically sending info. Then manually the <code>dispatchPeridically</code>
or <code>dispatchHits</code> should be called.

####  Session control.  A session represents a single period of user interaction with your game. Sessions serve as useful containers of measured activity, which includes screen views, events, and ecommerce transactions.

```cpp
sdkbox.PluginGoogleAnalytics.startSession();
```
> The analytics session is being explicitly started at plugin initialization time.

```cpp
sdkbox.PluginGoogleAnalytics.stopSession();
```
> You normally will never stop a session manually.

#### Screens. Screens in Google Analytics represent content users are viewing within your game. A screen view consists of a single string field that will be used as the screen name in your Google Analytics reports.

```cpp
sdkbox.PluginGoogleAnalytics.logScreen(title);
```
> Log screen info. title is the title of a screen. Screens are logical units
inside your app you'd like to identify at analytics panel.

#### Events. Events are a useful way to collect data about a user's interaction with interactive components of your game, like the use of a particular item. An event consists of four fields that you can use to describe a user's interaction with your game.

```cpp
sdkbox.PluginGoogleAnalytics.logEvent(eventCategory, eventAction, eventLabel, value);
```
> sdkbox.PluginGoogleAnalytics.logEvent("Achievement", "Unlocked", "Slay 10 dragons", 5);

#### Crashes and Exceptions. Crash and exception measurement allows you to measure the number and type of caught and uncaught crashes and exceptions that occur in your game.

```cpp
sdkbox.PluginGoogleAnalytics.logException(exceptionDescription, isFatal);
```
> Log an exception. It is a basic support for in-app events.

#### User timing. Measuring user timings provides a native way to measure a period of time in Google Analytics. For example, this can be useful to measure resource load times.

```cpp
sdkbox.PluginGoogleAnalytics.logTiming(timingCategory, timingInterval, timingName, timingLabel);
```
> Measure a time inside the application.

#### Social. Social interaction measurement allows you to measure a user's interactions with various social network sharing and recommendation widgets embedded in your content.

```cpp
sdkbox.PluginGoogleAnalytics.logSocial(socialNetwork, socialAction, socialTarget);
```
> Log a social event.

#### General purpose methods.

```cpp
sdkbox.PluginGoogleAnalytics.setDryRun(dr);
```
> While running on dry run, the tracked events won't be sent to the actual
analytics account.

```cpp
sdkbox.PluginGoogleAnalytics.enableAdvertisingTracking(e);
```
> Enable advertising tracking when in google's ad vendors.

```cpp
sdkbox.PluginGoogleAnalytics.createTracker(trackerId);
```
> Create a tracker identified by the google analytics tracker id XX-YYYYYYYY-Z.
If the tracker already existed, no new tracker will be created. In any case, the
tracker associated with tracker id will be set as default tracker for  analytics
operations.

```cpp
sdkbox.PluginGoogleAnalytics.enableTracker(trackerId);
```
> Enable a tracker identified by a trackerId. If the tracker does not exist,
nothing will happen.
