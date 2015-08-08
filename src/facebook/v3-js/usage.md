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
sc->addRegisterCallback(register_PluginFacebookJS_helper);
```

### Initialize Facebook
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginFacebook.init();
```

### Using Facebook
####Login
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

####Permissions
Facebook requires you to ask for the user's permission before you can perform actions, such as, posting on the user's behalf.
There are two types of permission __read__ and __publish__
You can get a complete list of permissions [here](https://developers.facebook.com/docs/facebook-login/permissions/v2.3#reference)

To request a permission, you do so by specifying what you want:
```javascript
sdkbox.PluginFacebook.requestReadPermissions(["public_profile", "email"]);
sdkbox.PluginFacebook.requestPublishPermissions(["publish_actions"]);
```

####Share
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
