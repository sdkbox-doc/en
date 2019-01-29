## API Reference

### Methods
```lua
sdkbox.IAP:init(jsonconfig)
```
> Initialize SDKBox IAP

```lua
sdkbox.IAP:setDebug(debug)
```
> Enable/disable debug logging

```lua
sdkbox.IAP:purchase(name)
```
> Make a purchase request

<pre>
@Param name is the name of the item specified in sdkbox_config.json
</pre>

```lua
sdkbox.IAP:refresh()
```
> Refresh the IAP data(title, price, description)

```lua
sdkbox.IAP:restore()
```
> Restore purchase

```lua
sdkbox.IAP:setListener(listener)
```
> Set listener for IAP

```lua
sdkbox.IAP:removeListener()
```
> Remove listener for IAP

```lua
sdkbox.IAP:enableUserSideVerification()
```

```lua
sdkbox.IAP:isAutoFinishTransaction()
```
> get auto invoke finishTransaction flag

```lua
sdkbox.IAP:setAutoFinishTransaction(b)
```
> set auto invoke finishTransaction flag

```lua
sdkbox.IAP:finishTransaction(productid)
```
> to invoke ios finishTransaction api

```lua
sdkbox.IAP:fetchStorePromotionOrder()
```

```lua
sdkbox.IAP:updateStorePromotionOrder(productNames)
```

```lua
sdkbox.IAP:fetchStorePromotionVisibility(productName)
```

```lua
sdkbox.IAP:updateStorePromotionVisibility(productName, visibility)
```

```lua
sdkbox.IAP:getPurchaseHistory();
```
> get all purchase history, include cancelled, expired

```lua
sdkbox.IAP:getInitializedErrMsg();
```
> get initialized error message

```lua
sdkbox.IAP:requestUpdateTransaction();
```
> request all unfinish transaction, and retrigger onSuccess, onFailed or onCancel event with corresponding transaction.
>
> just valid on iOS
>
> e.g. if there have two transaction (one is success, on is canceled) havn't been finish,
>      after invoke requestUpdateTransaction, onSuccess will trigger with the success transaction, onCancelled will trigger with the cancelled transaction.
>
> Note: for most developer, this api is needn't, onSuccess, onFailed or onCancel will auto trigger when transaction updated.
>
>

### Listeners
```lua
onInitialized(success)
```
> Called when IAP initialized

```lua
onSuccess(p)
```
> Called when an IAP processed successfully

```lua
onFailure(p, msg)
```
> Called when an IAP fails

```lua
onCanceled(p)
```
> Called when user canceled the IAP

```lua
onRestored(p)
```
> Called when server returns the IAP items user already purchased
@note this callback will be called multiple times if there are multiple IAP

```lua
onProductRequestSuccess(products)
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```lua
onProductRequestFailure(msg)
```
> Called when the product request fails

```lua
onRestoreComplete(ok, msg)
```
> Called when the restore completed

```lua
onShouldAddStorePayment(productName)
```

```lua
onFetchStorePromotionOrder(productNames, error)
```

```lua
onFetchStorePromotionVisibility(productName, visibility, error)
```

```lua
onUpdateStorePromotionOrder(error)
```

```lua
onUpdateStorePromotionVisibility(error)
```

```lua
onPurchaseHistory(purchases)
```

```lua
onConsumed(product, error)
```

```lua
onDeferred(product)
```
> Called when IAP pay deferred
>
> Note: Pay deferred status is a middle status, for most developer, needn't case this status
> this status will change to success or failed or cancel, its final status is pending external action.
>
> Please DO NOT finishTransaction when status is deferred.

