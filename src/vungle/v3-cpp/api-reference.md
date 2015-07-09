## API Reference

### Methods
```cpp
static void init();
```
> initialize the plugin instance.

```cpp
static void show(const std::string& name);
```
> show ad with a provided name.

```cpp
static void setListener(VungleListener* listener);
```
> set provided listener.

```cpp
static void removeListener();
```
> remove listeners.

```cpp
static void setDebug(bool enable);
```
> enable or disable debug mode.

```cpp
static bool isCacheAvailable();
```
> is there a cached video available.

```cpp
static void setUserID(const std::string& userID);
```
> sets the userID for rewarded ads.

### Listeners
```cpp
void onVungleStarted();
```
> Vungle is running and available.

```cpp
void onVungleFinished();
```
> Vungle is not running/has stopped.

```cpp
void onVungleOpenStore();
```
> is the Vungle store available.

```cpp
void onVungleCacheAvailable();
```
> ad cache is available.
