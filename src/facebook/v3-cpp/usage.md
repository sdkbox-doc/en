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
####Login
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

####Permissions
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

####Share
There are two types of sharing functionality.

* __share__ will automatically post to the user's wall
share a link:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::share(info);
```
share a photo:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox::PluginFacebook::share(info);
```
* __dialog__ will show a dialog and prompt the user to write their own comments in addition:

present a share dialog:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox::PluginFacebook::dialog(info);
```

share a photo with comments:
```cpp
sdkbox::FBShareInfo info;
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox::PluginFacebook::dialog(info);
```
 > Note: sharing photo with comments requires the __Facebook app__ to be installed on the device.

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
