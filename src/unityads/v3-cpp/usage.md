### Initialize UnityAds
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginUnityAds/PluginUnityAds.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginUnityAds::init();
}
```

### Show Ads
After initialization you can begin to use the UnityAds functionality:
```cpp

std::string ad = "";
if (sdkbox::PluginUnityAds::isReady(ad)) {
    sdkbox::PluginUnityAds::show(ad);
} else {
    CCLOG("unityads is not ready");
}
```

### Catch UnityAds events (optional)
This allows you to catch the `UnityAds` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::UnityAdsListener`
```cpp
#include "PluginUnityAds/PluginUnityAds.h"
class MyClass : public sdkbox::UnityAdsListener {
public:

    void unityAdsDidClick(const std::string& placementId) {
        CCLOG("unityads click %s", placementId.c_str());
    }

    void unityAdsPlacementStateChanged(const std::string& placementId,
                                PluginUnityAds::SBUnityAdsPlacementState oldState,
                                PluginUnityAds::SBUnityAdsPlacementState newState) {
        CCLOG("unityads state change %s %d->%d", placementId.c_str(), oldState, newState);
    }

    void unityAdsReady(const std::string& placementId) {
        CCLOG("unityads ready %s", placementId.c_str());
    }

    void unityAdsDidError(sdkbox::PluginUnityAds::SBUnityAdsError error, const std::string& message) {
        CCLOG("unityads error %d %s", error, message.c_str());
    }

    void unityAdsDidStart(const std::string& placementId) {
        CCLOG("unityads start %s", placementId.c_str());
    }

    void unityAdsDidFinish(const std::string& placementId, sdkbox::PluginUnityAds::SBUnityAdsFinishState state) {
        CCLOG("unityads finish %d %s", state, placementId.c_str());
    }

};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginUnityAds::setListener(this);
```
