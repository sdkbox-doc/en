### Initialize PhunwareAds
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginPhunwareAds/PluginPhunwareAds.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginPhunwareAds::init();
}
```

### Showing Ads
Display an ad where ever you want from your code:
```cpp
// To use customized location
sdkbox::PluginPhunwareAds::show("your_ad_name");
```

### Cache Ads
```cpp
sdkbox.PluginPhunwareAds::cache("your_ad_name")
```

### Hide Ads
```cpp
sdkbox.PluginPhunwareAds::hide("your_ad_name")
```

### Catch PhunwareAds events (optional)
This allows you to catch the `PhunwareAds` events so that you can perform operations such as providing player rewards for watching the video.

* Allow your class to extend `sdkbox::PhunwareAdsListener`
```cpp
#include "PluginPhunwareAds/PluginPhunwareAds.h"
class MyClass : public sdkbox::PhunwareAdsListener
{
public:
    void adLoaded(const std::string& name) {}
    void adFailed(const std::string& name, int errorCode, const std::string& msg) {}
    void adWillPresent(const std::string& name) {}
    void adDidPresent(const std::string& name) {}
    void adWillDissmiss(const std::string& name) {}
    void adDidDismiss(const std::string& name) {}
    void willLeaveApp(const std::string& name) {}
    void reward(const std::string& name, float amount, const std::string& currency) {}

};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginPhunwareAds::setListener(this);
```
