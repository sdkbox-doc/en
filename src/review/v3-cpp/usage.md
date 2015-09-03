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
you can set custom string of rate prompt, if you wan't to use default string

`Note:` if you set `tryPromptWhenInit` ture which in `sdkbox.config`, you must call the fllow function before `init()`
```cpp
sdkbox::PluginReview::setCustomPromptTitle("custom title");
sdkbox::PluginReview::setCustomPromptMessage("custom message");
sdkbox::PluginReview::setCustomPromptCancelButtonTitle("custom cancel");
sdkbox::PluginReview::setCustomPromptRateButtonTitle("custom rate");
sdkbox::PluginReview::setCustomPromptRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `tryToShowPrompt` try to display rate prompt:
```cpp
sdkbox::PluginReview::tryToShowPrompt();
```

Use `forceToShowPrompt` to display rate prompt without checks:
```cpp
sdkbox::PluginReview::forceToShowPrompt();
```

if you set `UserEventLimit` not 0 in `sdkbox.config`, you must call `userDidSignificantEvent` increase user event count
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
    void didDisplayAlert();
    void didDeclineToRate();
    void didToRate();
    void didToRemindLater();
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginReview::setListener(this);
```
