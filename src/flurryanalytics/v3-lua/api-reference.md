## API Reference

### Methods
```lua
sdkbox.PluginFlurryAnalytics:init()
```
> init plugin, must be first invoke

```lua
sdkbox.PluginFlurryAnalytics:setAppVersion(version)
```
> Explicitly specifies the App Version that Flurry will use to group Analytics data.

```lua
sdkbox.PluginFlurryAnalytics:getFlurryAgentVersion()
```
> Retrieves the Flurry Agent Build Version.

```lua
sdkbox.PluginFlurryAnalytics:setShowErrorInLogEnabled(value)
```
> Displays an exception in the debug log if thrown during a Session.

```lua
sdkbox.PluginFlurryAnalytics:setDebugLogEnabled(value)
```
> Generates debug logs to console.

```lua
sdkbox.PluginFlurryAnalytics:setLogLevel(value)
```
> Generates debug logs to console.

```lua
sdkbox.PluginFlurryAnalytics:setSessionContinueSeconds(seconds)
```
> Set the timeout for expiring a Flurry session.

```lua
sdkbox.PluginFlurryAnalytics:setCrashReportingEnabled(value)
```
> Enable automatic collection of crash reports.

```lua
sdkbox.PluginFlurryAnalytics:startSession()
```
> Start a Flurry session for the project denoted by  apiKey.

```lua
sdkbox.PluginFlurryAnalytics:endSession()
```
> end session, just valid on Android

```lua
sdkbox.PluginFlurryAnalytics:activeSessionExists()
```
> Start a Flurry session for the project denoted by  apiKey.

```lua
sdkbox.PluginFlurryAnalytics:getSessionID()
```
> Start a Flurry session for the project denoted by  apiKey.

```lua
sdkbox.PluginFlurryAnalytics:pauseBackgroundSession()
```
> Pauses a Flurry session left running in background. on valid on iOS

```lua
sdkbox.PluginFlurryAnalytics:addOrigin(originName, originVersion)
```
> Adds an SDK origin specified by  originName and  originVersion.

```lua
sdkbox.PluginFlurryAnalytics:addOrigin(originName, originVersion, parameters)
```
> Adds a custom parameterized origin specified by  originName with  originVersion and  parameters.

```lua
sdkbox.PluginFlurryAnalytics:addOrigin(originName, originVersion, parameters)
```
> just for lua, js binding, have the same function with addOrigin(string, string, map)

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName)
```
> Records a custom event specified by  eventName.

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters)
```
> Records a custom parameterized event specified by  eventName with  parameters.

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters)
```
> just for lua, js binding, have same function with logEvent(string, map)

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, timed)
```
> Records a timed event specified by  eventName.

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters, timed)
```
> Records a custom parameterized timed event specified by  eventName with  parameters.

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters, timed)
```
> just for lua, js binding, have the same function with logEvent(string, map, bool)

```lua
sdkbox.PluginFlurryAnalytics:endTimedEvent(eventId)
```
> End a timed event

```lua
sdkbox.PluginFlurryAnalytics:endTimedEvent(eventName, parameters)
```
> Ends a timed event specified by  eventName and optionally updates parameters with  parameters.

```lua
sdkbox.PluginFlurryAnalytics:endTimedEvent(eventName, parameters)
```
> just for lua, js binding, have same function with endTimeEvent(string, map)

```lua
sdkbox.PluginFlurryAnalytics:logError(errorID, message, info)
```
> Records an app exception. Commonly used to catch unhandled exceptions.

```lua
sdkbox.PluginFlurryAnalytics:logPageView()
```
> Explicitly track a page view during a session.

```lua
sdkbox.PluginFlurryAnalytics:setUserID(userID)
```
> Assign a unique id for a user in your app.

```lua
sdkbox.PluginFlurryAnalytics:setAge(age)
```
> Set your user's age in years.

```lua
sdkbox.PluginFlurryAnalytics:setGender(gender)
```
> Set your user's gender.

```lua
sdkbox.PluginFlurryAnalytics:setReportLocation(reportLocation)
```
> Set whether Flurry should record location via GPS. Defaults to true. valid on Android

```lua
sdkbox.PluginFlurryAnalytics:setLatitude(latitude,
                                          longitude,
                                          horizontalAccuracy,
                                          verticalAccuracy)
```
> Set the location of the session.

```lua
sdkbox.PluginFlurryAnalytics:clearLocation()
```
> clear the default location.valid on Android

```lua
sdkbox.PluginFlurryAnalytics:setSessionReportsOnCloseEnabled(sendSessionReportsOnClose)
```
> Set session to report when app closes.valid on iOS

```lua
sdkbox.PluginFlurryAnalytics:setSessionReportsOnPauseEnabled(setSessionReportsOnPauseEnabled)
```
> Set session to report when app is sent to the background.valid on iOS

```lua
sdkbox.PluginFlurryAnalytics:setBackgroundSessionEnabled(setBackgroundSessionEnabled)
```
> Set session to support background execution.valid on iOS

```lua
sdkbox.PluginFlurryAnalytics:setEventLoggingEnabled(value)
```
> Enable custom event logging.

```lua
sdkbox.PluginFlurryAnalytics:setPulseEnabled(value)
```
> Enables Flurry Pulse

```lua
sdkbox.PluginFlurryAnalytics:setListener(listener)
```
> set listener for session callback


### Listeners
```lua
flurrySessionDidCreateWithInfo(info)
```
> Invoked when analytics session is created,


