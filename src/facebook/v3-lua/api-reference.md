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
sdkbox.PluginFacebook:login(permissions)
```

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
sdkbox.PluginFacebook:fetchFriends()
```
> fetch friends data from Facebook

```lua
sdkbox.PluginFacebook:canPresentWithFBApp(info)
```
> check whether can present Facebook App

```lua
sdkbox.PluginFacebook:inviteFriends(app_link_url, preview_image_url)
```
> Use the default FB dialog to invite friends.

```lua
sdkbox.PluginFacebook:setAppId(appId)
```
> Set the Facebook App ID to be used by the FB SDK.

```lua
sdkbox.PluginFacebook:setAppURLSchemeSuffix(appURLSchemeSuffix)
```
> Set the app url scheme suffix used by the FB SDK.

### Listeners
```lua
onLogin(isLogin, msg)
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
onPermission(isLogin, msg)
```

```lua
onFetchFriends(ok, msg)
```

```lua
onRequestInvitableFriends(friends)
```

```lua
onInviteFriendsWithInviteIdsResult(result, msg)
```

```lua
onInviteFriendsResult(result, msg)
```

```lua
onGetUserInfo(userInfo)
```


