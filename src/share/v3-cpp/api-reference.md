## API Reference

### Methods
```cpp
static bool init ( ) ;
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
static void share ( const ShareInfo & info ) ;
```
> Share content


### Listeners
```cpp
void onShareState ( const PluginShare::ShareResponse & response ) {
```
> Notifies the delegate that share completion


