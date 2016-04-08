## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( ApteligentListener * listener ) ;
```
> Set listener to listen for apteligent events

```cpp
static ApteligentListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void addFilter ( const std::string & filter ) ;
```
> Adds an additional filter for network instrumentation.

```cpp
static void leaveBreadcrumb ( const std::string & breadcrumb ) ;
```
> Breadcrumbs provide the ability to track activity within your app.

```cpp
static void setAsyncBreadcrumbMode ( bool writeAsync ) ;
```
> By default, breadcrumbs are flushed to disk immediately when written.
This is by design - in order to provide an accurate record of everything
that happened up until the point your app crashed.

```cpp
static void updateLocation ( double latitude , double longitude ) ;
```
> Inform Apteligent of the device's most recent location for use with
performance monitoring.

```cpp
static bool logNetworkRequest ( const std::string & method ,
                                const std::string & urlString ,
                                long latency ,
                                long bytesRead ,
                                long bytesSent ,
                                long responseCode ) ;
```
> Logging endpoints is a way of manually logging custom network library
network access to URL's which fall outside Apteligent's monitoring
of NSURLConnection and ASIHTTPRequest method calls.

```cpp
static void setOptOutStatus ( bool status ) ;
```
> If you wish to offer your users the ability to opt out of Apteligent
crash reporting, you can set the OptOutStatus to YES. If you do so, any
pending crash reports will be purged.

```cpp
static bool getOptOutStatus ( ) ;
```
> Retrieve current opt out status.

```cpp
static void setMaxOfflineCrashReports ( int max ) ;
```
> Set the maximum number of crash reports that will be stored on
the local device if the device does not have internet connectivity. If
more than |maxOfflineCrashReports| crashes occur, the oldest crash will be
overwritten. Decreasing the value of this setting will not delete
any offline crash reports. Unsent crash reports will be kept until they are
successfully transmitted to Apteligent, hence there may be more than
|maxOfflineCrashReports| stored on the device for a short period of time.

```cpp
static int maxOfflineCrashReports ( ) ;
```
> Get the maximum number of Apteligent crash reports that will be stored on
the local device if the device does not have internet connectivity.

```cpp
static std::string getUserUUID ( ) ;
```
> Get the Apteligent generated unique identifier for this device.

```cpp
static void setUsername ( const std::string & username ) ;
```
> Associate a username string with the device's Apteligent UUID. This will
send the association to Apteligent's back end.

```cpp
static void setValueforKey ( const std::string & value ,
                             const std::string & key ) ;
```
> Associate an arbitrary key/value pair with the device's Apteligent UUID.

```cpp
static bool didCrashOnLastLoad ( ) ;
```
> Did the application crash on the previous load?

```cpp
static void beginUserflow ( const std::string & name ) ;
```
> Init and begin a userflow with a default value.

```cpp
static void beginUserflow ( const std::string & name , int value ) ;
```
> Init and begin a userflow with an input value.

```cpp
static void cancelUserflow ( const std::string & name ) ;
```
> Cancel a userflow as if it never existed.

```cpp
static void endUserflow ( const std::string & name ) ;
```
> End an already begun userflow successfully.

```cpp
static void failUserflow ( const std::string & name ) ;
```
> End an already begun userflow as a failure.

```cpp
static int valueForUserflow ( const std::string & name ) ;
```
> Get the currency cents value of a userflow.

```cpp
static void setValueforUserflow ( int value , const std::string & name ) ;
```
> Set the currency cents value of a userflow.

```cpp
static void sendAppLoadData ( ) ;
```
> Tell Apteligent to send app load event.
By default, Apteligent will send app load event automatically when your app is started
However, if you set delaySendingAppLoad flag to YES on config, you can call this method to
manually send app load event.

```cpp
static void setLoggingLevel ( int loggingLevel ) ;
```
> Set the logging level to tune the verbosity of Apteligent log messages.


### Listeners
```cpp
void onCrashOnLastLoad ( ) {
```
> Notifies the delegate that the app has crash last time.


