## API Reference

### Methods
```javascript
sdkbox.PluginOneSignal.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginOneSignal.setListener(listener);
```
> Set listener to listen for onesignal events

```javascript
sdkbox.PluginOneSignal.registerForPushNotifications();
```
> Only use if you set "auto_register":false in sdkbox_config.json (iOS only)

```javascript
// sdkbox.PluginOneSignal.LogLevel.None
// sdkbox.PluginOneSignal.LogLevel.Fatal
// sdkbox.PluginOneSignal.LogLevel.Error
// sdkbox.PluginOneSignal.LogLevel.Warn
// sdkbox.PluginOneSignal.LogLevel.Info
// sdkbox.PluginOneSignal.LogLevel.Debug
// sdkbox.PluginOneSignal.LogLevel.Verbose
sdkbox.PluginOneSignal.setLogLevel(logLevel, visualLogLevel);
```
> Enable logging to help debug if you run into an issue setting up OneSignal. This selector
is static so you can call it before OneSignal init. The following options are available
with increasingly more information;
sdkbox::OneSignalLogNone, sdkbox::OneSignalLogFatal, sdkbox::OneSignalLogError,
sdkbox::OneSignalLogWarn, sdkbox::OneSignalLogInfo, sdkbox::OneSignalLogDebug,
sdkbox::OneSignalLogVerbose

```javascript
sdkbox.PluginOneSignal.sendTag(key, value);
```
> Tag a user based on an app event of your choosing so later you can create segments on
onesignal.com to target these users.

<pre>
callback: `onSendTag`
</pre>

```javascript
sdkbox.PluginOneSignal.setEmail(email);
```
> Set email

```javascript
sdkbox.PluginOneSignal.getTags();
```
> Retrieve a list of tags that have been set on the user from the OneSignal server.

<pre>
callback: `onGetTags`
</pre>

```javascript
sdkbox.PluginOneSignal.deleteTag(key);
```
> Deletes a tag that was previously set on a user with sendTag

```javascript
sdkbox.PluginOneSignal.idsAvailable();
```
> Lets you retrieve the OneSignal user id and the Google registration id. Your handler is
called after the device is successfully registered with OneSignal.

<pre>
callback: `onIdsAvailable`
</pre>

```javascript
sdkbox.PluginOneSignal.enableInAppAlertNotification(enable);
```
> By default this is false and notifications will not be shown when the user is in your app,
instead the NotificationOpenedHandler is fired. If set to true notifications will be shown
as native alert boxes if a notification is received when the user is in your app. The
NotificationOpenedHandler is then fired after the alert box is closed.

```javascript
sdkbox.PluginOneSignal.setSubscription(enable);
```
> You can call this method with false to opt users out of receiving all notifications through
OneSignal. You can pass true later to opt users back into notifications.

```javascript
sdkbox.PluginOneSignal.postNotification(jsonString);
```
> Allows you to send notifications from user to user or schedule ones in the future to be
delivered to the current device.

<pre>
callback: `onPostNotification`
</pre>

```javascript
sdkbox.PluginOneSignal.promptLocation();
```
> Prompts the user for location permissions. This allows for geotagging so you can send
notifications to users based on location.

<pre>
Note: Make sure you also have the required location permission in your AndroidManifest.xml.
</pre>


### Listeners
```javascript
onSendTag(success, key, message);
```

```javascript
onGetTags(jsonString);
```

```javascript
onIdsAvailable(userId, pushToken);
```

```javascript
onPostNotification(success, message);
```

```javascript
onNotification(isActive, message, additionalData);
```

```javascript
onNotificationOpened(message);
```

```javascript
onNotificationReceived(message);
```


