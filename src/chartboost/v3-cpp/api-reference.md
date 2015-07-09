## API Reference

### Methods
```cpp
static void init();
```
> initialize the plugin instance.

```cpp
static void show(const std::string& name);
```
> show ad by specifying ad name.

```cpp
static void setListener(ChartboostListener* listener);
```
> creates the an optional listener.

```cpp
static void removeListener();
```
> removed the listener.

```cpp
static bool isAnyViewVisible();
```
> check to see if any views are visible.

```cpp
static bool isAvailable(const std::string& name);
```
> is the specified ad available?

```cpp
static void setAutoCacheAds(bool shouldCache);
```
> set to enable and disable the auto cache feature (Enabled by default).

```cpp
static bool getAutoCacheAds();
```
> get the current auto cache behavior (Enabled by default).

```cpp
static void closeImpression();
```
> close any visible Chartboost impressions (interstitials, more apps, rewarded
video, etc..) and the loading view (if visible).

```cpp
static void setStatusBarBehavior(CB_StatusBarBehavior behavior);
```
> set to control how the fullscreen ad units should interact with the status bar. (CBStatusBarBehaviorIgnore by default).

```cpp
static void didPassAgeGate(bool pass);
```
> confirm if an age gate passed or failed. When specified Chartboost will wait for
 this call before showing the IOS App Store.

```cpp
static void setShouldPauseClickForConfirmation(bool shouldPause);
```
> decide if Chartboost SDK should block for an age gate.

```cpp
static bool handleOpenURL(const std::string& url, const std::string& sourceApp);
```
> opens a "deep link" URL for a Chartboost Custom Scheme.

```cpp
static void setCustomID(const std::string& customID);
```
> set a custom identifier to send in the POST body for all Chartboost API server
requests.

```cpp
static std::string getCustomID();
```
> get the current custom identifier being sent in the POST body for all Chartboost
API server requests.

```cpp
static void setShouldRequestInterstitialsInFirstSession(bool shouldRequest);
```
> decide if Chartboost SDK should show interstitials in the first session.

```cpp
static void setShouldDisplayLoadingViewForMoreApps(bool shouldDisplay);
```
> decide if Chartboost SDK should show a loading view while preparing to display
the "more applications" UI.

```cpp
static void setShouldPrefetchVideoContent(bool shouldPrefetch);
```
> decide if Chartboost SDK will attempt to fetch videos from the Chartboost API
servers.
