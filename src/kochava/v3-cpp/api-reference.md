## API Reference

### Methods
```cpp
static void init();
```
> initialize the Kochava service.

```cpp
static void shutdown();
```
> shutdown the Kochava service.

```cpp
static void enableLogging(bool enabled);
```
> log? true or false.

```cpp
static void trackEvent(const char* event, const char* value);
```
> track a single event, specifying the event and value.

```cpp
static void identityLinkEvent(const std::map<std::string, std::string>& data);
```
> link one or more udid's to a Kochava id.

```cpp
static void spatialEvent(const char* title, float x, float y, float z);
```
> event specifying x, y, and z coordinate to Kochava server for visualizing your data.

```cpp
static void setLimitAdTracking(bool limitAdTracking);
```
> turn ad tracking off or on by using true or false.

```cpp
const std::map<std::string, std::string>& retrieveAttribution() const;
```
> returns the attribution data.

```cpp
void sendDeepLink(const char* url, const char* application);
```
> send a referral to where your app was opened from.
