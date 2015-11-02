### Register Javascript Functions
You need to register all the Achievement JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAchievementJS.hpp"
#include "PluginAchievementJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginAchievementJS);
sc->addRegisterCallback(register_all_PluginAchievementJS_helper);
```

### Initialize Achievement
Before initializing achievements for Playphone:

  - Register as a Playphone developer in the [Playphone Developer Portal](http://developer.playphone.com)
  - Create a new game and setup achievements for that game in the [Playphone
   Developer Portal](https://developer.playphone.com/games).
  - Setup Playphone configuration by following the JSON Configuration step as outlined in [Playphone plugin documentation](http://sdkbox- staging.github.io/en/plugins/playphone/v3 -cpp/#extra-steps)

Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginAchievement.init();
sdkbox.IAP.init();
```

### Using Achievement
#### unlock achievement
```javascript
sdkbox.PluginAchievement.unlock(achievementId);
```
