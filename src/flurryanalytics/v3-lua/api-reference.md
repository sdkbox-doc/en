## API Reference

### Methods
```lua
sdkbox.PluginFlurryAnalytics:init()
```
> init plugin, must be first invoke

```lua
sdkbox.PluginFlurryAnalytics:SDKBOX_DEPRECATED(setAppVersion(conststd::string&version)
```
> Explicitly specifies the App Version that Flurry will use to group Analytics data.

<pre>
This is an optional method that overrides the App Version Flurry uses for reporting. Flurry will
use the CFBundleVersion in your info.plist file when this method is not invoked.
@note There is a maximum of 605 versions allowed for a single app. \n
This method must be called prior to invoking #startSession:.
@related function
 Android:   setVersionName(String version)
 iOS:       setAppVersion(NString version)
@deprecated flurry will read veersion number from app itself, if it was not set
</pre>

```lua
sdkbox.PluginFlurryAnalytics:getFlurryAgentVersion()
```
> Retrieves the Flurry Agent Build Version.

<pre>
This is an optional method that retrieves the Flurry Agent Version the app is running under.
It is most often used if reporting an unexpected behavior of the SDK to <a href="mailto:iphonesupport@flurry.com">
Flurry Support</a>
@note This method must be called prior to invoking #startSession:. \n
FAQ for the iPhone SDK is located at <a href="http://wiki.flurry.com/index.php?title=IPhone_FAQ">
Support Center - iPhone FAQ</a>.
@see #setLogLevel: for information on how to view debugging information on your console.
@return The agent version of the Flurry SDK.
@related function
 Android:   getReleaseVersion()
 iOS:       getFlurryAgentVersion()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setShowErrorInLogEnabled(value)
```
> Displays an exception in the debug log if thrown during a Session.

<pre>
This is an optional method that augments the debug logs with exceptions that occur during the session.
You must both capture exceptions to Flurry and set debug logging to enabled for this method to
display information to the console. The default setting for this method is  NO.
@note This method must be called prior to invoking #startSession:.
@see #setLogLevel: for information on how to view debugging information on your console. \n
#logError:message:exception: for details on logging exceptions. \n
#logError:message:error: for details on logging errors.
@related function
 iOS:       setShowErrorInLogEnabled()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setDebugLogEnabled(value)
```
> Generates debug logs to console.

<pre>
This is an optional method that displays debug information related to the Flurry SDK.
display information to the console. The default setting for this method is  NO
which sets the log level to  FlurryLogLevelCriticalOnly.
When set to  YES the debug log level is set to  FlurryLogLevelDebug
@note This method must be called prior to invoking #startSession:. If the method, setLogLevel is called later in the code, debug logging will be automatically enabled.
@related function
 Android:   setLogEnabled
 iOS:       setDebugLogEnabled()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setLogLevel(value)
```
> Generates debug logs to console.

<pre>
This is an optional method that displays debug information related to the Flurry SDK.
display information to the console. The default setting for this method is  FlurryLogLevelCritycalOnly.
@note Its good practice to call this method prior to invoking #startSession:. If debug logging is disabled earlier, this method will enable it.
@related function
 Android:   setLogLevel
 iOS:       setLogLevel
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setSessionContinueSeconds(seconds)
```
> Set the timeout for expiring a Flurry session.

<pre>
This is an optional method that sets the time the app may be in the background before
starting a new session upon resume.  The default value for the session timeout is 10
seconds in the background.
@note This method must be called prior to invoking #startSession:.
@related function
 Android:   setContinueSessionMillis
 iOS:       setSessionContinueSeconds
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setCrashReportingEnabled(value)
```
> Enable automatic collection of crash reports.

<pre>
This is an optional method that collects crash reports when enabled. The
default value is  NO.
@note This method must be called prior to invoking #startSession:.
@related function
 Android:   setCaptureUncaughtExceptions
 iOS:       setCrashReportingEnabled
</pre>

```lua
sdkbox.PluginFlurryAnalytics:startSession()
```
> Start a Flurry session for the project denoted by  apiKey.

<pre>
This method serves as the entry point to Flurry Analytics collection.  It must be
called in the scope of  applicationDidFinishLaunching.  The session will continue
for the period the app is in the foreground until your app is backgrounded for the
time specified in #setSessionContinueSeconds:. If the app is resumed in that period
the session will continue, otherwise a new session will begin.
Crash reporting will not be enabled. See #setCrashReportingEnabled: for
more information.
@note If testing on a simulator, please be sure to send App to background via home
button. Flurry depends on the iOS lifecycle to be complete for full reporting.
@see #setSessionContinueSeconds: for details on setting a custom session timeout.
 @related function
  Android:   onStartSession
  iOS:       startSession
</pre>

```lua
sdkbox.PluginFlurryAnalytics:endSession()
```
> end session, just valid on Android

<pre>
@related function
 Android:    onEndSession()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:activeSessionExists()
```
> Start a Flurry session for the project denoted by  apiKey.

