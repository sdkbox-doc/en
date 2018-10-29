### Initialize Misc
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```diff
+ #include "PluginMisc/PluginMisc.h"
  AppDelegate::applicationDidFinishLaunching() {
+      sdkbox::PluginMisc::init();
  }
```

### send local notify

you will receive local notify in listener

```cpp
int nid = sdkbox::PluginMisc::localNotify("test title", "this a test notify content", 1000 * 10);
std::stringstream buf;
buf << "Local Notification:" << nid;
CCLOG(buf.str());
```

### Implement MiscListner
* You can implement MiscListener if you want to receive callbacks like video finish playing.
```cpp
#include "PluginMisc/PluginMisc.h"
class MyClass : public sdkbox::MiscListener
{
private:
    virtual void onHandleLocalNotify(const std::string& payloadJson) {
        // recevie local notification
        std::stringstream buf;
        buf << "onHandleLocalNotify:" << payloadJson;
        cocos2d::log("Log: %s", buf.str().c_str());
    };
}
```
