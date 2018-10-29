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
static std::string localNotify ( const std::string & title, const std::string & content, int delaymisillensecond ) ;
```
> send a local notification
@return notification id

### Listeners
```cpp
void onHandleLocalNotify ( const std::string & payloadJson ) 
```


