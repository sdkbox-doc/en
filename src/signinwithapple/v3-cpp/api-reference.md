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
static void setListener ( SignInWithAppleListener * listener ) ;
```
> Set listener to listen for SignInWithApple events

```cpp
static SignInWithAppleListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static bool isAvailable ( ) ;
```

```cpp
static void sign ( ) ;
```

```cpp
static void signWithExistingAccount ( ) ;
```


### Listeners
```cpp
void onAuthorizationDidComplete ( const std::string & authInfo );
```

```cpp
void onAuthorizationCompleteWithError ( const std::string & authInfo );
```

```cpp
void onAuthorizationStatus ( const std::string & authState ) {
```


