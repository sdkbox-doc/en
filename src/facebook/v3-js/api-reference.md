## API Reference

### Methods
```javascript
sdkbox.PluginFacebook.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginFacebook.login();
```
> log in

```javascript
sdkbox.PluginFacebook.requestReadPermissions(permissions);
```
> log in with specific read permissions, conflict with publish permissions
https://developers.facebook.com/docs/facebook-login/permissions

```javascript
sdkbox.PluginFacebook.requestPublishPermissions(permissions);
```
> log in with specific public permissions
https://developers.facebook.com/docs/facebook-login/permissions

```javascript
sdkbox.PluginFacebook.logout();
```
> log out

```javascript
sdkbox.PluginFacebook.isLoggedIn();
```
> Check whether the user logined or not

```javascript
sdkbox.PluginFacebook.getUserID();
```
> get UserID

```javascript
sdkbox.PluginFacebook.getAccessToken();
```
> get AccessToken

```javascript
sdkbox.PluginFacebook.getPermissionList();
```
> get permissoin list

```javascript
sdkbox.PluginFacebook.share(info);
```
> share

```javascript
sdkbox.PluginFacebook.dialog(info);
```
> open a dialog of Facebook app or WebDialog (dialog with photo only avaible with native Facebook app)

```javascript
sdkbox.PluginFacebook.getSDKVersion();
```
> return the version of Facebook SDK

```javascript
sdkbox.PluginFacebook.fetchFriends();
```
> fetch friends data from Facebook


### Listeners
```javascript
onLogin(isLogin, msg);
```

```javascript
onSharedSuccess(message);
```

```javascript
onSharedFailed(message);
```

```javascript
onSharedCancel();
```

```javascript
onAPI(key, jsonData);
```

```javascript
onPermission(isLogin, msg);
```

```javascript
onFetchFriends(ok, msg);
```


