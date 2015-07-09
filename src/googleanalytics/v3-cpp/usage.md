### Initialize Google Analytics
Call `sdkbox::PluginGoogleAnalytics::init();` where appropriate in your code.
We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the
appropriate headers:
```cpp
#include "PluginGoogleAnalytics/PluginGoogleAnalytics.h"
```
