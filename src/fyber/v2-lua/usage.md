### Modify `AppDelegate.cpp`
* Modify `Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFyberLua.hpp"
#include "PluginFyberLuaHelper.h"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginFyberLua(<lua_State*>);`.

  __Note:__ It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`.

	Here is an example of what this might look like for you:
```cpp
#include "PluginFyberLua.hpp"
#include "PluginFyberLuaHelper.h"
bool AppDelegate::applicationDidFinishLaunching()
{
	lua_State *tolua_s = pStack->getLuaState();
	register_all_PluginFyberLua(tolua_s);
	register_all_PluginFyberLua_helper(tolua_s);
	tolua_extensions_ccb_open(tolua_s);
}
```

### Initialize Fyber
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFyber:init()
```

### Using Fyber
#### Offer Wall
Displaying the Offer Wall with default placementId
```lua
sdkbox.PluginFyber:showOfferWall();
```

Displaying the Offer Wall with custom placementId
```lua
sdkbox.PluginFyber:showOfferWall("coins");
```

#### Rewarded Video
- iOS configure follow [rewarded-video-iOS](http://developer.fyber.com/content/ios/rewarded-video/introduction/existing-integration/)
- Android configure follow [rewarded-video-android](http://developer.fyber.com/content/android/rewarded-video/)

Queries the server for BrandEngage offers availability with default placementId.
```lua
sdkbox.PluginFyber:requestOffers();
```

Queries the server for BrandEngage offers availability with custom placementId.
```
sdkbox.PluginFyber:requestOffers("coins");
```

Display an available rewarded video, call `requestOffers` first.
```lua
sdkbox.PluginFyber:showOffers();
```

#### Interstitials
Check if interstitial ads are available
```lua
sdkbox.PluginFyber:requestInterstitial();
```

Shows an interstitial ad. call `requestInterstitial` first.
```lua
sdkbox.PluginFyber:showInterstitial();
```

### Catch Fyber events (optional)
This allows you to catch `Fyber` events so that you can perform operations after Fyber events have occurred.

```lua
sdkbox.PluginFyber:setListener(function(args)
	dump(args)
    if args.name == "onVirtualCurrencyConnectorFailed" then
    elseif args.name == "onVirtualCurrencyConnectorSuccess" then
    elseif args.name == "onCanShowInterstitial" then
    elseif args.name == "onInterstitialDidShow" then
    elseif args.name == "onInterstitialDismiss" then
    elseif args.name == "onInterstitialFailed" then
    elseif args.name == "onBrandEngageClientReceiveOffers" then
    elseif args.name == "onBrandEngageClientChangeStatus" then
    elseif args.name == "onOfferWallFinish" then
    end
end)
```
