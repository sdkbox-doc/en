## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( PhunwareMessagingListener * listener ) ;
```
> Set listener to listen for phunwaremessaging events

```cpp
static PhunwareMessagingListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void read ( const std::string & messageID ) ;
```

```cpp
static void remove ( const std::string & messageID ) ;
```

```cpp
static std::vector <sdkbox::PWMSGZoneMessage> messages ( ) ;
```

```cpp
static std::string deviceId ( ) ;
```

```cpp
static std::string serviceName ( ) ;
```

```cpp
static std::string version ( ) ;
```


### Listeners
```cpp
void init ( bool success , const std::string & message ) {
```
> Notifies the delegate that the module has finished loading

```cpp
void error ( const std::string & message ) {
```


