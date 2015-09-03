## API Reference

### Methods
```javascript
sdkbox.PluginKochava.init();
```
> init the kochava service

```javascript
sdkbox.PluginKochava.shutdown();
```
> shutdown the kochava service

```javascript
sdkbox.PluginKochava.enableLogging(enabled);
```
> enable kochava api logging

```javascript
sdkbox.PluginKochava.trackEvent(event, value);
```
> track a single event

```javascript
sdkbox.PluginKochava.spatialEvent(title, x, y, z);
```
> spatial event to help visualize data

```javascript
sdkbox.PluginKochava.setLimitAdTracking(limitAdTracking);
```
> turn on/off ad tracking

```javascript
sdkbox.PluginKochava.retrieveAttribution();
```
> returns the attribution data

```javascript
sdkbox.PluginKochava.sendDeepLink(url, application);
```
> send a referral to where your app was opened from.

```javascript
sdkbox.PluginKochava.setBeaconCallback(callback);
```
> specify beacon transition callback


### Listeners

