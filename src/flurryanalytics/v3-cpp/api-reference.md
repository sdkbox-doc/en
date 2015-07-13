## API Reference

### Methods
```cpp
static bool init ( ) ;
```
> init plugin, must be first invoke

```cpp
static void setAppVersion ( const std::string & version ) ;
```
> Explicitly specifies the App Version that Flurry will use to group Analytics data.

```cpp
static std::string getFlurryAgentVersion ( ) ;
```
> Retrieves the Flurry Agent Build Version.

```cpp
static void setShowErrorInLogEnabled ( bool value ) ;
```
> Displays an exception in the debug log if thrown during a Session.

```cpp
static void setDebugLogEnabled ( bool value ) ;
```
> Generates debug logs to console.

```cpp
static void setLogLevel ( FA_FlurryLogLevel value ) ;
```
> Generates debug logs to console.

```cpp
static void setSessionContinueSeconds ( float seconds ) ;
```
> Set the timeout for expiring a Flurry session.

```cpp
static void setCrashReportingEnabled ( bool value ) ;
```
> Enable automatic collection of crash reports.

```cpp
static void startSession ( ) ;
```
> Start a Flurry session for the project denoted by @c apiKey.

```cpp
static void endSession ( ) ;
```
> end session, just valid on android

```cpp
static bool activeSessionExists ( ) ;
```
> Start a Flurry session for the project denoted by @c apiKey.

```cpp
static std::string getSessionID ( ) ;
```
> Start a Flurry session for the project denoted by @c apiKey.

```cpp
static void pauseBackgroundSession ( ) ;
```
> Pauses a Flurry session left running in background. on valid on ios

```cpp
static void addOrigin ( const std::string & originName ,
                        const std::string & originVersion ) ;
```
> Adds an SDK origin specified by @c originName and @c originVersion.

```cpp
static void addOrigin ( const std::string & originName ,
                        const std::string & originVersion ,
                        std::map <std::string ,
                        std::string> & parameters ) ;
```
> Adds a custom parameterized origin specified by @c originName with @c originVersion and @c parameters.

```cpp
static void addOrigin ( const std::string & originName ,
                        const std::string & originVersion ,
                        const std::string & parameters ) ;
```
> just for lua, js binding, have the same function with addOrigin(string, string, map)

```cpp
static int logEvent ( const std::string & eventName ) ;
```
> Records a custom event specified by @c eventName.

```cpp
static int logEvent ( const std::string & eventName ,
                      std::map <std::string ,
                      std::string> & parameters ) ;
```
> Records a custom parameterized event specified by @c eventName with @c parameters.

```cpp
static int logEvent ( const std::string & eventName ,
                      const std::string & parameters ) ;
```
> just for lua, js binding, have same function with logEvent(string, map)

```cpp
static int logEvent ( const std::string & eventName , bool timed ) ;
```
> Records a timed event specified by @c eventName.

```cpp
static int logEvent ( const std::string & eventName ,
                      std::map <std::string ,
                      std::string> & parameters ,
                      bool timed ) ;
```
> Records a custom parameterized timed event specified by @c eventName with @c parameters.

```cpp
static int logEvent ( const std::string & eventName ,
                      const std::string & parameters ,
                      bool timed ) ;
```
> just for lua, js binding, have the same function with logEvent(string, map, bool)

```cpp
static void endTimedEvent ( const std::string & eventId ) ;
```
> End a timed event

```cpp
static void endTimedEvent ( const std::string & eventName ,
                            std::map <std::string ,
                            std::string> & parameters ) ;
```
> Ends a timed event specified by @c eventName and optionally updates parameters with @c parameters.

```cpp
static void endTimedEvent ( const std::string & eventName ,
                            const std::string & parameters ) ;
```
> just for lua, js binding, have same function with endTimeEvent(string, map)

```cpp
static void logError ( const std::string & errorID ,
                       const std::string & message ,
                       const std::string & info ) ;
```
> Records an app exception. Commonly used to catch unhandled exceptions.

```cpp
static void logPageView ( ) ;
```
> Explicitly track a page view during a session.

```cpp
static void setUserID ( const std::string & userID ) ;
```
> Assign a unique id for a user in your app.

```cpp
static void setAge ( int age ) ;
```
> Set your user's age in years.

```cpp
static void setGender ( const std::string & gender ) ;
```
> Set your user's gender.

```cpp
	 static void setReportLocation ( bool reportLocation ) ;
```
> Set whether Flurry should record location via GPS. Defaults to true. valid on android

```cpp
static void setLatitude ( double latitude ,
                          double longitude ,
                          float horizontalAccuracy ,
                          float verticalAccuracy ) ;
```
> Set the location of the session.

```cpp
static void clearLocation ( ) ;
```
> clear the default location.valid on andriod

```cpp
static void setSessionReportsOnCloseEnabled ( bool sendSessionReportsOnClose ) ;
```
> Set session to report when app closes.valid on ios

```cpp
static void setSessionReportsOnPauseEnabled ( bool setSessionReportsOnPauseEnabled ) ;
```
> Set session to report when app is sent to the background.valid on ios

```cpp
static void setBackgroundSessionEnabled ( bool setBackgroundSessionEnabled ) ;
```
> Set session to support background execution.valid on ios

```cpp
static void setEventLoggingEnabled ( bool value ) ;
```
> Enable custom event logging.

```cpp
static void setPulseEnabled ( bool value ) ;
```
> Enables Flurry Pulse

```cpp
static void setListener ( FlurryAnalyticsListener * listener ) ;
```
> set listener for session callback

```cpp
static FlurryAnalyticsListener * getListener ( ) ;
```
> get listener

```cpp
static void removeListener ( ) ;
```
> remove listener, just set null, will not delete it
        the user should delete listener self


### Listeners
```cpp
void flurrySessionDidCreateWithInfo ( std::map <std::string ,
                                      std::string> & info );
```
> Invoked when analytics session is created,
