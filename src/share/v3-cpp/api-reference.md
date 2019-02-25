## API Reference

### Methods
```cpp
static bool init ( const char * jsonConfig = 0 ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( ShareListener * listener ) ;
```
> Set listener to listen for share events

```cpp
static ShareListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void setSharePanelTitle ( const std::string & s ) ;
```
> set custome share platform choose panel title, default is "Share to"

```cpp
static void setSharePanelCancel ( const std::string & s ) ;
```
> set custome share platform choose panel cancel button, default is "Cancel"

```cpp
static void share ( const sdkbox::SocialShareInfo & info ) ;
```
> Share content

```cpp
static void nativeShare ( const sdkbox::SocialShareInfo & info ) ;
```
> will use ios/android system share panel

<pre>
IOS:
when trigger share success event, action name will pass by error in sdkbox::SocialShareResponse
Android:
share success event will trigger, but this is not real share success, just show share panel success
can't get real share success event on android
</pre>

```cpp
static void logoutTwitter ( ) ;
```

```cpp
static void setFileProviderAuthorities ( const std::string & authority ) ;
```


### Listeners
```cpp
void onShareState ( const sdkbox::SocialShareResponse & response ) 
```
> Notifies the delegate that share completion


