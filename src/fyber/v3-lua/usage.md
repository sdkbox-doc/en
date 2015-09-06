### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Fyber` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginFyberLua.hpp"
#include "PluginFyberLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginFyberLua(L);
  register_all_PluginFyberLua_helper(L);
}
```

### Initialize Fyber
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFyber:init();
```

### Using Fyber
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

### Fyber events
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
