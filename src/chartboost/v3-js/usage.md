### Initialize Chartboost
* Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginChartboost.init();
```

* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginChartboostJS.hpp"
#include "PluginChartboostJSHelper.h"
```

* Modify `AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginChartboostJS);
sc->addRegisterCallback(register_PluginChartboostJs_helper);
```
This registers the Javascript callbacks.

### Showing Ads
Display an ad where ever you want from your code:
```javascript
// To use Chartboost's predefined location
sdkbox.PluginChartboost.show("Default");
// To use customized location
sdkbox.PluginChartboost.show("your_ad_name");
```

### Catch Chartboost events (optional)
This allows you to catch the `Chartboost` events so that you can perform operations such as providing player rewards for viewing ads.

* Create a listener (demonstrated by logging events):
```javascript
sdkbox.PluginChartboost.setListener({
    onChartboostCached : function (name) { cc.log("onChartboostCached " + name) },
    onChartboostShouldDisplay : function (name) { cc.log("onChartboostShouldDisplay " + name) },
    onChartboostDisplay : function (name) { cc.log("onChartboostDisplay " + name) },
    onChartboostDismiss : function (name) { cc.log("onChartboostDismiss " + name) },
    onChartboostClose : function (name) { cc.log("onChartboostClose " + name) },
    onChartboostClick : function (name) { cc.log("onChartboostClick " + name) },
    onChartboostReward : function (name, reward) { cc.log("onChartboostReward " + name + " reward " + reward) },
    onChartboostFailedToLoad : function (name, e) { cc.log("onChartboostFailedToLoad " + name + " load error " + e) },
    onChartboostFailToRecordClick : function (name, e) { cc.log("onChartboostFailToRecordClick " + name + " click error " + e) },
    onChartboostConfirmation : function () { cc.log("onChartboostConfirmation") },
    onChartboostCompleteStore : function () { cc.log("onChartboostCompleteStore") },
})
```