<pre>
@related function
 Android:    isSessionActive
 iOS:        activeSessionExists
</pre>

```lua
sdkbox.PluginFlurryAnalytics:getSessionID()
```
> Start a Flurry session for the project denoted by  apiKey.

<pre>
@related function
Android: getSessionId()
iOS:     getSessionID()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:pauseBackgroundSession()
```
> Pauses a Flurry session left running in background. on valid on iOS

<pre>
This method should be used in case of #setBackgroundSessionEnabled: set to YES. It can be
called when application finished all background tasks (such as playing music) to pause session.
@see #setBackgroundSessionEnabled: for details on setting a custom behaviour on resigning activity.
@related function
iOS:     pauseBackgroundSession()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:addOrigin(originName, originVersion)
```
> Adds an SDK origin specified by  originName and  originVersion.

<pre>
This method allows you to specify origin within your Flurry SDK wrapper. As a general rule
you should capture all the origin info related to your wrapper for Flurry SDK after every session start.
@see #addOrigin:withVersion:withParameters: for details on reporting origin info with parameters. \n
@related function
Android: addOrigin (String originName, String originVersion)
iOS:     addOrigin: (NSString >) originName withVersion: (NSString >) originVersion
</pre>

```lua
sdkbox.PluginFlurryAnalytics:addOrigin(originName, originVersion, parameters)
```
> Adds a custom parameterized origin specified by  originName with  originVersion and  parameters.

<pre>
This method overrides #addOrigin to allow you to associate parameters with an origin attribute. Parameters
are valuable as they allow you to store characteristics of an origin.
@note You should not pass private or confidential information about your origin info in a
custom origin. \n
A maximum of 9 parameter names may be associated with any origin. Sending
over 10 parameter names with a single origin will result in no parameters being logged
for that origin.
@related function
Android: addOrigin (String originName, String originVersion, Map< String, String > originParameters)
iOS:     addOrigin: (NSString >) originName withVersion: (NSString >) originVersion withParameters: (NSDictionary >) parameters
</pre>

```lua
sdkbox.PluginFlurryAnalytics:addOrigin(originName, originVersion, parameters)
```
> just for lua, js binding, have the same function with addOrigin(string, string, map)

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName)
```
> Records a custom event specified by  eventName.

<pre>
This method allows you to specify custom events within your app.  As a general rule
you should capture events related to user navigation within your app, any action
around monetization, and other events as they are applicable to tracking progress
towards your business goals.
@note You should not pass private or confidential information about your users in a
custom event. \n
Where applicable, you should make a concerted effort to use timed events with
parameters (#logEvent:withParameters:timed:) or events with parameters
(#logEvent:withParameters:). This provides valuable information around the time the user
spends within an action (e.g. - time spent on a level or viewing a page) or characteristics
of an action (e.g. - Buy Event that has a Parameter of Widget with Value Golden Sword).
@see #logEvent:withParameters: for details on storing events with parameters. \n
#logEvent:timed: for details on storing timed events. \n
#logEvent:withParameters:timed: for details on storing timed events with parameters. \n
#endTimedEvent:withParameters: for details on stopping a timed event and (optionally) updating
parameters.
that can be easily understood by non-technical people in your business domain.
@return enum FA_FlurryEventRecordStatus for the recording status of the logged event.
@related function
Android: logEvent (String eventId)
iOS:     logEvent:(NSString >)eventName
</pre>

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters)
```
> Records a custom parameterized event specified by  eventName with  parameters.

<pre>
This method overrides #logEvent to allow you to associate parameters with an event. Parameters
are extremely valuable as they allow you to store characteristics of an action. For example,
if a user purchased an item it may be helpful to know what level that user was on.
By setting this parameter you will be able to view a distribution of levels for the purcahsed
event on the <a href="http://dev.flurry.com">Flurrly Dev Portal</a>.
@note You should not pass private or confidential information about your users in a
custom event. \n
A maximum of 10 parameter names may be associated with any event. Sending
over 10 parameter names with a single event will result in no parameters being logged
for that event. You may specify an infinite number of Parameter values. For example,
a Search Box would have 1 parameter name (e.g. - Search Box) and many values, which would
allow you to see what values users look for the most in your app. \n
Where applicable, you should make a concerted effort to use timed events with
parameters (#logEvent:withParameters:timed:). This provides valuable information
around the time the user spends within an action (e.g. - time spent on a level or
viewing a page).
@see #logEvent:withParameters:timed: for details on storing timed events with parameters. \n
#endTimedEvent:withParameters: for details on stopping a timed event and (optionally) updating
parameters.
that can be easily understood by non-technical people in your business domain.
@return enum FA_FlurryEventRecordStatus for the recording status of the logged event.
@related function
Android: logEvent (String eventId, Map< String, String > parameters)
iOS:     logEvent:(NSString >)eventName withParameters:(NSDictionary >)parameters;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters)
```
> just for lua, js binding, have same function with logEvent(string, map)

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, timed)
```
> Records a timed event specified by  eventName.

