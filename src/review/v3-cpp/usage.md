### Initialize Review
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginReview/PluginReview.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginReview::init();
}
```

### Setting Review (optional)
You can set a custom string for the rate prompt, if you don't want to use the default string.

`Note:` if you set `tryPromptWhenInit` to __true__ which is in `sdkbox.config`, you must call the following functions before `init()`:
```cpp
sdkbox::PluginReview::setTitle("custom title");
sdkbox::PluginReview::setMessage("custom message");
sdkbox::PluginReview::setCancelButtonTitle("custom cancel");
sdkbox::PluginReview::setRateButtonTitle("custom rate");
sdkbox::PluginReview::setRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `show` to display rate prompt:
```cpp
sdkbox::PluginReview::show();
```

If you set `UserEventLimit` to something other than 0 in `sdkbox.config`, you must call `userDidSignificantEvent` to increase user event count. Example:
```cpp
sdkbox::PluginReview::userDidSignificantEvent(true);
```

### Catch Review events (optional)
This allows you to catch the `Review` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::ReviewListener`
```cpp
#include "PluginReview/PluginReview.h"
class MyClass : public sdkbox::ReviewListener
{
private:
    void onDisplayAlert();
    void onDeclineToRate();
    void onRate();
    void onRemindLater();
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginReview::setListener(this);
```
