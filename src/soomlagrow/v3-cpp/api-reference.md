## API Reference

### Methods
```cpp
static bool init();
```
>  initialize the plugin instance.

```cpp
static void setListener(SoomlaGrowListener* listener);
```
> Set listener to listen for agecheq events

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
>  Refreshed SoomlaInsights information from the server

```cpp
static std::string getUserInsightInfo();
```
>  get user insight info
>  Note: the return may be empty


### Listeners
```cpp
void onHighWayInitialized();
```

>  The delegate named onHighWayInitialized is triggerred once the highway initialized.

```cpp
void onHighWayConnected();
```

>  The delegate named onHighWayConnected is triggerred once the highway connected to server success.

```cpp
void onHighWayDisconnected();
```

>  The delegate named onHighWayDisconnected is triggerred once the highway disconnect to server.

