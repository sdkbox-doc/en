### Initialize Achievement
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginAchievement/PluginAchievement.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAchievement::init();
     sdkbox::IAP::init();
}
```

### Using Achievement
#### unlock achievement
```cpp
sdkbox::PluginAchievement::unlock(achievementId);
```
