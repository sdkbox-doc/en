## API Reference

### Methods
```javascript
sdkbox.IAP.init();
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


### Listeners
```javascript
onInitialized(ok);
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


