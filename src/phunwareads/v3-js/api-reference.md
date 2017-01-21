## API Reference

### Methods
```javascript
sdkbox.PluginPhunwareAds.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginPhunwareAds.setListener(listener);
```
> Set listener to listen for phunware events

```javascript
sdkbox.PluginPhunwareAds.cache(name);
```
> cache ad by specifying ad name, auto cache default.

```javascript
sdkbox.PluginPhunwareAds.isAvailable(name);
```
> is the specified ad available?

```javascript
sdkbox.PluginPhunwareAds.show(name);
```
> show ad by specifying ad name.

```javascript
sdkbox.PluginPhunwareAds.hide(name);
```
> hide ad by specifying ad name.

```javascript
sdkbox.PluginPhunwareAds.setUserID(userID);
```
> set user ID for rewarded video.

```javascript
sdkbox.PluginPhunwareAds.getRemainingViews(name);
```
> get remaining views of rewarded video.


### Listeners
```javascript
adLoaded(name);
```
> there is cached content

```javascript
adFailed(name, errorCode, msg);
```
> there is error when cache content

```javascript
adWillPresent(name);
```
> ad will present

```javascript
adDidPresent(name);
```
> ad did present

```javascript
adWillDissmiss(name);
```
> ad will dissmiss

```javascript
adDidDismiss(name);
```
> ad did dismiss

```javascript
willLeaveApp(name);
```
> will leave application

```javascript
reward(name, amount, currency);
```
> reward user with specifying ad name


