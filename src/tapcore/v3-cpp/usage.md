### Initialize Tapcore
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```cpp
#include "PluginTapcore/PluginTapcore.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginTapcore::init();
}
```
