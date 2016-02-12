## API Reference

### Methods
```lua
sdkbox.PluginFyber:init(userID)
```
> initialize the fyber plugin.

```lua
sdkbox.PluginFyber:showOfferWall(placementId)
```
> Presents the Fyber Mobile OfferWall as a child view controller of your own view controller.

```lua
sdkbox.PluginFyber:requestOffers(placementId)
```
> Request the server for rewarded video availability.

```lua
sdkbox.PluginFyber:showOffers(placementId)
```
> Show an available rewarded video.

```lua
sdkbox.PluginFyber:requestInterstitial()
```
> Check if interstitial ads are available

```lua
sdkbox.PluginFyber:showInterstitial()
```
> Shows an interstitial ad. Check first that one is ready to be shown with requestInterstitial.

```lua
sdkbox.PluginFyber:requestDeltaOfCoins(currencyId)
```
> Fetches the amount of a given currency earned since the last time this method was 
invoked for the current user ID / app ID combination.


### Listeners
```lua
onVirtualCurrencyConnectorFailed(error, errorCode, errorMsg)
```

```lua
onVirtualCurrencyConnectorSuccess(deltaOfCoins,
                                   currencyId,
                                   currencyName,
                                   transactionId)
```

```lua
onCanShowInterstitial(canShowInterstitial)
```

```lua
onInterstitialDidShow()
```

```lua
onInterstitialDismiss(reason)
```

```lua
onInterstitialFailed()
```

```lua
onBrandEngageClientReceiveOffers(areOffersAvailable)
```

```lua
onBrandEngageClientChangeStatus(status, msg)
```

```lua
onOfferWallFinish(status)
```


