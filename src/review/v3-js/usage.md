### Register Javascript Functions
You need to register all the Review JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginReviewJS.hpp"
#include "PluginReviewJSHelper.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginReviewJS);
sc->addRegisterCallback(register_all_PluginReviewJS_helper);
```

### Initialize Review
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginReview.init();
```

### Setting Review (optional)
You can set a custom string for the rate prompt, if you don't want to use the default string.

`Note:` if you set `tryPromptWhenInit` to __true__ which is in `sdkbox.config`, you must call the following functions before `init()`:
```cpp
sdkbox.PluginReview.setCustomPromptTitle("custom title");
sdkbox.PluginReview.setCustomPromptMessage("custom message");
sdkbox.PluginReview.setCustomPromptCancelButtonTitle("custom cancel");
sdkbox.PluginReview.setCustomPromptRateButtonTitle("custom rate");
sdkbox.PluginReview.setCustomPromptRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `tryToShowPrompt` try to display rate prompt:
```cpp
sdkbox.PluginReview.tryToShowPrompt();
```

Use `forceToShowPrompt` to display rate prompt without checks:
```cpp
sdkbox.PluginReview.forceToShowPrompt();
```

If you set `UserEventLimit` not 0 in `sdkbox.config`, you must call `userDidSignificantEvent` increase user event count: `userDidSignificantEvent` increase user event count
```cpp
sdkbox.PluginReview.userDidSignificantEvent(true);
```


### Catch Review events (optional)
This allows you to catch the `Review` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginReview
plugin.setListener({
  didDisplayAlert: function(data) {cc.log("didDisplayAlert")},
  didDeclineToRate: function(data) { cc.log("didDeclineToRate") },
  didToRate: function(data) { cc.log("didToRate") },
  didToRemindLater: function(data) { cc.log("didToRemindLater") }
})
plugin.init()
```
