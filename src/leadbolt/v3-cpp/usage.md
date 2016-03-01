### Initialize LeadBolt
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginLeadBolt/PluginLeadBolt.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginLeadBolt::init();
}
```

### Cache Ad
```cpp
sdkbox::PluginLeadbolt::loadModuleToCache("directdeal");
sdkbox::PluginLeadbolt::loadModuleToCache("rewardedvideo");
```
> Note: Leadbolt ads are cached before use for better user experience. Please allow time for ads to be cached.  Once an ad is cached, you will be able to see the ad. While caching is in progress, ads are not available for display.

### Load/Display Ad
```cpp
sdkbox::PluginLeadbolt::loadModule("directdeal");
sdkbox::PluginLeadbolt::loadModule("rewardedvideo");
```

### Check if Ad is available
```cpp
sdkbox::PluginLeadbolt::isAdReady("directdeal");
sdkbox::PluginLeadbolt::isAdReady("rewardedvideo");
```

### Catch LeadBolt events (optional)
This allows you to catch the LeadBolt ad events so that you can perform operations based upon responses. With rewarded video, the onMediaFinished event allows you to reward players for watching the video.

* Allow your class to extend `sdkbox::LeadBoltListener`
```cpp
#include "PluginLeadBolt/PluginLeadBolt.h"

class LBListener : public sdkbox::LeadBoltListener {
public:

    void onModuleLoaded(const std::string& placement);
    void onModuleClosed(const std::string& placement);
    void onModuleClicked(const std::string& placement);
    void onModuleCached(const std::string& placement);
    void onModuleFailed(const std::string& placement, const std::string& error, bool iscached);
    void onMediaFinished(bool viewCompleted);

};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginLeadBolt::setListener(this);
```
