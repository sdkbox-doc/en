### Initialize Share
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginShare/PluginShare.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginShare::init();
}
```

### share content
After initialization you can begin to use the Share functionality:
```cpp
sdkbox::SocialShareInfo info;
info.text = "#sdkbox(www.sdkbox.com) - the cure for sdk fatigue ";
info.title = "sdkbox";
info.image = "http://www.sdkbox.com/assets/images/logo.png";
info.link = "http://www.sdkbox.com";

//sdkbox::SocialPlatform::Platform_Select will show platforms list, let user select which platform want to share
//sdkbox::SocialPlatform::Platform_Twitter will share with twitter directly
//sdkbox::SocialPlatform::Platform_Facebook will share with facebook directly
info.platform = sdkbox::SocialPlatform::Platform_Select;
sdkbox::PluginShare::share(info);
```


### Catch Share events (optional)
This allows you to catch the `Share` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::ShareListener`
```cpp
#include "PluginShare/PluginShare.h"
class SListener : public sdkbox::ShareListener {
public:
    virtual void onShareState(const sdkbox::SocialShareResponse& response) {
        switch (response.state) {
            case sdkbox::SocialShareState::SocialShareStateNone: {
                CCLOG("SharePlugin::onShareState none");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateUnkonw: {
                CCLOG("SharePlugin::onShareState unkonw");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateBegin: {
                CCLOG("SharePlugin::onShareState begin");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateSuccess: {
                CCLOG("SharePlugin::onShareState success");
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateFail: {
                CCLOG("SharePlugin::onShareState fail, error:%s", response.error.c_str());
                break;
            }
            case sdkbox::SocialShareState::SocialShareStateCancelled: {
                CCLOG("SharePlugin::onShareState cancelled");
                break;
            }
            case sdkbox::SocialShareStateSelectShow: {
                CCLOG("SharePlugin::onShareState show pancel %d", response.platform);
                break;
            }
            case sdkbox::SocialShareStateSelectCancelled: {
                CCLOG("SharePlugin::onShareState show pancel cancelled %d", response.platform);
                break;
            }
            case sdkbox::SocialShareStateSelected: {
                CCLOG("SharePlugin::onShareState show pancel selected %d", response.platform);
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
