### Initialize Fyber
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFyber:init();
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

Request Coin
```lua
sdkbox.PluginFyber:requestDeltaOfCoins();
// sdkbox.PluginFyber:requestDeltaOfCoins("coins");

//
// **Best Practice Check**
//
// Some Offer Wall requests can take a few moments longer to load, so ensure that you've configured
// for a potential 5 second delay.

// Although we recommend you call the VCS when returning from the Offer Wall (after a short delay;
// recommended 5 seconds), you can also call when you're loading the screen that shows currency or
// after the user comes back from the Offer Wall.
```

[Fyber iOS](https://ios.fyber.com/docs/sdk-rewards#VCS%20Hosting), [Fyber Android](https://android.fyber.com/docs/learning-rewarding)

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

Display an available rewarded video, call `requestOffers()` first and then `showOffers()`. Developer can `requestOffers()` anytime, then `showOffers()` without any delay:
```lua
sdkbox.PluginFyber:requestOffers();
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

Fetches the amount of a given currency earned since the last time this method was
invoked for the current user ID / app ID combination.
```lua
sdkbox.PluginFyber:requestDeltaOfCoins();
```
or
```
sdkbox.PluginFyber:requestDeltaOfCoins("currencyId")
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
