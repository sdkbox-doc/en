### Initialize PhunwareAds
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginPhunwareMessaging/PluginPhunwareMessaging.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginPhunwareMessaging::init();
}
```

### Read message
```cpp
sdkbox::PluginPhunwareMessaging::read("123");
```

### Remove message
```cpp
sdkbox.PluginPhunwareMessaging::remove("123")
```

### Get all messages
```cpp
sdkbox.PluginPhunwareMessaging::messages()
```

### Catch PhunwareAds events (optional)
This allows you to catch the `PhunwareAds` events so that you can perform operations such as providing player rewards for watching the video.

* Allow your class to extend `sdkbox::PhunwareAdsListener`
```cpp
#include "PluginPhunwareMessaging/PluginPhunwareMessaging.h"
class MyClass : public sdkbox::PhunwareAdsListener
{
public:
    void init(bool success, const std::string& message) {}
    void error(const std::string& message) {}
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginPhunwareMessaging::setListener(this);
```
