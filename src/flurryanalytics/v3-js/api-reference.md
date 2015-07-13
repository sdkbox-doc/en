## API Reference

### Methods
```javascript
sdkbox.PluginFlurryAnalytics.init();
```
> init plugin, must be first invoke

```javascript
sdkbox.PluginFlurryAnalytics.setAppVersion(version);
```
> Explicitly specifies the App Version that Flurry will use to group Analytics data.

```javascript
sdkbox.PluginFlurryAnalytics.getFlurryAgentVersion();
```
> Retrieves the Flurry Agent Build Version.

```javascript
sdkbox.PluginFlurryAnalytics.setShowErrorInLogEnabled(value);
```
> Displays an exception in the debug log if thrown during a Session.

```javascript
sdkbox.PluginFlurryAnalytics.setDebugLogEnabled(value);
```
> Generates debug logs to console.

```javascript
sdkbox.PluginFlurryAnalytics.setLogLevel(value);
```
> Generates debug logs to console.

```javascript
sdkbox.PluginFlurryAnalytics.setSessionContinueSeconds(seconds);
```
> Set the timeout for expiring a Flurry session.

```javascript
sdkbox.PluginFlurryAnalytics.setCrashReportingEnabled(value);
```
> Enable automatic collection of crash reports.

```javascript
sdkbox.PluginFlurryAnalytics.startSession();
```
> Start a Flurry session for the project denoted by @c apiKey.

```javascript
sdkbox.PluginFlurryAnalytics.endSession();
```
> end session, just valid on android

```javascript
sdkbox.PluginFlurryAnalytics.activeSessionExists();
```
> Start a Flurry session for the project denoted by @c apiKey.

```javascript
sdkbox.PluginFlurryAnalytics.getSessionID();
```
> Start a Flurry session for the project denoted by @c apiKey.

```javascript
sdkbox.PluginFlurryAnalytics.pauseBackgroundSession();
```
> Pauses a Flurry session left running in background. on valid on ios

```javascript
sdkbox.PluginFlurryAnalytics.addOrigin(originName, originVersion);
```
> Adds an SDK origin specified by @c originName and @c originVersion.

```javascript
sdkbox.PluginFlurryAnalytics.addOrigin(originName, originVersion, parameters);
```
> Adds a custom parameterized origin specified by @c originName with @c originVersion and @c parameters.

```javascript
sdkbox.PluginFlurryAnalytics.addOrigin(originName, originVersion, parameters);
```
> just for lua, js binding, have the same function with addOrigin(string, string, map)

```javascript
sdkbox.PluginFlurryAnalytics.logEvent(eventName);
```
> Records a custom event specified by @c eventName.

```javascript
sdkbox.PluginFlurryAnalytics.logEvent(eventName, parameters);
```
> Records a custom parameterized event specified by @c eventName with @c parameters.

```javascript
sdkbox.PluginFlurryAnalytics.logEvent(eventName, parameters);
```
> just for lua, js binding, have same function with logEvent(string, map)

```javascript
sdkbox.PluginFlurryAnalytics.logEvent(eventName, timed);
```
> Records a timed event specified by @c eventName.

```javascript
sdkbox.PluginFlurryAnalytics.logEvent(eventName, parameters, timed);
```
> Records a custom parameterized timed event specified by @c eventName with @c parameters.

```javascript
sdkbox.PluginFlurryAnalytics.logEvent(eventName, parameters, timed);
```
> just for lua, js binding, have the same function with logEvent(string, map, bool)

```javascript
sdkbox.PluginFlurryAnalytics.endTimedEvent(eventId);
```
> End a timed event

```javascript
sdkbox.PluginFlurryAnalytics.endTimedEvent(eventName, parameters);
```
> Ends a timed event specified by @c eventName and optionally updates parameters with @c parameters.

```javascript
sdkbox.PluginFlurryAnalytics.endTimedEvent(eventName, parameters);
```
> just for lua, js binding, have same function with endTimeEvent(string, map)

```javascript
sdkbox.PluginFlurryAnalytics.logError(errorID, message, info);
```
> Records an app exception. Commonly used to catch unhandled exceptions.

```javascript
sdkbox.PluginFlurryAnalytics.logPageView();
```
> Explicitly track a page view during a session.

```javascript
sdkbox.PluginFlurryAnalytics.setUserID(userID);
```
> Assign a unique id for a user in your app.

```javascript
sdkbox.PluginFlurryAnalytics.setAge(age);
```
> Set your user's age in years.

```javascript
sdkbox.PluginFlurryAnalytics.setGender(gender);
```
> Set your user's gender.

```javascript
sdkbox.PluginFlurryAnalytics.setReportLocation(reportLocation);
```
> Set whether Flurry should record location via GPS. Defaults to true. valid on android

```javascript
sdkbox.PluginFlurryAnalytics.setLatitude(latitude,
                                          longitude,
                                          horizontalAccuracy,
                                          verticalAccuracy);
```
> Set the location of the session.

```javascript
sdkbox.PluginFlurryAnalytics.clearLocation();
```
> clear the default location.valid on andriod

```javascript
sdkbox.PluginFlurryAnalytics.setSessionReportsOnCloseEnabled(sendSessionReportsOnClose);
```
> Set session to report when app closes.valid on ios

```javascript
sdkbox.PluginFlurryAnalytics.setSessionReportsOnPauseEnabled(setSessionReportsOnPauseEnabled);
```
> Set session to report when app is sent to the background.valid on ios

```javascript
sdkbox.PluginFlurryAnalytics.setBackgroundSessionEnabled(setBackgroundSessionEnabled);
```
> Set session to support background execution.valid on ios

```javascript
sdkbox.PluginFlurryAnalytics.setEventLoggingEnabled(value);
```
> Enable custom event logging.

```javascript
sdkbox.PluginFlurryAnalytics.setPulseEnabled(value);
```
> Enables Flurry Pulse

```javascript
sdkbox.PluginFlurryAnalytics.setListener(listener);
```
> set listener for session callback


### Listeners
```javascript
flurrySessionDidCreateWithInfo(info);
```
> Invoked when analytics session is created,
