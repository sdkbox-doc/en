## API Reference

### Methods
```lua
sdkbox.PluginApteligent:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginApteligent:setListener(listener)
```
> Set listener to listen for apteligent events

```lua
sdkbox.PluginApteligent:addFilter(filter)
```
> Adds an additional filter for network instrumentation.

```lua
sdkbox.PluginApteligent:leaveBreadcrumb(breadcrumb)
```
> Breadcrumbs provide the ability to track activity within your app.

<pre>
A breadcrumb is a free form string you supply, which will be timestamped,
and stored in case a crash occurs. Crash reports will contain the breadcrumb
trail from the run of your app that crashed, as well as that of the prior
run.
Breadcrumbs are limited to 140 characters, and only the most recent 100 are
kept. Apteligent will automatically insert a breadcrumb marked
  "session_start"
on each initial launch, or foreground of your app.
Note - Breadcrumbs are an Enterprise level feature.
</pre>

```lua
sdkbox.PluginApteligent:setAsyncBreadcrumbMode(writeAsync)
```
> By default, breadcrumbs are flushed to disk immediately when written.
This is by design - in order to provide an accurate record of everything
that happened up until the point your app crashed.

<pre>
If you are concerned about the performance costs of writing the file, you can
instruct the library to perform all breadcrumb writes on a background thread.
</pre>

```lua
sdkbox.PluginApteligent:updateLocation(latitude, longitude)
```
> Inform Apteligent of the device's most recent location for use with
performance monitoring.

```lua
sdkbox.PluginApteligent:logNetworkRequest(method,
                                           urlString,
                                           latency,
                                           bytesRead,
                                           bytesSent,
                                           responseCode)
```
> Logging endpoints is a way of manually logging custom network library
network access to URL's which fall outside Apteligent's monitoring
of NSURLConnection and ASIHTTPRequest method calls.

```lua
sdkbox.PluginApteligent:setOptOutStatus(status)
```
> If you wish to offer your users the ability to opt out of Apteligent
crash reporting, you can set the OptOutStatus to YES. If you do so, any
pending crash reports will be purged.

```lua
sdkbox.PluginApteligent:getOptOutStatus()
```
> Retrieve current opt out status.

```lua
sdkbox.PluginApteligent:setMaxOfflineCrashReports(max)
```
> Set the maximum number of crash reports that will be stored on
the local device if the device does not have internet connectivity. If
more than |maxOfflineCrashReports| crashes occur, the oldest crash will be
overwritten. Decreasing the value of this setting will not delete
any offline crash reports. Unsent crash reports will be kept until they are
successfully transmitted to Apteligent, hence there may be more than
|maxOfflineCrashReports| stored on the device for a short period of time.

<pre>
The default value is 3, and there is an upper bound of 10.
</pre>

```lua
sdkbox.PluginApteligent:maxOfflineCrashReports()
```
> Get the maximum number of Apteligent crash reports that will be stored on
the local device if the device does not have internet connectivity.

```lua
sdkbox.PluginApteligent:getUserUUID()
```
> Get the Apteligent generated unique identifier for this device.

<pre>
!! This is NOT the device's UDID.
If called before enabling the library, this will return an empty string.
All Apteligent enabled apps on a device will share the UUID created by the
first installed Apteligent enabled app.
If all Apteligent enabled applications are removed from a device, a new
UUID will be generated when the next one is installed.
</pre>

```lua
sdkbox.PluginApteligent:setUsername(username)
```
> Associate a username string with the device's Apteligent UUID. This will
send the association to Apteligent's back end.

```lua
sdkbox.PluginApteligent:setValueforKey(value, key)
```
> Associate an arbitrary key/value pair with the device's Apteligent UUID.

```lua
sdkbox.PluginApteligent:didCrashOnLastLoad()
```
> Did the application crash on the previous load?

```lua
sdkbox.PluginApteligent:beginUserflow(name)
```
> Init and begin a userflow with a default value.

```lua
sdkbox.PluginApteligent:beginUserflow(name, value)
```
> Init and begin a userflow with an input value.

```lua
sdkbox.PluginApteligent:cancelUserflow(name)
```
> Cancel a userflow as if it never existed.

```lua
sdkbox.PluginApteligent:endUserflow(name)
```
> End an already begun userflow successfully.

```lua
sdkbox.PluginApteligent:failUserflow(name)
```
> End an already begun userflow as a failure.

```lua
sdkbox.PluginApteligent:valueForUserflow(name)
```
> Get the currency cents value of a userflow.

```lua
sdkbox.PluginApteligent:setValueforUserflow(value, name)
```
> Set the currency cents value of a userflow.

```lua
sdkbox.PluginApteligent:sendAppLoadData()
```
> Tell Apteligent to send app load event.
By default, Apteligent will send app load event automatically when your app is started
However, if you set delaySendingAppLoad flag to YES on config, you can call this method to
manually send app load event.

```lua
sdkbox.PluginApteligent:setLoggingLevel(loggingLevel)
```
> Set the logging level to tune the verbosity of Apteligent log messages.


### Listeners
```lua
onCrashOnLastLoad()
```
> Notifies the delegate that the app has crash last time.


