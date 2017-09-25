### Methods

```
sdkbox.PluginGameroom.init(appID);
```

>   Initialize the Gameroom Plugin. `appID` is your Facebook Application ID. The method will return 0 if the plugin is Initialized successfully.

```
sdkbox.PluginGameroom.login();
```

>   Player login. The method will return a string representing `GameroomReq`.


```
sdkbox.PluginGameroom.loginWithScopes(scopeCount, loginScopes);
```

>   Player login with some permissions. `scopeCount` is the total of the permissions. `loginScopes` is a vector which can include these values: `public_profile`, `email`, `user_friends` and `publish_actions`. The method will return a string representing `GameroomReq`.


```
sdkbox.PluginGameroom.isLoggedIn();
```

>   Check whether the player has logged in.

```
sdkbox.PluginGameroom.feedShare(
    toId,
    link,
    linkName,
    linkCaption,
    linkDescription,
    pictureLink,
    mediaSource
);
```

>   Share to Facebook. The meaning of each parameters is as its name. The method will return a string representing `GameroomReq`.


```
sdkbox.PluginGameroom.purchaseIAP(
    product,
    quantity,
    quantityMin,
    quantityMax,
    requestId,
    pricePointId,
    testCurrency
);
```

>   Purchase a product with a prouduct ID. `quantity` is the number of product, `quantityMin` is the minimum number of quantity of product, `quantityMax` is the maximum of quantity of product. For other parameters, you can refer to [Facebook Gameroom SDK](https://developers.facebook.com/docs/games/gameroom/sdk) and [SDKBOX Gameroom Plugin Sample](https://github.com/sdkbox/sdkbox-sample-gameroom). The method will return a string representing `GameroomReq`.

```
sdkbox.PluginGameroom.purchaseIAPWithProductURL(
    product,
    quantity,
    quantityMin,
    quantityMax,
    requestId,
    pricePointId,
    testCurrency
);
```

>   Purchase a product with a prouduct url link. `quantity` is the number of product, `quantityMin` is the minimum number of quantity of product, `quantityMax` is the maximum of quantity of product. For other parameters, you can refer to [Facebook Gameroom SDK](https://developers.facebook.com/docs/games/gameroom/sdk). The method will return a string representing `GameroomReq`.

```
sdkbox.PluginGameroom.payPremium();
```

>   Purchase a premium version or license. It will return a string representing `GameroomReq`.

```
sdkbox.PluginGameroom.hasLicense();
```

>   Check whether the player has license or premium version. The method will return a string representing `GameroomReq`.

```
sdkbox.PluginGameroom.logAppEvent(eventName, formData);
```

>   Send an event to Facebook Analytics. `FormDataHandle` is a JavaScript object. The method will return a string representing `GameroomReq`.

```
sdkbox.PluginGameroom.logAppEventWithValueToSum(eventName, formData, valueToSum);
```

>   Send an event to Facebook Analytics with an extra value `valueToSum`. `FormDataHandle` is a JavaScript object. The method will return a string representing `GameroomReq`.


```
sdkbox.PluginGameroom.appRequest(
    message,
    actionType,
    objectID,
    to,
    filters,
    excludeIDs,
    maxRecipients,
    data,
    title
);
```

>   Send an app request to some users. if parameter `to` is `nullptr`, this method will let player to choose which users he want to send the request. For other parameters, please refer to [Facebook Game Service Requests](https://developers.facebook.com/docs/games/services/gamerequests) and [SDKBOX Gameroom Plugin Sample](https://github.com/sdkbox/sdkbox-sample-gameroom). The method will return a string representing `GameroomReq`.

### Listener Callbacks

Each parameter in callback is a JavaScript object, which has the properties to indicate the result of coresponding methods.

```
onLoginAccessTokenMsg(AccessTokenHandle);
```
>   Triggered by `login()` or `loginWithScopes()`.

```
onFeedShareMsg(FeedShareHandle);
```

>   Triggered by `feedShare()`.

```
onPurchaseIAPMsg(PurchaseHandle);
```

>   Triggered by `purchaseIAP()`, `purchaseIAPWithProductURL()` or `payPremium()`.

```
onHasLicenseMsg(HasLicenseHandle);
```

>   Triggered by `hasLicense()`.

```
onAppRequestMsg(AppRequestHandle);
```

>   Triggered by `appRequest()`.

```
sdkbox.PluginGameroom.setListener(listenerObject);
```

>   Set a JavaScript listener object.

