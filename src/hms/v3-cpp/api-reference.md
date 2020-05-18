## API Reference

### Methods
```cpp
static void setGDPR ( bool enabled ) ;
```
> Set GDPR

```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( HMSListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static HMSListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void login ( int loginType ) ;
```
> HMS provider three way to login
loginType: 0, slient login 1, login with HuaweiID(ID Token) 2, login with HuaweID(Authorization Code)

```cpp
static void logout ( ) ;
```
> logout HMS


### Listeners
```cpp
void onLogin ( int code , const std::string & msg );
```


