## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( ReviewListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static ReviewListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void show ( bool force = false ) ;
```
> Tells 'SDKBox review plugin' to try and show the prompt (a rating alert).
if you call `show` with `false` or null params,
the prompt will be showed if there is connection available,
the user hasn't declined to rate or hasn't rated current version.
if the item `tryPromptWhenInit` in sdkbox.config is false, you can call this try to show prompt
if you call `show` with `true` params
the prompt will be showed without checks (the prompt is always displayed).
The case where you should call this is if your app has an
explicit "Rate this app" command somewhere. This is similar to rateApp,
but instead of jumping to the review directly, an intermediary prompt is displayed.
another case is for debug

```cpp
static void userDidSignificantEvent ( bool canPromptForRating ) ;
```

```cpp
static void setTitle ( const std::string & title ) ;
```

```cpp
static void setMessage ( const std::string & message ) ;
```

```cpp
static void setCancelButtonTitle ( const std::string & cancelTitle ) ;
```

```cpp
static void setRateButtonTitle ( const std::string & rateTitle ) ;
```

```cpp
static void setRateLaterButtonTitle ( const std::string & rateLaterTitle ) ;
```


### Listeners
```cpp
void onDisplayAlert ( );
```
> trigger when alert prompt show

```cpp
void onDeclineToRate ( );
```
> trigger when user refuse to rate

```cpp
void onRate ( );
```
> trigger when user want to rate

```cpp
void onRemindLater ( );
```
> trigger when user want to remind later


