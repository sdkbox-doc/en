## API Reference

### Methods
```javascript
sdkbox.IAP.init(jsonconfig);
```
> Initialize SDKBox IAP

```javascript
sdkbox.IAP.setDebug(debug);
```
> Enable/disable debug logging

```javascript
sdkbox.IAP.purchase(name);
```
> Make a purchase request

<pre>
@Param name is the name of the item specified in sdkbox_config.json
</pre>

```javascript
sdkbox.IAP.refresh();
```
> Refresh the IAP data(title, price, description)

```javascript
sdkbox.IAP.restore();
```
> Restore purchase

```javascript
sdkbox.IAP.setListener(listener);
```
> Set listener for IAP

```javascript
sdkbox.IAP.removeListener();
```
> Remove listener for IAP

```javascript
sdkbox.IAP.enableUserSideVerification();
```

```javascript
sdkbox.IAP.isAutoFinishTransaction();
```
> get auto invoke finishTransaction flag

```javascript
sdkbox.IAP.setAutoFinishTransaction(b);
```
> set auto invoke finishTransaction flag

```javascript
sdkbox.IAP.finishTransaction(productid);
```
> to invoke ios finishTransaction api

```javascript
sdkbox.IAP.fetchStorePromotionOrder();
```

```javascript
sdkbox.IAP.updateStorePromotionOrder(productNames);
```

```javascript
sdkbox.IAP.fetchStorePromotionVisibility(productName);
```

```javascript
sdkbox.IAP.updateStorePromotionVisibility(productName, visibility);
```

```javascript
sdkbox.IAP.getPurchaseHistory();
```
> get all purchase history, include cancelled, expired

```javascript
sdkbox.IAP.getInitializedErrMsg();
```
> get initialized error message

```javascript
sdkbox.IAP.requestUpdateTransaction();
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


### Listeners
```javascript
onInitialized(success);
```
> Called when IAP initialized

```javascript
onSuccess(p);
```
> Called when an IAP processed successfully

```javascript
onFailure(p, msg);
```
> Called when an IAP fails

```javascript
onCanceled(p);
```
> Called when user canceled the IAP

```javascript
onRestored(p);
```
> Called when server returns the IAP items user already purchased
@note this callback will be called multiple times if there are multiple IAP

```javascript
onProductRequestSuccess(products);
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```javascript
onProductRequestFailure(msg);
```
> Called when the product request fails

```javascript
onRestoreComplete(ok, msg);
```
> Called when the restore completed

```javascript
onShouldAddStorePayment(productName);
```

```javascript
onFetchStorePromotionOrder(productNames, error);
```

```javascript
onFetchStorePromotionVisibility(productName, visibility, error);
```

```javascript
onUpdateStorePromotionOrder(error);
```

```javascript
onUpdateStorePromotionVisibility(error);
```

```javascript
onPurchaseHistory(purchases);
```

```javascript
onConsumed(product, error);
```

```javascript
onDeferred(product);
```
> Called when IAP pay deferred
>
> Note: Pay deferred status is a middle status, for most developer, needn't case this status
> this status will change to success or failed or cancel, its final status is pending external action.
>
> Please DO NOT finishTransaction when status is deferred.

