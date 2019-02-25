## API Reference

### Methods
```lua
sdkbox.PluginMisc:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginMisc:setListener(listener)
```
> Set listener to listen for misc events

```lua
sdkbox.PluginMisc:localNotify(title, content, delayMillisecond)
```
> Local Notification

<pre>
title: notification title, just valid on android
content: notification content
delayMillisecond: delay millisecond to notify, just valid on iOS

return notifyID
</pre>

```lua
sdkbox.PluginMisc:cleanLocalNotify(notifyID)
```
> Clear Local Notification

<pre>
notificationID: notification id, 0: will cancel all local notify
</pre>

```lua
sdkbox.PluginMisc:handleLocalNotify(notificationUserInfo)
```
> Handle Local Notification, just For iOS

<pre>
on Android, please use com.sdkbox.plugin.PluginMisc.onHandleNotification(intent);

</pre>

```lua
sdkbox.PluginMisc:getPlatformName()
```
> get current platform, iOS or Android


```lua
sdkbox.PluginMisc:getMetaData(name)
```
> just valid on android, can get meta data from AndroidManifest.xml


```lua
sdkbox.PluginMisc:getIAPProvider()
```
> get current iap provider of SDKBox IAP
return 'Apple', 'Google', 'Amazon' or 'Playphone'

```lua
sdkbox.PluginMisc:getAppVersion()
```
> get app version

```lua
sdkbox.PluginMisc:getAppBuildVersion()
```
> get iOS app build version

```lua
sdkbox.PluginMisc:getAppVersionCode()
```
> get android app version code

```lua
sdkbox.PluginMisc:getDeviceInfo()
```
> get device info

```lua
sdkbox.PluginMisc:setKeychainService(service)
```
> set keychain service

```lua
sdkbox.PluginMisc:setKeychainAccessGroup(group)
```
> set keychain accessgroup

```lua
sdkbox.PluginMisc:storeStringInKeychain(account, value)
```
> store account data in keychain, if exist will update it
return SecurityFrameworkResultCode: https://developer.apple.com/documentation/security/1542001-security_framework_result_codes

```lua
sdkbox.PluginMisc:fetchStringInKeychain(account)
```
> fetch account data from keychain

```lua
sdkbox.PluginMisc:removeDataInKeychain(account)
```
> remove account in keychain


### Listeners
```lua
onHandleLocalNotify(payloadJson)
```
> Notifies the delegate that user tap the notify


