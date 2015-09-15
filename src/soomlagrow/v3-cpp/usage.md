### Initialize SoomlaGrow
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginSoomlaGrow/PluginSoomlaGrow.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSoomlaGrow::init();
}
```

### Using GROW's Insights module
After initialization you can begin to use the Insights functionality. Use `refreshInsight` or `getUserInsightInfo()` wherever you want from your code:
```cpp
sdkbox::PluginSoomlaGrow::refreshInsight();
std::string jsonStr = sdkbox::PluginSoomlaGrow::getUserInsightInfo();
```

### Catch GROW events (optional)
This allows you to catch the `GROW` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::SoomlaGrowListener`
```cpp
#include "PluginSoomlaGrow/PluginSoomlaGrow.h"
class MyClass : public sdkbox::SoomlaGrowListener
{
private:
    void onHighWayInitialized();
    void onHighWayConnected();
    void onHighWayDisconnected();
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginSoomlaGrow::setListener(this);
```
