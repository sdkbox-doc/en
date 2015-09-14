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
```javascript
sdkbox.PluginReview.setTitle("custom title");
sdkbox.PluginReview.setMessage("custom message");
sdkbox.PluginReview.setCancelButtonTitle("custom cancel");
sdkbox.PluginReview.setRateButtonTitle("custom rate");
sdkbox.PluginReview.setRateLaterButtonTitle("custom rate later");
```

After initialization you can begin to use the Review functionality.
Use `show` try to display rate prompt:
```javascript
sdkbox.PluginReview.show();
```

If you set `UserEventLimit` not 0 in `sdkbox.config`, you must call `userDidSignificantEvent` increase user event count: `userDidSignificantEvent` increase user event count
```javascript
sdkbox.PluginReview.userDidSignificantEvent(true);
```


### Catch Review events (optional)
This allows you to catch the `Review` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginReview
plugin.setListener({
  onDisplayAlert: function(data) {cc.log("didDisplayAlert")},
  onDeclineToRate: function(data) { cc.log("didDeclineToRate") },
  onRate: function(data) { cc.log("didToRate") },
  onRemindLater: function(data) { cc.log("didToRemindLater") }
})
plugin.init()
```
