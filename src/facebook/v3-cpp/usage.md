### Initialize Facebook
* Modify your app's __Info.plist__ to include the following additional keys, ensuring that you replace __<APP ID>__ with yours:
```xml
<key>CFBundleURLTypes</key>
<array>
<dict>
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

* Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginFacebook/PluginFacebook.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginFacebook::init();
}
```

### Using Facebook
There are many Facebook operations that you can take advantage of. Before using any of them it is necessary to call `login()`, example:
  ```cpp
  sdkbox::PluginFacebook::login();
  ```

* You can share links, example:
  ```cpp
  FBShareInfo info;
  info.type  = FB_LINK;
  info.link  = "http://www.cocos2d-x.org";
  info.title = "cocos2d-x";
  info.text  = "Best Game Engine";
  info.image = "http://cocos2d-x.org/images/logo.png";
  PluginFacebook::share(info);
  ```
  
* You can share a link, but also comment on it at the same time, example:
  ```cpp
  FBShareInfo info;
  info.type  = FB_LINK;
  info.link  = "http://www.cocos2d-x.org";
  info.title = "cocos2d-x";
  info.text  = "Best Game Engine";
  info.image = "http://cocos2d-x.org/images/logo.png";
  PluginFacebook::dialog(info);
  ```

* You can share a photo example:
  ```cpp
  FBShareInfo info;
  info.type  = FB_PHOTO;
  info.title = "My Photo";
  info.image = __path to image__;
  PluginFacebook::share(info);
  ```

* You can share a photo, but also comment on it at the same time, example:
  ```cpp
  FBShareInfo info;
  info.type  = FB_PHOTO;
  info.title = "My Photo";
  info.image = __path to image__;
  PluginFacebook::dialog(info);
  ```

* Besides logging in, you also will need to request `read()` and `publish()` permissions to post. Example:
  ```cpp
  PluginFacebook::requestReadPermissions({FB_PERM_READ_USER_FRIENDS});
  PluginFacebook::requestPublishPermissions({FB_PERM_PUBLISH_POST});
  ```

* When are are finished, it is appropriate to call `logout()`, example:
  ```cpp
  sdkbox::PluginFacebook::logout();
  ```

### Catch Facebook events (optional)
This allows you to catch `Facebook` events so that you can perform operations after Facebook events have occurred.

* Allow your class to extend `sdkbox::FacebookListener` and override the functions listed:
```cpp
#include "PluginFacebook/PluginFacebook.h"
class MyClass : public sdkbox::FacebookListener
{
private:
  void onLogin(bool isLogin, const std::string& error);
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
