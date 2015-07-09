### Initialize AdColony
* Call `sdkbox::PluginAdColony::init();` where appropriate in your code. We
recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginAdColony/PluginAdColony.h"
```

### Showing Ads
Display an ad where ever you want from your code:
```cpp
sdkbox::PluginAdColony::show("<AD_NAME>");
```

### Catch AdColony events (optional)
This allows you to catch the `AdColony` events so that you can perform operations such as providing player rewards for watching the video.

* Allow your class to extend `sdkbox::AdColonyListener`
```cpp
#include "PluginAdColony/PluginAdColony.h"
class MyClass : public sdkbox::AdColonyListener
{
private:
  void onAdColonyChange(const std::string& zoneID, bool available);
  void onAdColonyReward(const std::string& zoneID,
                        const std::string& currencyName,
                        int amount, bool success);
  void onAdColonyStarted(const std::string& zoneID);
  void onAdColonyFinished(const sdkbox::AdColonyAdInfo& info);
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginAdColony::setListener(this);
```
