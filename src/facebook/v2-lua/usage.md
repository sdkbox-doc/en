### Initialize Facebook
* Modify your app's __Info.plist__ to include the following additional keys, ensuring that you replace __<APP ID>__ with yours:
```xml
<key>CFBundleURLTypes</key>
<array>
<dict
    <key>CFBundleURLName</key>
    <string></string>
    <key>CFBundleURLSchemes</key>
    <array>
        <string>fb<APP ID></string>
    </array>
</dict>
</array>
<key>FacebookAppID</key>
<string><APP ID></string>
<key>FacebookDisplayName</key>
<string>MyTestApp</string>
```

If my Facebook __APP ID__ is `655158077954837` a completed example would be:
```xml
<key>CFBundleURLTypes</key>
<array>
<dict>
    <key>CFBundleURLName</key>
    <string></string>
    <key>CFBundleURLSchemes</key>
    <array>
        <string>fb655158077954837</string>
    </array>
</dict>
</array>
<key>FacebookAppID</key>
<string>655158077954837</string>
<key>FacebookDisplayName</key>
<string>MyTestApp</string>
```

* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFacebook:init()
```

### Using Facebook
There are many Facebook operations that you can take advantage of. Before using any of them it is necessary to call `login()`, example:
```lua
sdkbox.PluginFacebook:login();
```

* You can share links, example:
```lua
FBShareInfo info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.share(info);
```

* You can share a link, but also comment on it at the same time. This requires the __Facebook app__ to be installed on the device. Example:
```lua
FBShareInfo info;
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.dialog(info);
```

* You can share a photo example:
```lua
FBShareInfo info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.share(info);
```

* You can share a photo, but also comment on it at the same time, example:
```lua
FBShareInfo info;
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.dialog(info);
```

* Besides logging in, you also will need to request `read()` and `publish()` permissions to post. Example:
```lua
sdkbox.PluginFacebook.requestReadPermissions({FB_PERM_READ_USER_FRIENDS});
sdkbox.PluginFacebook.requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

* When are are finished, it is appropriate to call `logout()`, example:
```lua
sdkbox.PluginFacebook.logout();
```

#### Invite
There are both __standard__ and __custom__ *Invite* dialogs available to use when inviting your Friends.

When using the *standard invite dialog*, it is necessary to select the friends to send the invitation request too. The API call is `inviteFriends()` passing in a URL for __app__ and a __preview image__. Example:
```lua
sdkbox.PluginFacebook:inviteFriends(
  "https://play.google.com/store/apps/details?id=com.cocos2dx.PluginTest",
  "http://www.cocos2d-x.org/attachments/801/cocos2dx_portrait.png");
```

The __app__ URL must be to a valid GooglePlay/iTunes application URL. At runtime, a custom message can be attached to the invite request. It is not possible to set a predefined invite message.

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

### Catch Facebook events (optional)
This allows you to catch `Facebook` events so that you can perform operations after Facebook events have occurred.

* Allow your class to extend `sdkbox::FacebookListener` and override the functions listed:
```lua
sdkbox.PluginFacebook:setListener(function(event)
    print("PluginFacebook callback")
    dump(event)
end)
```
