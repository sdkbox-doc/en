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
sdkbox.IAP.onSuccess(product);
```
> Called when an IAP processed successfully

```javascript
sdkbox.IAP.onFailure(product, message);
```
> Called when an IAP fails

```javascript
sdkbox.IAP.onCanceled(product);
```
> Called when user canceled the IAP

```javascript
sdkbox.IAP.onRestored(product);
```
> Called when server returns the IAP items user already purchased

```javascript
sdkbox.IAP.onProductRequestSuccess(products);
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```javascript
sdkbox.IAP.onProductRequestFailure(message);
```
> Called when the product request fails
