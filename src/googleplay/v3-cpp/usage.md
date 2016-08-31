##Usage
### Initialize Google Analytics
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginGoogleAnalytics/PluginGoogleAnalytics.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginGoogleAnalytics::init();
}
```

You can always manually stop recording events at any time by calling:
```cpp
sdkbox::PluginGoogleAnalytics::stopSession();
```

However, in-order to record events again you must then manually call:
```cpp
sdkbox::PluginGoogleAnalytics::startSession();
```

Logged data usually shows up within one day.
