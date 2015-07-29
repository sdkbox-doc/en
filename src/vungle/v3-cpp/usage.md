### Initialize Vungle
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```cpp
#include "PluginVungle/PluginVungle.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginVungle::init();
}
```

### Showing Ads
Display an ad where ever you want from your code, either __video__ or __reward__:
```cpp
sdkbox::PluginVungle::show("video");
sdkbox::PluginVungle::show("reward");
```

### Catch Vungle events (optional)
This allows you to catch the `Vungle` events so that you can pause or resume
your game.

* Allow your class to extend `sdkbox::VungleListener`
```cpp
#include "PluginVungle/PluginVungle.h"
class MyClass : public sdkbox::VungleListener
{
private:
  void onVungleCacheAvailable();
  void onVungleStarted();
  void onVungleFinished();
  void onVungleAdViewed(bool isComplete);
}
```

* Create a __listener__ that handles callbacks (optional):
```cpp
sdkbox::PluginVungle::setListener(this);
```
