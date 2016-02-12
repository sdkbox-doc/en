## API Reference

### Methods
```javascript
sdkbox.PluginFyber.init(userID);
```
> initialize the fyber plugin.

```javascript
sdkbox.PluginFyber.showOfferWall(placementId);
```
> Presents the Fyber Mobile OfferWall as a child view controller of your own view controller.

```javascript
sdkbox.PluginFyber.requestOffers(placementId);
```
> Request the server for rewarded video availability.

```javascript
sdkbox.PluginFyber.showOffers(placementId);
```
> Show an available rewarded video.

```javascript
sdkbox.PluginFyber.requestInterstitial();
```
> Check if interstitial ads are available

```javascript
sdkbox.PluginFyber.showInterstitial();
```
> Shows an interstitial ad. Check first that one is ready to be shown with requestInterstitial.

```javascript
sdkbox.PluginFyber.requestDeltaOfCoins(currencyId);
```
> Fetches the amount of a given currency earned since the last time this method was 
invoked for the current user ID / app ID combination.


### Listeners
```javascript
onVirtualCurrencyConnectorFailed(error, errorCode, errorMsg);
```

```javascript
onVirtualCurrencyConnectorSuccess(deltaOfCoins,
                                   currencyId,
                                   currencyName,
                                   transactionId);
```

```javascript
onCanShowInterstitial(canShowInterstitial);
```

```javascript
onInterstitialDidShow();
```

```javascript
onInterstitialDismiss(reason);
```

```javascript
onInterstitialFailed();
```

```javascript
onBrandEngageClientReceiveOffers(areOffersAvailable);
```

```javascript
onBrandEngageClientChangeStatus(status, msg);
```

```javascript
onOfferWallFinish(status);
```


