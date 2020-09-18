## API Reference

### Methods
```javascript
sdkbox.PluginSignInWithApple.setGDPR(enabled);
```
> Set GDPR

```javascript
sdkbox.PluginSignInWithApple.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginSignInWithApple.setListener(listener);
```
> Set listener to listen for SignInWithApple events

```javascript
sdkbox.PluginSignInWithApple.isAvailable();
```

```javascript
sdkbox.PluginSignInWithApple.sign();
```

```javascript
sdkbox.PluginSignInWithApple.signWithExistingAccount();
```


### Listeners
```javascript
onAuthorizationDidComplete(authInfo);
```

```javascript
onAuthorizationCompleteWithError(authInfo);
```

```javascript
onAuthorizationStatus(authState);
```


