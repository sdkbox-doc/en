### Register Javascript Functions
You need to register all the SdkboxAds JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginSdkboxAdsJS.hpp"
#include "PluginSdkboxAdsJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginSdkboxAdsJS);
sc->addRegisterCallback(register_all_PluginSdkboxAdsJS_helper);
```

### Initialize SdkboxAds
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginSdkboxAds.init();
```

### Using SdkboxAds

To request a default Ad for the default AdUnit and have a fast integration test:
```javascript
sdkbox.PluginSdkboxAds.play()
```

To request Ads in the Default AdUnit:
```javascript
sdkbox.PluginSdkboxAds.play( zone_place_location, params );

// params is an object with string keys and values.
```
> Note: the params are defined per AdUnit, and should be checked in each AdUnit's documentation.

To request Ads for an specific AdUnit:
```javascript
sdkbox.PluginSdkboxAds.play( ad_unit_name, zone_place_location, params );
```

To request ads for a placement defined in the sdkbox_config.json file:
```javascript
sdkbox.PluginSdkboxAds.placement( placement_name );
```

To have fine grained cache control (for AdUnits that expose it):
```javascript
sdkbox.PluginSdkboxAds.cacheControl( ad_unit, cacheOpts );

// cacheOpts is an object with keys and values as strings. 
```
> Cache options are AdUnit specific and must be checked in each AdUnit's documentation.

### SdkboxAds events
This allows you to catch `SdkboxAds` events.

```javascript
sdkbox.PluginSdkboxAds.setListener({
    onAdAction : function( ad_unit_id, zone_location_place_you_name_it, action_type),
    onRewardAction : function( ad_unit_id, zone_id, reward_amount, reward_succeed )
});
```

> refer to the cpp documentation for action_type values.
