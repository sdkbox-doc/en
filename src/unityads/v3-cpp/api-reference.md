## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( UnityAdsListener * listener ) ;
```
> Set listener to listen for unityads events

```cpp
static UnityAdsListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static bool isSupported();
```
> is unityads support current platform

```cpp
static bool isReady(const std::string& placementId);
```
> is unityads ready to show

```cpp
static void show(const std::string& placementId);
```
> show unityads

```cpp
static SBUnityAdsPlacementState getPlacementState(const std::string& placementId);
```
> unityads placement state


### Listeners

```cpp
void unityAdsDidClick(const std::string& placementId);
```
> unityads clicked

```cpp
void unityAdsPlacementStateChanged(const std::string& placementId,
                                PluginUnityAds::SBUnityAdsPlacementState oldState,
                                PluginUnityAds::SBUnityAdsPlacementState newState);
```
> unityads placement state changed

```cpp
void unityAdsReady(const std::string& placementId);
```
> unityads ready

```cpp
void unityAdsDidError(PluginUnityAds::SBUnityAdsError error, const std::string& message);
```
> unityads error

```cpp
void unityAdsDidStart(const std::string& placementId);
```
> unityads start

```cpp
void unityAdsDidFinish(const std::string& placementId, PluginUnityAds::SBUnityAdsFinishState state);
```
> unityads finish
