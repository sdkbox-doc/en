### Register Javascript Functions
You need to register all the Facebook JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFacebookJS.hpp"
#include "PluginFacebookJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginFacebookJS);
sc->addRegisterCallback(register_all_PluginFacebookJS_helper);
```

### Initialize Facebook
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginFacebook.init();
```

### Using Facebook
#### Login
First the user needs to login to Facebook in order to use it.
```javascript
sdkbox.PluginFacebook.login();
```
If a user doesn't want to use Facebook functionality anymore, logout. using
```javascript
sdkbox.PluginFacebook.logout();
```
You can check whether user already logged in using
```javascript
sdkbox.PluginFacebook.isLoggedIn();
```
> Note: user only needs to perform login once, unless they logout

#### Permissions
Facebook requires you to ask for the user's permission before you can perform actions, such as, posting on the user's behalf.
There are two types of permission __read__ and __publish__
You can get a complete list of permissions [here](https://developers.facebook.com/docs/facebook-login/permissions/v2.3#reference)

To request a permission, you do so by specifying what you want:
```javascript
sdkbox.PluginFacebook.requestReadPermissions(["public_profile", "email"]);
sdkbox.PluginFacebook.requestPublishPermissions(["publish_actions"]);
```

#### Share
There are two types of sharing functionality.

* __share__ will automatically post to the user's wall
share a link:
```javascript
var info = new Object();
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.share(info);
```
share a photo:
```javascript
var info = new Object();
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.share(info);
```
* __dialog__ will show a dialog and prompt the user to write their own comments in addition:

present a share dialog:
```javascript
var info = new Object();
info.type  = "link";
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook.dialog(info);
```

share a photo with comments:
```javascript
var info = new Object();
info.type  = "photo";
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook.dialog(info);
```
 > Note: sharing photo with comments requires the __Facebook app__ to be installed on the device.

 #### Invite
 There are both __standard__ and __custom__ *Invite* dialogs available to use when inviting your Friends.

 When using the *standard invite dialog*, it is necessary to select the friends to send the invitation request too. The API call is `inviteFriends()` passing in a URL for __app__ and a __preview image__. Example:
 ```js
 sdkbox.PluginFacebook.inviteFriends(
   "https://play.google.com/store/apps/details?id=com.cocos2dx.PluginTest",
   "http://www.cocos2d-x.org/attachments/801/cocos2dx_portrait.png");
 ```

 The __app__ URL must be to a valid GooglePlay/iTunes application URL. At runtime, a custom message can be attached to the invite request. It is not possible to set a predefined invite message.

 Creating a *custom invite dialog* is a two step process, starting with a call to `requestInvitableFriends()` then a call to `inviteFriendsWithInviteIds()` to actually send the invites. Example:
 ```js
 sdkbox.PluginFacebook.inviteFriendsWithInviteIds([], “title", “invitation text");
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
You can perform [Graph API](https://developers.facebook.com/docs/graph-api/overview/) using the `api` function

For example, to get the friend list:
```javascript
var params = new Object();
sdkbox.PluginFacebook.api("/me/friendlists", "GET", params, "/me/friendlists");
```

### Facebook events
This allows you to catch `Facebook` events so that you can perform operations after Facebook events have occurred.

```javascript
sdkbox.PluginFacebook.setListener({
    onLogin: function(isLogin, msg) {},
    onAPI: function(tag, data) {},
    onSharedSuccess: function(data) {},
    onSharedFailed: function(data) {},
    onSharedCancel: function() {},
    onPermission: function(isLogin, msg) {}
});
```
