## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( FacebookListener * listener ) ;
```
> Set listener to listen for facebook events

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
static void requestReadPermissions ( const std::vector <std::string> & permissions ) ;
```
> log in with specific read permissions, conflict with publish permissions
https://developers.facebook.com/docs/facebook-login/permissions

```cpp
static void requestPublishPermissions ( const std::vector <std::string> & permissions ) ;
```
> log in with specific public permissions
https://developers.facebook.com/docs/facebook-login/permissions

```cpp
static void logout ( ) ;
```
> log out

```cpp
static bool isLoggedIn ( ) ;
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
static std::vector <std::string> getPermissionList ( ) ;
```
> get permissoin list

```cpp
static void share ( const FBShareInfo & info ) ;
```
> share

```cpp
static void dialog ( const FBShareInfo & info ) ;
```
> open a dialog of Facebook app or WebDialog (dialog with photo only avaible with native Facebook app)

```cpp
static std::string getSDKVersion ( ) ;
```
> return the version of Facebook SDK

```cpp
static void api ( const std::string & path ,
                  const std::string & method ,
                  const FBAPIParam & params ,
                  const std::string & tag ) ;
```
> use Facebook Open Graph api
https://developers.facebook.com/docs/ios/graph

```cpp
static void fetchFriends ( ) ;
```
> fetch friends data from Facebook

```cpp
static std::vector <FBGraphUser> getFriends ( ) ;
```
> get friends info


### Listeners
```cpp
void onLogin ( bool isLogin , const std::string & msg );
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

```cpp
void onAPI ( const std::string & key , const std::string & jsonData );
```

```cpp
void onPermission ( bool isLogin , const std::string & msg );
```

```cpp
void onFetchFriends ( bool ok , const std::string & msg );
```


