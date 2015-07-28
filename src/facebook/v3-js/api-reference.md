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
sdkbox.PluginFacebook.logInWithReadPermissions(permissions);
```
> log in with specific read permissions, conflict with publish permissions
https://developers.facebook.com/docs/facebook-login/permissions

```javascript
sdkbox.PluginFacebook.logInWithPublishPermissions(permissions);
```
> log in with specific public permissions
https://developers.facebook.com/docs/facebook-login/permissions

```javascript
sdkbox.PluginFacebook.logout();
```
> log out

```javascript
sdkbox.PluginFacebook.isLogined();
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
> open a dialog of Facebook app

```javascript
sdkbox.PluginFacebook.api(path, method, params, tag);
```
> use Facebook Open Graph api
https://developers.facebook.com/docs/ios/graph

```javascript
sdkbox.PluginFacebook.activateApp();
```
> Notifies the events system that the app has launched & logs an activatedApp event.

```javascript
sdkbox.PluginFacebook.getSDKVersion();
```
> @breif return the version of Facebook SDK for Cocos


### Listeners
```javascript
onLogin(isLogin, error);
```

```javascript
onAPI(key, jsonData);
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
