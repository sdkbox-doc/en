### Initialize LeadBolt
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginLeadBolt/PluginLeadBolt.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginLeadBolt::init();
}
```

### show ad
After initialization you can begin to use the LeadBolt functionality:
```cpp
sdkbox::PluginLeadBolt::loadModule("adname");
```

### Catch LeadBolt events (optional)
This allows you to catch the `LeadBolt` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::LeadBoltListener`
```cpp
#include "PluginLeadBolt/PluginLeadBolt.h"

class LBListener : public sdkbox::LeadBoltListener {
public:

    virtual void onModuleLoaded(const std::string& placement) {
        CCLOG("onModuleLoaded placement:%s", placement.c_str());
    }
    virtual void onModuleClosed(const std::string& placement) {
        CCLOG("onModuleClosed placement:%s", placement.c_str());
    }
    virtual void onModuleClicked(const std::string& placement) {
        CCLOG("onModuleClicked placement:%s", placement.c_str());
    }
    virtual void onModuleCached(const std::string& placement) {
        CCLOG("onModuleCached placement:%s", placement.c_str());
    }
    virtual void onModuleFailed(const std::string& placement, const std::string& error, bool iscached) {
        CCLOG("onModuleFailed placement:%s, error:%s, cached:%d", placement.c_str(), error.c_str(), iscached);
    }
    virtual void onMediaFinished(bool viewCompleted) {
        CCLOG("onMediaFinished viewCompleted:%d", viewCompleted);
    }

};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginLeadBolt::setListener(this);
```
