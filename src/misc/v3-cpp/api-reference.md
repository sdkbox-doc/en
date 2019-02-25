## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( MiscListener * listener ) ;
```
> Set listener to listen for misc events

```cpp
static MiscListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static int localNotify ( const std::string & title ,
                         const std::string & content ,
                         int delayMillisecond ) ;
```
> Local Notification

<pre>
title: notification title, just valid on android
content: notification content
delayMillisecond: delay millisecond to notify, just valid on iOS

return notifyID
</pre>

```cpp
static void cleanLocalNotify ( int notifyID = 0 ) ;
```
> Clear Local Notification

<pre>
notificationID: notification id, 0: will cancel all local notify
</pre>

```cpp
static void handleLocalNotify ( const std::string & notificationUserInfo ) ;
```
> Handle Local Notification, just For iOS

<pre>
on Android, please use com.sdkbox.plugin.PluginMisc.onHandleNotification(intent);

</pre>

```cpp
static std::string getPlatformName ( ) ;
```
> get current platform, iOS or Android


```cpp
static std::string getMetaData ( const std::string & name ) ;
```
> just valid on android, can get meta data from AndroidManifest.xml


```cpp
static std::string getIAPProvider ( ) ;
```
> get current iap provider of SDKBox IAP
return 'Apple', 'Google', 'Amazon' or 'Playphone'

```cpp
static std::string getAppVersion ( ) ;
```
> get app version

```cpp
static std::string getAppBuildVersion ( ) ;
```
> get iOS app build version

```cpp
static int getAppVersionCode ( ) ;
```
> get android app version code

```cpp
static std::string getDeviceInfo ( ) ;
```
> get device info

```cpp
static void setKeychainService ( const std::string & service ) ;
```
> set keychain service

```cpp
static void setKeychainAccessGroup ( const std::string & group ) ;
```
> set keychain accessgroup

```cpp
static int storeStringInKeychain ( const std::string & account ,
                                   const std::string & value ) ;
```
> store account data in keychain, if exist will update it
return SecurityFrameworkResultCode: https://developer.apple.com/documentation/security/1542001-security_framework_result_codes

```cpp
static const std::string fetchStringInKeychain ( const std::string & account ) ;
```
> fetch account data from keychain

```cpp
static int removeDataInKeychain ( const std::string & account ) ;
```
> remove account in keychain


### Listeners
```cpp
void onHandleLocalNotify ( const std::string & payloadJson ) 
```
> Notifies the delegate that user tap the notify


