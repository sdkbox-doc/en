### Initialize Flurry Analytics
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. `init()` and `startSession()` are required. Example:
```cpp
#include "PluginFlurryAnalytics/PluginFlurryAnalytics.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFlurryAnalytics::init();
     // start session
     sdkbox::PluginFlurryAnalytics::startSession();
}
```

### Using Flurry Analytics
After initialization you can begin to use the Flurry Analytics functionality. Use `logevent` where ever you want from your code:
```cpp
std::string eventName = "test event1";
sdkbox::PluginFlurryAnalytics::logEvent(eventName);
```

### Ending Flurry Analytics (Android only)
When you are finished using `FlurryAnalytics` or when your games ends. It is necessary to end the `FlurryAnalytics` session. This is a requirement for Android but optional on iOS. Example:
```cpp
// end session just valid on android, but it's ok to invoke it on iOS
sdkbox::PluginFlurryAnalytics::endSession();
```
