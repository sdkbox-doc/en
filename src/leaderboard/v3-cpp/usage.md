### Initialize Leaderboard
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginLeaderboard/PluginLeaderboard.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginLeaderboard::init();
}
```

### Using Leaderboard
#### Submit score
```cpp
sdkbox::PluginLeaderboard::submitScore(leaderboardId, score);
```

#### Get current score
sdkbox::PluginLeaderboard::getLeaderboard(leaderboardId);


### Leaderboard events
This allows you to catch `Leaderboard` events so that you can perform operations after Leaderboard events have occurred.

* Allow your class to extend `sdkbox::LeaderboardListener` and override the functions listed:
```cpp
#include "PluginLeaderboard/PluginLeaderboard.h"
class MyClass : public sdkbox::LeaderboardListener
{
    void onComplete ( std::string leaderboard ) {}
    void onFail ( ) {}
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginLeaderboard::setListener(this);
```
