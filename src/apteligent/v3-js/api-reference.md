## API Reference

### Methods
```javascript
sdkbox.PluginApteligent.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginApteligent.setListener(listener);
```
> Set listener to listen for apteligent events

```javascript
sdkbox.PluginApteligent.addFilter(filter);
```
> Adds an additional filter for network instrumentation.

```javascript
sdkbox.PluginApteligent.leaveBreadcrumb(breadcrumb);
```
> Breadcrumbs provide the ability to track activity within your app.

```javascript
sdkbox.PluginApteligent.setAsyncBreadcrumbMode(writeAsync);
```
> By default, breadcrumbs are flushed to disk immediately when written.
This is by design - in order to provide an accurate record of everything
that happened up until the point your app crashed.

```javascript
sdkbox.PluginApteligent.updateLocation(latitude, longitude);
```
> Inform Apteligent of the device's most recent location for use with
performance monitoring.

```javascript
sdkbox.PluginApteligent.logNetworkRequest(method,
                                           urlString,
                                           latency,
                                           bytesRead,
                                           bytesSent,
                                           responseCode);
```
> Logging endpoints is a way of manually logging custom network library
network access to URL's which fall outside Apteligent's monitoring
of NSURLConnection and ASIHTTPRequest method calls.

```javascript
sdkbox.PluginApteligent.setOptOutStatus(status);
```
> If you wish to offer your users the ability to opt out of Apteligent
crash reporting, you can set the OptOutStatus to YES. If you do so, any
pending crash reports will be purged.

```javascript
sdkbox.PluginApteligent.getOptOutStatus();
```
> Retrieve current opt out status.

```javascript
sdkbox.PluginApteligent.setMaxOfflineCrashReports(max);
```
> Set the maximum number of crash reports that will be stored on
the local device if the device does not have internet connectivity. If
more than |maxOfflineCrashReports| crashes occur, the oldest crash will be
overwritten. Decreasing the value of this setting will not delete
any offline crash reports. Unsent crash reports will be kept until they are
successfully transmitted to Apteligent, hence there may be more than
|maxOfflineCrashReports| stored on the device for a short period of time.

```javascript
sdkbox.PluginApteligent.maxOfflineCrashReports();
```
> Get the maximum number of Apteligent crash reports that will be stored on
the local device if the device does not have internet connectivity.

```javascript
sdkbox.PluginApteligent.getUserUUID();
```
> Get the Apteligent generated unique identifier for this device.

```javascript
sdkbox.PluginApteligent.setUsername(username);
```
> Associate a username string with the device's Apteligent UUID. This will
send the association to Apteligent's back end.

```javascript
sdkbox.PluginApteligent.setValueforKey(value, key);
```
> Associate an arbitrary key/value pair with the device's Apteligent UUID.

```javascript
sdkbox.PluginApteligent.didCrashOnLastLoad();
```
> Did the application crash on the previous load?

```javascript
sdkbox.PluginApteligent.beginUserflow(name);
```
> Init and begin a userflow with a default value.

```javascript
sdkbox.PluginApteligent.beginUserflow(name, value);
```
> Init and begin a userflow with an input value.

```javascript
sdkbox.PluginApteligent.cancelUserflow(name);
```
> Cancel a userflow as if it never existed.

```javascript
sdkbox.PluginApteligent.endUserflow(name);
```
> End an already begun userflow successfully.

```javascript
sdkbox.PluginApteligent.failUserflow(name);
```
> End an already begun userflow as a failure.

```javascript
sdkbox.PluginApteligent.valueForUserflow(name);
```
> Get the currency cents value of a userflow.

```javascript
sdkbox.PluginApteligent.setValueforUserflow(value, name);
```
> Set the currency cents value of a userflow.

```javascript
sdkbox.PluginApteligent.sendAppLoadData();
```
> Tell Apteligent to send app load event.
By default, Apteligent will send app load event automatically when your app is started
However, if you set delaySendingAppLoad flag to YES on config, you can call this method to
manually send app load event.

```javascript
sdkbox.PluginApteligent.setLoggingLevel(loggingLevel);
```
> Set the logging level to tune the verbosity of Apteligent log messages.


### Listeners
```javascript
onCrashOnLastLoad();
```
> Notifies the delegate that the app has crash last time.


