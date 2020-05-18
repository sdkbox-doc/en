## API Reference

### Methods
```javascript
sdkbox.PluginHMS.setGDPR(enabled);
```
> Set GDPR

```javascript
sdkbox.PluginHMS.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginHMS.setListener(listener);
```
> Set listener to listen for adcolony events

```javascript
sdkbox.PluginHMS.login(loginType);
```
> HMS provider three way to login
loginType: 0, slient login 1, login with HuaweiID(ID Token) 2, login with HuaweID(Authorization Code)

```javascript
sdkbox.PluginHMS.logout();
```
> logout HMS


### Listeners
```javascript
onLogin(code, msg);
```


