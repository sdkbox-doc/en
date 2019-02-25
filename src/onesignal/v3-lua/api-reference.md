## API Reference

### Methods
```lua
sdkbox.PluginOneSignal:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginOneSignal:setListener(listener)
```
> Set listener to listen for onesignal events

```lua
sdkbox.PluginOneSignal:registerForPushNotifications()
```
> Only use if you set "auto_register":false in sdkbox_config.json (iOS only)

```lua
--[[
sdkbox.PluginOneSignal.LogLevel.None
sdkbox.PluginOneSignal.LogLevel.Fatal
sdkbox.PluginOneSignal.LogLevel.Error
sdkbox.PluginOneSignal.LogLevel.Warn
sdkbox.PluginOneSignal.LogLevel.Info
sdkbox.PluginOneSignal.LogLevel.Debug
sdkbox.PluginOneSignal.LogLevel.Verbose
]]
sdkbox.PluginOneSignal:setLogLevel(logLevel, visualLogLevel)
```
> Enable logging to help debug if you run into an issue setting up OneSignal. This selector
is static so you can call it before OneSignal init. The following options are available
with increasingly more information;
sdkbox::OneSignalLogNone, sdkbox::OneSignalLogFatal, sdkbox::OneSignalLogError,
sdkbox::OneSignalLogWarn, sdkbox::OneSignalLogInfo, sdkbox::OneSignalLogDebug,
sdkbox::OneSignalLogVerbose

```lua
sdkbox.PluginOneSignal:sendTag(key, value)
```
> Tag a user based on an app event of your choosing so later you can create segments on
onesignal.com to target these users.

<pre>
callback: `onSendTag`
</pre>

```lua
sdkbox.PluginOneSignal:setEmail(email)
```
> Set email

```lua
sdkbox.PluginOneSignal:getTags()
```
> Retrieve a list of tags that have been set on the user from the OneSignal server.

<pre>
callback: `onGetTags`
</pre>

```lua
sdkbox.PluginOneSignal:deleteTag(key)
```
> Deletes a tag that was previously set on a user with sendTag

```lua
sdkbox.PluginOneSignal:idsAvailable()
```
> Lets you retrieve the OneSignal user id and the Google registration id. Your handler is
called after the device is successfully registered with OneSignal.

<pre>
callback: `onIdsAvailable`
</pre>

```lua
sdkbox.PluginOneSignal:enableInAppAlertNotification(enable)
```
> By default this is false and notifications will not be shown when the user is in your app,
instead the NotificationOpenedHandler is fired. If set to true notifications will be shown
as native alert boxes if a notification is received when the user is in your app. The
NotificationOpenedHandler is then fired after the alert box is closed.

```lua
sdkbox.PluginOneSignal:setSubscription(enable)
```
> You can call this method with false to opt users out of receiving all notifications through
OneSignal. You can pass true later to opt users back into notifications.

```lua
sdkbox.PluginOneSignal:postNotification(jsonString)
```
> Allows you to send notifications from user to user or schedule ones in the future to be
delivered to the current device.

<pre>
callback: `onPostNotification`
</pre>

```lua
sdkbox.PluginOneSignal:promptLocation()
```
> Prompts the user for location permissions. This allows for geotagging so you can send
notifications to users based on location.

<pre>
Note: Make sure you also have the required location permission in your AndroidManifest.xml.
</pre>

```lua
sdkbox.PluginOneSignal:setRequiresUserPrivacyConsent(enabled)
```
> For GDPR users, your application should call this method before initialization of the SDK.
If you pass in true, your application will need to call provideConsent(true) before the
OneSignal SDK gets fully initialized.

```lua
sdkbox.PluginOneSignal:consentGranted(enabled)
```
> If you set the SDK to require the user's privacy consent, your application can use this
method once the user does or doesn't provide privacy consent to use the OneSignal SDK.

```lua
sdkbox.PluginOneSignal:requiresUserPrivacyConsent()
```
> You can use this property to check if the OneSignal SDK is waiting for the user to
provide privacy consent.

<pre>
@return [description]
</pre>


### Listeners
```lua
onSendTag(success, key, message)
```

```lua
onGetTags(jsonString)
```

```lua
onIdsAvailable(userId, pushToken)
```

```lua
onPostNotification(success, message)
```

```lua
onNotification(isActive, message, additionalData)
```

```lua
onNotificationOpened(message)
```

```lua
onNotificationReceived(message)
```


