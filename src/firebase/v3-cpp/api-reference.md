## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static std::string getVersion ( ) ;
```
>  firebase version.

```cpp
static void setUserProperty(const std::string& name, const std::string& value);
```
> set user property

```cpp
static void setUserID(const std::string& userID);
```
> set user id

```cpp
static void setScreenName(const std::string& screen, const std::string& screenClass);
```
> set current screen

```cpp
static void logEvent(const std::string& event, const std::map<std::string, std::string>& params);
```
> log event
