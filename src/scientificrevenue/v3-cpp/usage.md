### Please check Scientific Revenue Documentation

https://documentation.scientificrevenue.com/sdkbox-cocos2d-x/

contact ted@scientificrevenue.com for access. 

Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include “PluginScientificRevenue/PluginScientificRevenue.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::ScientificRevenue::getInstance()->init();
}
```

###Set The pricing session parameters
```cpp
sdkbox::ScientificRevenue::getInstance()->sessionOptions(true, "en_US", true);
```

###Start Session
```cpp
sdkbox::ScientificRevenue::getInstance()->startSession(“UserName”);
```
