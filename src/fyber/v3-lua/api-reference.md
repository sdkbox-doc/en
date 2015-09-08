## API Reference

### Methods
```lua
sdkbox.PluginFyber:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginFyber:showOfferWall(placementId)
```
> Presents the SponsorPay Mobile OfferWall as a child view controller of your own view controller.

```lua
sdkbox.PluginFyber:requestOffers(placementId)
```
> Queries the server for BrandEngage offers availability.

```lua
sdkbox.PluginFyber:showOffers()
```
> Starts running an available engagement.

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


