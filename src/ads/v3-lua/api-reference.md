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
onInitialized(ok)
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


