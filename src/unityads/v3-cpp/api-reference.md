## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( UnityAdsListener * listener ) ;
```
> Set listener to listen for inmobi events

```cpp
static UnityAdsListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static bool isSupported ( ) ;
```

```cpp
static bool isReady ( const std::string & placementId ) ;
```

```cpp
static void show ( const std::string & placementId ) ;
```

```cpp
static SBUnityAdsPlacementState getPlacementState ( const std::string & placementId ) ;
```

```cpp
static void setGDPR ( bool enabled ) ;
```
> Enable GDPR

```cpp
static void setServerId ( const std::string & sid ) ;
```


### Listeners
```cpp
void unityAdsDidClick ( const std::string & placementId ) 
```

```cpp
void unityAdsPlacementStateChanged ( const std::string & placementId ,
                                     PluginUnityAds::SBUnityAdsPlacementState oldState ,
                                     PluginUnityAds::SBUnityAdsPlacementState newState ) 
```

```cpp
void unityAdsReady ( const std::string & placementId ) 
```

```cpp
void unityAdsDidError ( PluginUnityAds::SBUnityAdsError error ,
                        const std::string & message ) 
```

```cpp
void unityAdsDidStart ( const std::string & placementId ) 
```

```cpp
void unityAdsDidFinish ( const std::string & placementId ,
                         PluginUnityAds::SBUnityAdsFinishState state ) 
```


