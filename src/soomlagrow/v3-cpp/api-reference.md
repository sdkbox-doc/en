## API Reference

### Methods
```cpp
static bool init();
```
>  initialize the plugin instance.

```cpp
static void setListener(SoomlaGrowListener* listener);
```
> Set listener to listen for different events (list below)

```cpp
static SoomlaGrowListener* getListener();
```
> Get the listener

```cpp
static void removeListener();
```
> Remove the listener, and can't listen to events anymore

```cpp
static void refreshInsight();
```
>  Refreshed GROW's Insights information from the server

```cpp
static std::string getUserInsightInfo();
```
>  get user insight info
>  Note: the returned value may be empty


### Listeners
```cpp
void onHighWayInitialized();
```

>  This event is triggered once the highway initialized.

```cpp
void onHighWayConnected();
```

>  This event is triggered once the highway is connected to server.

```cpp
void onHighWayDisconnected();
```

>  This event is triggered once the highway disconnect from the server.
