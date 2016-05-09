## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( OneSignalListener * listener ) ;
```
> Set listener to listen for onesignal events

```cpp
static OneSignalListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void registerForPushNotifications ( ) ;
```
> Only use if you set "auto_register":false in sdkbox_config.json (iOS only)

```cpp
static void setLogLevel ( int logLevel , int visualLogLevel ) ;
```
> Enable logging to help debug if you run into an issue setting up OneSignal. This selector 
is static so you can call it before OneSignal init. The following options are available 
with increasingly more information;
sdkbox::OneSignalLogNone, sdkbox::OneSignalLogFatal, sdkbox::OneSignalLogError, 
sdkbox::OneSignalLogWarn, sdkbox::OneSignalLogInfo, sdkbox::OneSignalLogDebug, 
sdkbox::OneSignalLogVerbose

```cpp
static void sendTag ( const std::string & key , const std::string & value ) ;
```
> Tag a user based on an app event of your choosing so later you can create segments on 
onesignal.com to target these users.

```cpp
static void setEmail ( const std::string & email ) ;
```
> Set email

```cpp
static void getTags ( ) ;
```
> Retrieve a list of tags that have been set on the user from the OneSignal server.

```cpp
static void deleteTag ( const std::string & key ) ;
```
> Deletes a tag that was previously set on a user with sendTag

```cpp
static void idsAvailable ( ) ;
```
> Lets you retrieve the OneSignal user id and the Google registration id. Your handler is 
called after the device is successfully registered with OneSignal.

```cpp
static void enableInAppAlertNotification ( bool enable ) ;
```
> By default this is false and notifications will not be shown when the user is in your app,
instead the NotificationOpenedHandler is fired. If set to true notifications will be shown
as native alert boxes if a notification is received when the user is in your app. The 
NotificationOpenedHandler is then fired after the alert box is closed.

```cpp
static void setSubscription ( bool enable ) ;
```
> You can call this method with false to opt users out of receiving all notifications through 
OneSignal. You can pass true later to opt users back into notifications.

```cpp
static void postNotification ( const std::string & jsonString ) ;
```
> Allows you to send notifications from user to user or schedule ones in the future to be 
delivered to the current device.

```cpp
static void promptLocation ( ) ;
```
> Prompts the user for location permissions. This allows for geotagging so you can send 
notifications to users based on location.


### Listeners
```cpp
void onSendTag ( bool success ,
                 const std::string & key ,
                 const std::string & message ) {
```

```cpp
void onGetTags ( const std::string & jsonString ) {
```

```cpp
void onIdsAvailable ( const std::string & userId ,
                      const std::string & pushToken ) {
```

```cpp
void onPostNotification ( bool success , const std::string & message ) {
```

```cpp
void onNotification ( bool isActive ,
                      const std::string & message ,
                      const std::string & additionalData ) {
```


