## API Reference

### Methods
```lua
sdkbox.PluginFacebook:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginFacebook:login()
```
> log in

```lua
sdkbox.PluginFacebook:requestReadPermissions(permissions)
```
> log in with specific read permissions, conflict with publish permissions
https://developers.facebook.com/docs/facebook-login/permissions

```lua
sdkbox.PluginFacebook:requestPublishPermissions(permissions)
```
> log in with specific public permissions
https://developers.facebook.com/docs/facebook-login/permissions

```lua
sdkbox.PluginFacebook:logout()
```
> log out

```lua
sdkbox.PluginFacebook:isLoggedIn()
```
> Check whether the user logined or not

```lua
sdkbox.PluginFacebook:getUserID()
```
> get UserID

```lua
sdkbox.PluginFacebook:getAccessToken()
```
> get AccessToken

```lua
sdkbox.PluginFacebook:getPermissionList()
```
> get permissoin list

```lua
sdkbox.PluginFacebook:share(info)
```
> share

```lua
sdkbox.PluginFacebook:dialog(info)
```
> open a dialog of Facebook app or WebDialog (dialog with photo only avaible with native Facebook app)

```lua
sdkbox.PluginFacebook:getSDKVersion()
```
> return the version of Facebook SDK

```lua
sdkbox.PluginFacebook:api(path, method, params, tag)
```
> use Facebook Open Graph api
https://developers.facebook.com/docs/ios/graph


### Listeners
```lua
onLogin(isLogin, error)
```

```lua
onSharedSuccess(message)
```

```lua
onSharedFailed(message)
```

```lua
onSharedCancel()
```

```lua
onAPI(key, jsonData)
```

```lua
onPermission(isLogin, error)
```


