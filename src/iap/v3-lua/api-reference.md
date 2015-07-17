## API Reference

### Methods
```lua
sdkbox.IAP:init()
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

### Listeners
```lua
sdkbox.IAP:onSuccess(product)
```
> Called when an IAP processed successfully

```lua
sdkbox.IAP:onFailure(product, message)
```
> Called when an IAP fails

```lua
sdkbox.IAP:onCanceled(product)
```
> Called when user canceled the IAP

```lua
sdkbox.IAP:onRestored(product)
```
> Called when server returns the IAP items user already purchased

```lua
sdkbox.IAP:onProductRequestSuccess(products)
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```lua
sdkbox.IAP:onProductRequestFailure(message)
```
> Called when the product request fails
