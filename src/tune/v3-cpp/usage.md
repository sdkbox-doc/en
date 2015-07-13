### Initialize Tune
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. `init()` and `measureSession()` are required. Example:
```cpp
#include "PluginTune/PluginTune.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginTune::init();
     sdkbox::PluginTune::measureSession();
}
```

### Using Tune
After initialization you can begin to use the Tune functionality. Tune uses a concept of __events__ (also known as __MAT Native Event Types__). You log __events__ that you care about and you can later view them using the web-based report viewer. Tune provides a structure for these events in their documentation. Example:
```cpp
{
    PluginTune::measureEventName("purchase");
    PluginTune::measureEventId(1122334455);
		TuneEvent event;
    event.eventName = "purchase2";
    event.refId     = "RJ1357";
    event.searchString = "sweet crisp red apples";
    event.attribute1 = "crisp";
    event.attribute2 = "red";
    event.quantity = 3;
    PluginTune::measureEvent(event);
}
```
Notice that at the end of the __event__ `PluginTune::measureEvent(event)` was called. This takes care of logging our event.
