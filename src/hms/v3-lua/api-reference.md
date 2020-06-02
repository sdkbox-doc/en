## API Reference

### Methods
```lua
sdkbox.PluginHMS:setGDPR(enabled)
```
> Set GDPR

```lua
sdkbox.PluginHMS:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginHMS:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginHMS:login(loginType)
```
> HMS provider three way to login
loginType: 0, slient login 1, login with HuaweiID(ID Token) 2, login with HuaweID(Authorization Code)

```lua
sdkbox.PluginHMS:logout()
```
> logout HMS

```lua
sdkbox.PluginHMS:iapRequestProducts()
```

```lua
sdkbox.PluginHMS:iapPurchase(name)
```

```lua
sdkbox.PluginHMS:iapPurchaseWithPrice(productJson)
```

```lua
sdkbox.PluginHMS:iapRequestOwnedPurchases()
```

```lua
sdkbox.PluginHMS:iapConsume(purchaseToken)
```

```lua
sdkbox.PluginHMS:iapRequestOwnedPurchaseRecords()
```


### Listeners
```lua
onLogin(code, msg)
```

```lua
onIAPReady(code, msg)
```

```lua
onIAPProducts(code, errorOrJson)
```

```lua
onIAPPurchase(code, errorOrJson)
```

```lua
onIAPPConsume(code, errorOrJson)
```

```lua
onIAPOwnedPurchases(code, errorOrJson)
```

```lua
onIAPOwnedPurchaseRecords(code, errorOrJson)
```


