### Initialize Facebook
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginFacebook/PluginFacebook.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFacebook::init();
}
```

### Using Facebook
#### Login
First the user needs to login to Facebook in order to use it.
```cpp
sdkbox::PluginFacebook::login();
```
If a user doesn't want to use Facebook functionality anymore, logout.
```cpp
sdkbox::PluginFacebook::logout();
```
You can check whether user already logged in using
```cpp
sdkbox::PluginFacebook::isLoggedIn();
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
```cpp
sdkbox::PluginFacebook::requestReadPermissions({FB_PERM_READ_PUBLIC_PROFILE, FB_PERM_READ_USER_FRIENDS});
sdkbox::PluginFacebook::requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

#### Share
There are two types of sharing functionality.

* __share__ will automatically post to the user's wall
share a link:
```cpp
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::share(info);
```
share a photo:
```cpp
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox::PluginFacebook::share(info);
```
* __dialog__ will show a dialog and prompt the user to write their own comments in addition:

present a share dialog:
```cpp
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::dialog(info);
```

share a photo with comments:
```cpp
sdkbox::FBShareInfo info;
info.type  = sdkbox::FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox::PluginFacebook::dialog(info);
```
  > Note: sharing photo with comments requires the __Facebook app__ to be installed on the device.

#### Invite
There are both __standard__ and __custom__ *Invite* dialogs available to use when inviting your Friends.

When using the *standard invite dialog*, it is necessary to select the friends to send the invitation request too. The API call is `inviteFriends()` passing in an __app link url__ and a __preview image__. Example:
```cpp
sdkbox::PluginFacebook::inviteFriends(
  "https://fb.me/322164761287181",
  "http://www.cocos2d-x.org/attachments/801/cocos2dx_portrait.png");
```

  > Note: Contrary to what it may seem the __app link url__, it is not an App Store or Google Play application url. You must follow the instructions on this [page](https://developers.facebook.com/quickstarts/?platform=app-links-host)  and use the resulting url as the __app_link_url__ parameter. Facebook hosts this file for the developer, but anyone could host their own file using this [format](https://developers.facebook.com/docs/app-invites/android#app_links)

At runtime, a custom message can be attached to the invite request. It is not possible to set a predefined invite message.

Creating a *custom invite dialog* is a two step process, starting with a call to `requestInvitableFriends()` then a call to `inviteFriendsWithInviteIds()` to actually send the invites. Example:
```cpp
std::vector<std::string> vec;
vec.push_back(invitable_token);
sdkbox::PluginFacebook::inviteFriendsWithInviteIds(vec, "Invitation title", "Invitation text up to 60 chars.");
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
```
sdkbox::PluginFacebook::FBAPIParam params;
sdkbox::PluginFacebook::api("/me/friendlists", "GET", params, "/me/friendlists");
```

### Facebook events
This allows you to catch `Facebook` events so that you can perform operations after Facebook events have occurred.

* Allow your class to extend `sdkbox::FacebookListener` and override the functions listed:
```cpp
#include "PluginFacebook/PluginFacebook.h"
class MyClass : public sdkbox::FacebookListener
{
private:
  void onLogin(bool isLogin, const std::string& msg);
  void onPermission(bool isLogin, const std::string& msg);
  void onAPI(const std::string& tag, const std::string& jsonData);
  void onSharedSuccess(const std::string& message);
  void onSharedFailed(const std::string& message);
  void onSharedCancel();
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginFacebook::setListener(this);
```
