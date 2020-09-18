## API Reference

### Methods
```lua
sdkbox.PluginSignInWithApple:setGDPR(enabled)
```
> Set GDPR

```lua
sdkbox.PluginSignInWithApple:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginSignInWithApple:setListener(listener)
```
> Set listener to listen for SignInWithApple events

```lua
sdkbox.PluginSignInWithApple:isAvailable()
```

```lua
sdkbox.PluginSignInWithApple:sign()
```

```lua
sdkbox.PluginSignInWithApple:signWithExistingAccount()
```


### Listeners
```lua
onAuthorizationDidComplete(authInfo)
```

```lua
onAuthorizationCompleteWithError(authInfo)
```

```lua
onAuthorizationStatus(authState)
```


