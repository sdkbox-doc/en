## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( FacebookListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static FacebookListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void login ( ) ;
```
> log in

```cpp
static void logInWithReadPermissions ( const std::string & permissions ) ;
```
> log in with specific read permissions, conflict with publish permissions
https://developers.facebook.com/docs/facebook-login/permissions

```cpp
static void logInWithPublishPermissions ( const std::string & permissions ) ;
```
> log in with specific public permissions
https://developers.facebook.com/docs/facebook-login/permissions

```cpp
static void logout ( ) ;
```
> log out

```cpp
static bool isLogined ( ) ;
```
> Check whether the user logined or not

```cpp
static std::string getUserID ( ) ;
```
> get UserID

```cpp
static std::string getAccessToken ( ) ;
```
> get AccessToken

```cpp
static std::string getPermissionList ( ) ;
```
> get permissoin list

```cpp
static void share ( FBInfo & info ) ;
```
> share

```cpp
static void dialog ( FBInfo & info ) ;
```
> open a dialog of Facebook app

```cpp
static void api ( const std::string & path ,
                  const std::string & method ,
                  FBInfo & params ,
                  const std::string & tag ) ;
```
> use Facebook Open Graph api
https://developers.facebook.com/docs/ios/graph

```cpp
static void activateApp ( ) ;
```
> Notifies the events system that the app has launched & logs an activatedApp event.

```cpp
static std::string getSDKVersion ( ) ;
```
> @breif return the version of Facebook SDK for Cocos


### Listeners
```cpp
void onLogin ( bool isLogin , const std::string & error );
```

```cpp
void onAPI ( const std::string & key , const std::string & jsonData );
```

```cpp
void onSharedSuccess ( const std::string & message );
```

```cpp
void onSharedFailed ( const std::string & message );
```

```cpp
void onSharedCancel ( );
```
