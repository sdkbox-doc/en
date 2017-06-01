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

<pre>
This method calls login with a single permission: sdkbox::FB_PERM_READ_PUBLIC_PROFILE
</pre>

```javascript
sdkbox.PluginFacebook.login(permissions);
```

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

<pre>
This data only reflects your friends that are using the app.
The number of friends defaults to 25.
</pre>

```javascript
sdkbox.PluginFacebook.canPresentWithFBApp(info);
```
> check whether can present Facebook App

```javascript
sdkbox.PluginFacebook.inviteFriends(app_link_url, preview_image_url);
```
> Use the default FB dialog to invite friends.

```javascript
sdkbox.PluginFacebook.setAppId(appId);
```
> Set the Facebook App ID to be used by the FB SDK.

```javascript
sdkbox.PluginFacebook.setAppURLSchemeSuffix(appURLSchemeSuffix);
```
> Set the app url scheme suffix used by the FB SDK.

```javascript
sdkbox.PluginFacebook.requestGift(invite_ids,
                                   object_id,
                                   message,
                                   title,
                                   additional_data);
```
> Ask friends for a gift

```javascript
sdkbox.PluginFacebook.sendGift(friend_ids,
                                object_id,
                                title,
                                message,
                                additional_data);
```
> Send friend a gift


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

```javascript
onRequestInvitableFriends(friends);
```

```javascript
onInviteFriendsWithInviteIdsResult(result, msg);
```

```javascript
onInviteFriendsResult(result, msg);
```

```javascript
onGetUserInfo(userInfo);
```

```javascript
onAskGiftResult(result, msg);
```

```javascript
onSendGiftResult(result, msg);
```


