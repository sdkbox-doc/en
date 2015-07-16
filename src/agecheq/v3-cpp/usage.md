### Initialize AgeCheq
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginAgeCheq/PluginAgeCheq.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginAgeCheq::init();
}
```

### Using AgeCheq
After initialization you can begin to use the AgeCheq functionality. Use `check` or `associateDate()` wherever you want from your code:
```cpp
sdkbox::PluginAgeCheq::check("1426");
sdkbox::PluginAgeCheq::associateData("1426", "ikfill");
```

### Catch AgeCheq events (optional)
This allows you to catch the `AgeCheq` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::AgeCheqListener`
```cpp
#include "PluginAgeCheq/PluginAgeCheq.h"
class MyClass : public sdkbox::AgeCheqListener
{
private:
  void checkResponse(const std::string& rtn, const std::string& rtnmsg,
          int apiversion, int checktype, bool appauthorized,
          bool appblocked, int parentverified, bool under13,
          bool under18, bool underdevage, int trials);

  void associateDataResponse(const std::string& rtn,
          const std::string& rtnmsg);
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginAgeCheq::setListener(this);
```