<pre>
This method overrides #logEvent to allow you to capture the length of an event. This can
be extremely valuable to understand the level of engagement with a particular action. For
example, you can capture how long a user spends on a level or reading an article.
@note You should not pass private or confidential information about your users in a
custom event. \n
Where applicable, you should make a concerted effort to use parameters with your timed
events (#logEvent:withParameters:timed:). This provides valuable information
around the characteristics of an action (e.g. - Buy Event that has a Parameter of Widget with
Value Golden Sword).
@see #logEvent:withParameters:timed: for details on storing timed events with parameters. \n
#endTimedEvent:withParameters: for details on stopping a timed event and (optionally) updating
parameters.
that can be easily understood by non-technical people in your business domain.
@return enum FA_FlurryEventRecordStatus for the recording status of the logged event.
@related function
Android: logEvent (String eventId, boolean timed)
iOS:     logEvent:(NSString >)eventName timed:(BOOL)timed;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters, timed)
```
> Records a custom parameterized timed event specified by  eventName with  parameters.

<pre>
This method overrides #logEvent to allow you to capture the length of an event with parameters.
This can be extremely valuable to understand the level of engagement with a particular action
and the characteristics associated with that action. For example, you can capture how long a user
spends on a level or reading an article. Parameters can be used to capture, for example, the
author of an article or if something was purchased while on the level.
@note You should not pass private or confidential information about your users in a
custom event.
@see #endTimedEvent:withParameters: for details on stopping a timed event and (optionally) updating
parameters.
that can be easily understood by non-technical people in your business domain.
@return enum FA_FlurryEventRecordStatus for the recording status of the logged event.
@related function
Android: logEvent (String eventId, Map< String, String > parameters, boolean timed)
iOS:     logEvent:(NSString >)eventName withParameters:(NSDictionary >)parameters timed:(BOOL)timed;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:logEvent(eventName, parameters, timed)
```
> just for lua, js binding, have the same function with logEvent(string, map, bool)

```lua
sdkbox.PluginFlurryAnalytics:endTimedEvent(eventId)
```
> End a timed event

<pre>
@related function
Android: endTimedEvent (String eventId)
</pre>

```lua
sdkbox.PluginFlurryAnalytics:endTimedEvent(eventName, parameters)
```
> Ends a timed event specified by  eventName and optionally updates parameters with  parameters.

<pre>
This method ends an existing timed event.  If parameters are provided, this will overwrite existing
parameters with the same name or create new parameters if the name does not exist in the parameter
map set by #logEvent:withParameters:timed:.
@note You should not pass private or confidential information about your users in a
custom event. \n
If the app is backgrounded prior to ending a timed event, the Flurry SDK will automatically
end the timer on the event. \n
#endTimedEvent:withParameters: is ignored if called on a previously
terminated event.
@see #logEvent:withParameters:timed: for details on starting a timed event with parameters.
that can be easily understood by non-technical people in your business domain.
@related function
Android: endTimedEvent (String eventId, Map< String, String > parameters)
iOS:     endTimedEvent:(NSString >)eventName withParameters:(NSDictionary >)parameters;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:endTimedEvent(eventName, parameters)
```
> just for lua, js binding, have same function with endTimeEvent(string, map)

```lua
sdkbox.PluginFlurryAnalytics:logError(errorID, message, info)
```
> Records an app exception. Commonly used to catch unhandled exceptions.

<pre>
This method captures an exception for reporting to Flurry. We recommend adding an uncaught
exception listener to capture any exceptions that occur during usage that is not
anticipated by your app.
@see #logError:message:error: for details on capturing errors.
@related function
Android: onError (String errorId, String message, String errorClass)
iOS:     logError:(NSString >)errorID message:(NSString >)message error:nullptr;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:logPageView()
```
> Explicitly track a page view during a session.

