### Initialize AdColony
* Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginAdColony.init();
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAdColonyJS.hpp"
#include "PluginAdColonyJSHelper.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginAdColonyJS);
sc->addRegisterCallback(register_all_PluginAdColonyJS_helper);
```
This registers the Javascript callbacks.

### Showing Ads
Display an ad wherever you want from your code, by specifying ad type:
```cpp
sdkbox.PluginAdColony.show("video");
```
or:
```cpp
sdkbox.PluginAdColony.show("v4vc");
```

### Catch AdColony events (optional)
This allows you to catch the `AdColony` events so that you can perform operations such as providing player rewards for watching the video.

* Create a listener (demonstrated by logging events):
```javascript
/**
 * The structure of data
 * data.name : name of the ad (in sdkbox_config.json)
 * data.zoneID : the zoneID of the ad
 * data.shown : indicates wether the ad gets shown or closed by user
 * data.iapEnabled : indicating whether or not the associated ad is an IAP
 * data.iapProductID : product identifier for the associated ad's IAP
 * data.iapQuantity : he number of items the user wishes to purchase
 * data.iapEngagementType : indicating the IAP engagement mechanism
 */

sdkbox.PluginAdColony.setListener({
		onAdColonyChange : function (data, available) {
				// Called when AdColony finish loading
		},
		onAdColonyReward : function (data, currencyName, amount, success) {
				// Called when AdColony v4vc ad finish playing
		},
		onAdColonyStarted : function (data) {
				// Called when ad starts playing
		},
		onAdColonyFinished : function (data) {
				// Called when an ad finish displaying
		}
});
```
