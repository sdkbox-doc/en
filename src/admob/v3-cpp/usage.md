### Initialize AdMob
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```cpp
#include "PluginAdMob/PluginAdMob.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAdMob::init();
}
```

### cache ad
```cpp
sdkbox::PluginAdMob::cache("home");
sdkbox::PluginAdMob::cache("gameover");
```

### show ad
```cpp
sdkbox::PluginAdMob::show("home");
sdkbox::PluginAdMob::show("gameover");
```

### hide ad
You can not hide an interstitial ad
```cpp
sdkbox::PluginAdMob::hide("home");
```

### check ad available
```cpp
sdkbox::PluginAdMob::isAvailable("home");
sdkbox::PluginAdMob::isAvailable("gameover");
```

### Implement AdMobListner
* You can implement AdMobListener if you want to receive callbacks like video finish playing.
```cpp
#include "PluginAdMob/PluginAdMob.h"
class MyClass : public sdkbox::AdMobListener
{
private:
    void adViewDidReceiveAd(const std::string &name) {}
    void adViewDidFailToReceiveAdWithError(const std::string &name, const std::string &msg) {}
    void adViewWillPresentScreen(const std::string &name) {}
    void adViewDidDismissScreen(const std::string &name) {}
    void adViewWillDismissScreen(const std::string &name) {}
    void adViewWillLeaveApplication(const std::string &name) {}
}
```