<pre>
This method increments the page view count for a session when invoked. It does not associate a name
with the page count. To associate a name with a count of occurences see #logEvent:.
@see #logAllPageViews for details on automatically incrementing page view count based on user
traversing navigation or tab bar controller.
@related function
Android: onPageView
iOS:     logPageView
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setUserID(userID)
```
> Assign a unique id for a user in your app.

<pre>
@note Please be sure not to use this method to pass any private or confidential information
about the user.
@related function
Android: setUserId (String userId)
iOS:     setUserID:(NSString >)userID
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setAge(age)
```
> Set your user's age in years.

<pre>
Use this method to capture the age of your user. Only use this method if you collect this
information explictly from your user (i.e. - there is no need to set a default value).
@note The age is aggregated across all users of your app and not available on a per user
basis.
@related function
Android: setAge (int age)
iOS:     setAge:(int)age;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setGender(gender)
```
> Set your user's gender.

<pre>
Use this method to capture the gender of your user. Only use this method if you collect this
information explictly from your user (i.e. - there is no need to set a default value). Allowable
values are  @"m" or  @"f"
@note The gender is aggregated across all users of your app and not available on a per user
basis.
                 "u" -1 unknow
                 "m" 1 male
                 "f" 0 female
@related function
Android: setGender (byte gender)
iOS:     setGender:(NSString >)gender;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setReportLocation(reportLocation)
```
> Set whether Flurry should record location via GPS. Defaults to true. valid on Android

<pre>
@related function
Android: setReportLocation (boolean reportLocation)
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setLatitude(latitude,
                                          longitude,
                                          horizontalAccuracy,
                                          verticalAccuracy)
```
> Set the location of the session.

<pre>
Use information from the CLLocationManager to specify the location of the session. Flurry does not
automatically track this information or include the CLLocation framework.
@note Only the last location entered is captured per session. \n
Regardless of accuracy specified, the Flurry SDK will only report location at city level or higher. \n
Location is aggregated across all users of your app and not available on a per user basis. \n
This information should only be captured if it is germaine to the use of your app.
After starting the location manager, you can set the location with Flurry. You can implement
CLLocationManagerDelegate to be aware of when the location is updated. Below is an example
of how to use this method, after you have recieved a location update from the locationManager.
        no use on Android
        no use on Android
@related function
Android: setLocation (float lat, float lon)
iOS:     setLatitude:(double)latitude longitude:(double)longitude horizontalAccuracy:(float)horizontalAccuracy verticalAccuracy:(float)verticalAccuracy;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:clearLocation()
```
> clear the default location.valid on Android

<pre>
@related function
Android: clearLocation ()
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setSessionReportsOnCloseEnabled(sendSessionReportsOnClose)
```
> Set session to report when app closes.valid on iOS

<pre>
Use this method report session data when the app is closed. The default value is  YES.
@note This method is rarely invoked in iOS >= 3.2 due to the updated iOS lifecycle.
@see #setSessionReportsOnPauseEnabled:
@related function
iOS: setSessionReportsOnCloseEnabled:(bool) sendSessionReportsOnClose
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setSessionReportsOnPauseEnabled(setSessionReportsOnPauseEnabled)
```
> Set session to report when app is sent to the background.valid on iOS

<pre>
Use this method report session data when the app is paused. The default value is  YES.
@related function
iOS: setSessionReportsOnPauseEnabled:(bool) setSessionReportsOnPauseEnabled
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setBackgroundSessionEnabled(setBackgroundSessionEnabled)
```
> Set session to support background execution.valid on iOS

<pre>
Use this method to enable reporting of errors and events when application is
running in backgorund (such applications have  UIBackgroundModes in Info.plist).
You should call #pauseBackgroundSession when appropriate in background mode to
pause the session (for example when played song completed in background)
Default value is  NO
@see #pauseBackgroundSession for details
continue log events and errors for running session.
@related function
iOS:         setBackgroundSessionEnabled:(bool) setBackgroundSessionEnabled
@
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setEventLoggingEnabled(value)
```
> Enable custom event logging.

<pre>
Use this method to allow the capture of custom events. The default value is  YES.
@related function
Android:     setLogEvents (boolean logEvents)
iOS:         setEventLoggingEnabled:(bool) value
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setPulseEnabled(value)
```
> Enables Flurry Pulse

<pre>
@note: Please see https://developer.yahoo.com/flurry-pulse/ for more details
@related function
Android:     setPulseEnabled (boolean isEnabled)
iOS:         setPulseEnabled:(BOOL)value;
</pre>

```lua
sdkbox.PluginFlurryAnalytics:setListener(listener)
```
> set listener for session callback


### Listeners
```lua
flurrySessionDidCreateWithInfo(info)
```
> Invoked when analytics session is created,

<pre>
This method informs the app that an analytics session is created.
@see Flurry#startSession for details on session.
</pre>


