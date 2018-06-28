## API Reference

### Methods
```javascript
sdkbox.firebase.Analytics.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.firebase.Analytics.getVersion();
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```javascript
sdkbox.firebase.Analytics.setUserProperty(name, value);
```

```javascript
sdkbox.firebase.Analytics.setUserID(userID);
```

```javascript
sdkbox.firebase.Analytics.setScreenName(screen, screenClass);
```

```javascript
sdkbox.firebase.Analytics.logEvent(event, params);
```

```javascript
sdkbox.firebase.Analytics.resetAnalyticsData();
```
> Clears all analytics data for this instance from the device and resets the app instance ID.
FIRAnalyticsConfiguration values will be reset to the default values.

```javascript
sdkbox.firebase.Analytics.setAnalyticsCollectionEnabled(enabled);
```
> Sets whether analytics collection is enabled for this app on this device.
This setting is persisted across app sessions. By default it is enabled. (Only for Android)


### Listeners

