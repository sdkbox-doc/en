### Initialize Firebase
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginFirebase/PluginFirebase.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::Firebase::Analytics::init();
}
```

### Set property
After initialization you can begin to use the Firebase functionality:

```cpp
    sdkbox::Firebase::Analytics::setUserID("sdkbox_inter_test");
    sdkbox::Firebase::Analytics::setUserProperty("favorite_food", "hot pot");
    sdkbox::Firebase::Analytics::setScreenName("login", "");
```

### Log event
You can log game event

```cpp
    std::map<std::string, std::string> params;
    params[sdkbox::Firebase::Analytics::kFIRParameterItemID] = "id123456";
    params[sdkbox::Firebase::Analytics::kFIRParameterItemName] = "name123456";
    params[sdkbox::Firebase::Analytics::kFIRParameterItemCategory] = "category123456";
    params[sdkbox::Firebase::Analytics::kFIRParameterPrice] = "123.4";

    sdkbox::Firebase::Analytics::logEvent(sdkbox::Firebase::Analytics::kFIREventViewItem, params);
```
