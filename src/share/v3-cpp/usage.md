### Initialize Share
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginShare/PluginShare.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginShare::init();
}
```

### share content to twitter
After initialization you can begin to use the Share functionality:
```cpp
sdkbox::PluginShare::ShareInfo info;
info.text = "#sdkbox - the cure for sdk fatigue";
sdkbox::PluginShare::share(info);
```

### Catch Share events (optional)
This allows you to catch the `Share` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::ShareListener`
```cpp
#include "PluginShare/PluginShare.h"
class SListener : public sdkbox::ShareListener {
public:
    virtual void onShareState(const sdkbox::PluginShare::ShareResponse& response) {
        switch (response.state) {
            case sdkbox::PluginShare::ShareState::ShareStateNone: {
                CCLOG("SharePlugin::onShareState none");
                break;
            }
            case sdkbox::PluginShare::ShareState::ShareStateUnkonw: {
                CCLOG("SharePlugin::onShareState unkonw");
                break;
            }
            case sdkbox::PluginShare::ShareState::ShareStateBegin: {
                CCLOG("SharePlugin::onShareState begin");
                break;
            }
            case sdkbox::PluginShare::ShareState::ShareStateSuccess: {
                CCLOG("SharePlugin::onShareState success");
                break;
            }
            case sdkbox::PluginShare::ShareState::ShareStateFail: {
                CCLOG("SharePlugin::onShareState fail, error:%s", response.error.c_str());
                break;
            }
            case sdkbox::PluginShare::ShareState::ShareStateCancelled: {
                CCLOG("SharePlugin::onShareState cancelled");
                break;
            }
            default: {
                CCLOG("SharePlugin::onShareState");
                break;
            }
        }
     }
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginShare::setListener(this);
```
