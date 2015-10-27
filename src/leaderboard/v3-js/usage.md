### Register Javascript Functions
You need to register all the Leaderboard JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginLeaderboardJS.hpp"
#include "PluginLeaderboardJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginLeaderboardJS);
sc->addRegisterCallback(register_all_PluginLeaderboardJS_helper);
```

### Initialize Leaderboard
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginLeaderboard.init();
```

### Using Leaderboard
#### Submit score
```javascript
sdkbox.PluginLeaderboard.submitScore(leaderboardId, score);
```

#### Get current score
```javascript
sdkbox.PluginLeaderboard.getLeaderboard(leaderboardId);
```

### Leaderboard events
This allows you to catch `Leaderboard` events so that you can perform operations after Leaderboard events have occurred.

```javascript
sdkbox.PluginLeaderboard.setListener({
	onComplete: function(leaderboard) {},
	onFail: function() {}
});
```
