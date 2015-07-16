### Initialize AdColony
* Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginAdColony/PluginAdColony.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAdColony::init();
}
```

### Showing Ads
Display an ad wherever you want from your code, by specifying ad type:
```cpp
sdkbox::PluginAdColony::show("video");
```
or:
```cpp
sdkbox::PluginAdColony::show("v4vc");
```

### Catch AdColony events (optional)
This allows you to catch the `AdColony` events so that you can perform operations such as providing player rewards for watching the video.

* Allow your class to extend `sdkbox::AdColonyListener`
```cpp
#include "PluginAdColony/PluginAdColony.h"
class MyClass : public sdkbox::AdColonyListener
{
private:
  void onAdColonyChange(const sdkbox::AdColonyAdInfo& info, bool available);
  void onAdColonyReward(const sdkbox::AdColonyAdInfo& info,
		const std::string& currencyName, int amount, bool success);
  void onAdColonyStarted(const sdkbox::AdColonyAdInfo& info);
  void onAdColonyFinished(const sdkbox::AdColonyAdInfo& info);
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginAdColony::setListener(this);
```
