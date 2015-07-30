### Modify Lua Code
Modify `./frameworks/runtime-src/Classes/lua_module_register.h` to include the necessary headers and calls to register `Facebook` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginFacebookLua.hpp"
#include "PluginFacebookLuaHelper.h"
```
```cpp
static int lua_module_register(lua_State* L)
{
  register_all_PluginFacebookLua(L);
  register_PluginFacebookLua_helper(L);
}
```

### Initialize Facebook
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginFacebook:init();
```

### Using Facebook
####Login
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
```lua
sdkbox.PluginFacebook:requestReadPermissions({FB_PERM_READ_PUBLIC_PROFILE, FB_PERM_READ_USER_FRIENDS});
sdkbox.PluginFacebook:requestPublishPermissions({FB_PERM_PUBLISH_POST});
```

####Share
There are two types of sharing functionality.

* __share__ will automatically post to the user's wall
share a link:
```lua
local info;
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook:share(info);
```
share a photo:
```lua
local info;
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook:share(info);
```
* __dialog__ will show a dialog and prompt the user to write their own comments in addition:

present a share dialog:
```lua
local info;
info.type  = FB_LINK;
info.link  = "http://www.cocos2d-x.org";
info.title = "cocos2d-x";
info.text  = "Best Game Engine";
info.image = "http://cocos2d-x.org/images/logo.png";
sdkbox.PluginFacebook:dialog(info);
```

share a photo with comments:
```lua
local info;
info.type  = FB_PHOTO;
info.title = "My Photo";
info.image = __path to image__;
sdkbox.PluginFacebook:dialog(info);
```
 > Note: sharing photo with comments requires the __Facebook app__ to be installed on the device.

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
    if "onLogin" == args.name then
        local isLogin = args.isLogin;
        local msg = args.msg;
    elseif "onPermission" ==  args.name then
        local isLogin = args.isLogin;
        local msg = args.msg;
    elseif "onAPI" ==  args.name then
        local tag = args.tag;
        local jsonData = args.jsonData;
    elseif "onSharedSuccess" ==  args.name then
        local msg = args.message
    elseif "onSharedFailed" ==  args.name then
        local msg = args.message
    elseif "onSharedCancel" ==  args.name then
    end
end)
```
