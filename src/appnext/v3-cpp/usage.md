### Initialize Appnext
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```cpp
#include "PluginAppnext/PluginAppnext.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAppnext::init();
}
```

### cache ad/video

```cpp
sdkbox::PluginAppnext::cacheAd("default");
sdkbox::PluginAppnext::cacheVideo("fullscreen");
```
**NOTE** : Appnext ads needs to be cached before use, auto-caching is not available with this plugin. It might take couple of minutes to cache ads, once cached you would be able to see the ads. While caching, ads are not available.


### refresh ad/video

```
sdkbox::PluginAppnext::refreshAds();
sdkbox::PluginAppnext::refreshVideo("fullscreen");
```
**NOTE** : refresh ad or video after it is closed.


### show ad/video
```cpp
sdkbox::PluginAppnext::showAd("default");
sdkbox::PluginAppnext::showVideo("fullscreen");
```

### hide ad
```cpp
sdkbox::PluginAppnext::hideAd();
```

### check ad/video available
```cpp
sdkbox::PluginAppnext::isAdReady();
sdkbox::PluginAppnext::isVideoReady("fullscreen");
```

### Implement AppnextListner
* You can implement AppnextListener if you want to receive callbacks like video finish playing.
```cpp
#include "PluginAppnext/PluginAppnext.h"
class MyClass : public sdkbox::AppnextListener
{
private:
    void onAdError(const std::string& msg) {}
    void onAdLoaded() {}
    void onAdOpened() {} // not support on android
    void onAdClosed() {}
    void onAdClicked() {}

    void onVideoLoaded(const std::string& name) {}
    void onVideoClicked(const std::string& name) {}
    void onVideoClosed(const std::string& name) {}
    void onVideoEnded(const std::string& name) {} // not support on ios
    void onVideoError(const std::string& name, const std::string& msg) {}
}
```
