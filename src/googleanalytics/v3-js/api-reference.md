## API Reference

### Methods
```javascript
sdkbox.PluginGoogleAnalytics.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginGoogleAnalytics.startSession();
```
> The analytics session is being explicitly started at plugin initialization time.

```javascript
sdkbox.PluginGoogleAnalytics.stopSession();
```
> You normally will never stop a session manually.

```javascript
sdkbox.PluginGoogleAnalytics.dispatchHits();
```
> Manually request dispatch of hits. By default, data is dispatched from the
Google Analytics SDK for Android every 5 minutes.

```javascript
sdkbox.PluginGoogleAnalytics.dispatchPeriodically(seconds);
```
> Change the dispatch info time period to the desired amount of seconds.

```javascript
sdkbox.PluginGoogleAnalytics.stopPeriodicalDispatch();
```
> Stop periodically sending info. Then manually the <code>dispatchPeridically</code>
or <code>dispatchHits</code> should be called.

```javascript
sdkbox.PluginGoogleAnalytics.logScreen(title);
```
> Log screen info. title is the title of a screen. Screens are logical units
inside your app you'd like to identify at analytics panel.

```javascript
sdkbox.PluginGoogleAnalytics.logEvent(eventCategory,
                                       eventAction,
                                       eventLabel,
                                       value);
```
> GoogleAnalytics::logEvent("Achievement", "Unlocked", "Slay 10 dragons", 5);

```javascript
sdkbox.PluginGoogleAnalytics.logException(exceptionDescription, isFatal);
```
> Log an exception. It is a basic support for in-app events.

```javascript
sdkbox.PluginGoogleAnalytics.logTiming(timingCategory,
                                        timingInterval,
                                        timingName,
                                        timingLabel);
```
> Measure a time inside the application.

```javascript
sdkbox.PluginGoogleAnalytics.logSocial(socialNetwork,
                                        socialAction,
                                        socialTarget);
```
> Log a social event.

```javascript
sdkbox.PluginGoogleAnalytics.setDryRun(dr);
```
> While running on dry run, the tracked events won't be sent to the actual
analytics account.

```javascript
sdkbox.PluginGoogleAnalytics.enableAdvertisingTracking(e);
```
> Enable advertising tracking when in google's ad vendors.

```javascript
sdkbox.PluginGoogleAnalytics.createTracker(trackerId);
```
> Create a tracker identified by the google analytics tracker id XX-YYYYYYYY-Z.
If the tracker already existed, no new tracker will be created. In any case, the
tracker associated with tracker id will be set as default tracker for  analytics
operations.

```javascript
sdkbox.PluginGoogleAnalytics.enableTracker(trackerId);
```
> Enable a tracker identified by a trackerId. If the tracker does not exist,
nothing will happen.


### Listeners

