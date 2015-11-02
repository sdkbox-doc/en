### Initialize Achievement
Before initializing achievements for Playphone:
  - Register as a Playphone developer in the [Playphone Developer Portal](http://developer.playphone.com)
  - Create a new game and setup achievements for that game in the [Playphone
   Developer Portal](https://developer.playphone.com/games).
  - Setup Playphone configuration by following the JSON Configuration step as outlined in [Playphone plugin documentation](http://sdkbox- staging.github.io/en/plugins/playphone/v3 -cpp/#extra-steps)
   
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
