## API Reference

### Methods
```javascript
sdkbox.PluginMisc.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginMisc.setListener(listener);
```
> Set listener to listen for misc events

```javascript
sdkbox.PluginMisc.localNotify(title, content, delayMillisecond);
```
> Local Notification

<pre>
title: notification title, just valid on android
content: notification content
delayMillisecond: delay millisecond to notify, just valid on iOS

return notifyID
</pre>

```javascript
sdkbox.PluginMisc.cleanLocalNotify(notifyID);
```
> Clear Local Notification

<pre>
notificationID: notification id, 0: will cancel all local notify
</pre>

```javascript
sdkbox.PluginMisc.handleLocalNotify(notificationUserInfo);
```
> Handle Local Notification, just For iOS

<pre>
on Android, please use com.sdkbox.plugin.PluginMisc.onHandleNotification(intent);

</pre>

```javascript
sdkbox.PluginMisc.getPlatformName();
```
> get current platform, iOS or Android


```javascript
sdkbox.PluginMisc.getMetaData(name);
```
> just valid on android, can get meta data from AndroidManifest.xml


```javascript
sdkbox.PluginMisc.getIAPProvider();
```
> get current iap provider of SDKBox IAP
return 'Apple', 'Google', 'Amazon' or 'Playphone'

```javascript
sdkbox.PluginMisc.getAppVersion();
```
> get app version

```javascript
sdkbox.PluginMisc.getAppBuildVersion();
```
> get iOS app build version

```javascript
sdkbox.PluginMisc.getAppVersionCode();
```
> get android app version code

```javascript
sdkbox.PluginMisc.getDeviceInfo();
```
> get device info

```javascript
sdkbox.PluginMisc.setKeychainService(service);
```
> set keychain service

```javascript
sdkbox.PluginMisc.setKeychainAccessGroup(group);
```
> set keychain accessgroup

```javascript
sdkbox.PluginMisc.storeStringInKeychain(account, value);
```
> store account data in keychain, if exist will update it
return SecurityFrameworkResultCode: https://developer.apple.com/documentation/security/1542001-security_framework_result_codes

```javascript
sdkbox.PluginMisc.fetchStringInKeychain(account);
```
> fetch account data from keychain

```javascript
sdkbox.PluginMisc.removeDataInKeychain(account);
```
> remove account in keychain


### Listeners
```javascript
onHandleLocalNotify(payloadJson);
```
> Notifies the delegate that user tap the notify


