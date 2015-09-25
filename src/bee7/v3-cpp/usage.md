### Initialize Bee7
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginBee7/PluginBee7.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginBee7::init();
}
```

### Using Bee7
#### Show Game Wall
```cpp
sdkbox::PluginBee7::showGameWall();
```

### Bee7 events
This allows you to catch `Bee7` events so that you can perform operations after Bee7 events have occurred.

* Allow your class to extend `sdkbox::Bee7Listener` and override the functions listed:
```cpp
#include "PluginBee7/PluginBee7.h"
class MyClass : public sdkbox::Bee7Listener
{
    void onAvailableChange(bool available) = 0;
    void onVisibleChange(bool available) = 0;
    void onGameWallWillClose() = 0;
    void onGiveReward(long bee7Points,
                      long virtualCurrencyAmount,
                      const std::string& appId,
                      bool cappedReward,
                      long campaignId,
                      bool videoReward) = 0;
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginBee7::setListener(this);
```
