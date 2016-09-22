### Initialize Facebook
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFacebook:init();
```

### Using Facebook
#### Login
First the user needs to login to Facebook in order to use it.
```lua
sdkbox.PluginFacebook:login();
```
If a user doesn't want to use Facebook functionality anymore, logout. using
```lua
sdkbox.PluginFacebook:logout();
```
You can check whether user already logged in using
```lua
sdkbox.PluginFacebook:isLoggedIn();
```
> Note: user only needs to perform login once, unless they logout

#### Permissions
Facebook requires you to ask for the user's permission before you can perform actions, such as, posting on the user's behalf.
There are two types of permission __read__ and __publish__
You can get a complete list of permissions [here](https://developers.facebook.com/docs/facebook-login/permissions/v2.3#reference)

SDKBOX provides the most commonly used permissions:

* FB_PERM_READ_PUBLIC_PROFILE
* FB_PERM_READ_EMAIL
* FB_PERM_READ_USER_FRIENDS
* FB_PERM_PUBLISH_POST

To request a permission, you do so by specifying what you want:
```lua
sdkbox.PluginFacebook:requestReadPermissions({FB_PERM_READ_PUBLIC_PROFILE, FB_PERM_READ_USER_FRIENDS});
sdkbox.PluginFacebook:requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

#### Share
There are two types of sharing functionality.

* __share__ will automatically post to the user's wall
share a link:
```lua
local info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook:share(info);
```
share a photo:
```lua
local info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook:share(info);
```
* __dialog__ will show a dialog and prompt the user to write their own comments in addition:

present a share dialog:
```lua
local info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook:dialog(info);
```

share a photo with comments:
```lua
local info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook:dialog(info);
```
 > Note: sharing photo with comments requires the __Facebook app__ to be installed on the device.

#### Invite
There are both __standard__ and __custom__ *Invite* dialogs available to use when inviting your Friends.

When using the *standard invite dialog*, it is necessary to select the friends to send the invitation request too. The API call is `inviteFriends()` passing in a URL for __app__ and a __preview image__. Example:
```lua
sdkbox.PluginFacebook:inviteFriends(
 "https://fb.me/322164761287181",
 "http://www.cocos2d-x.org/attachments/801/cocos2dx_portrait.png");
```

  > Note: Contrary to what it may seem the __app link url__, it is not an App Store or Google Play application url. You must follow the instructions on this [page](https://developers.facebook.com/quickstarts/?platform=app-links-host)  and use the resulting url as the __app_link_url__ parameter. Facebook hosts this file for the developer, but anyone could host their own file using this [format](https://developers.facebook.com/docs/app-invites/android#app_links)

Creating a *custom invite dialog* is a two step process, starting with a call to `requestInvitableFriends()` then a call to `inviteFriendsWithInviteIds()` to actually send the invites. Example:
```lua
sdkbox.PluginFacebook:inviteFriendsWithInviteIds({}, “title", “invitation text");
```

The `requestInvitableFriends()` function has a __Bundle(map<string,string>)__ parameter, where the developer can define a few flags:

| Flag  | Description  |
| :---- | :---------------|
| fields | a comma separated values of the fields you want to get from your invitable friend’s profiles. |
| exclude_ids | a comma separated FB ids to exclude from the result. |
| limit | number of friends per page. |

A call to `requestInvitableFriends()` will return a different collection of friends per call, and it is Facebook's decision which ones to return first.
This function returns a `FBInvitableFriendsInfo` object, which will contain a collection of the friends data and a pagination cursor object which has URLS for requesting the next and previous page of invitable friends.

The *custom invite dialog* is only available for games with a __canvas implementation__ for the Facebook application. The __canvas__ must be defined but doesn't need to how any web content. If the __canvas__ is not defined a *standard invite dialog* is used instead.

### Graph API
You can perform [Graph API](https://developers.facebook.com/docs/graph-api/overview/) using `api` function

For example, to get the friend list:
```
local params;
sdkbox.PluginFacebook:api("/me/friendlists", "GET", params, "/me/friendlists");
```

### Facebook events
This allows you to catch `Facebook` events so that you can perform operations after Facebook events have occurred.

```lua
sdkbox.PluginFacebook:setListener(function(args)
    dump(args, "FB listener args:")
    if "onLogin" == args.name then
        local isLogin = args.isLoggedIn;
        local msg = args.data;
    elseif "onPermission" ==  args.name then
        local isLogin = args.ok;
        local msg = args.data;
    elseif "onAPI" ==  args.name then
        local tag = args.tag;
        local jsonData = args.data;
    elseif "onSharedSuccess" ==  args.name then
        local msg = args.data
    elseif "onSharedFailed" ==  args.name then
        local msg = args.data
    elseif "onSharedCancel" ==  args.name then
        local msg = args.data
    elseif "onFetchFriends" == args.name then
        local ok = args.ok
        local msg = args.data
    elseif "onInviteFriendsResult" == args.name then
        local ok = args.ok
        local msg = args.data
    elseif "onInviteFriendsWithInviteIdsResult" == args.name then
        local ok = args.ok
        local msg = args.data
    elseif "onRequestInvitableFriends" == args.name then
        local users = args.users
        local urls = args.urls
    elseif "onGetUserInfo" == args.name then
        local user = args.data
    else
        print("Unknown event:" .. args.name)
    end
end)
```
