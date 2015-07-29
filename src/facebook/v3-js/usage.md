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

* Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginFacebook.init();
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFacebookJS.hpp"
#include "PluginFacebookJSHelper.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginFacebookJS);
sc->addRegisterCallback(register_all_PluginFacebookJS_helper);
```
This registers the Javascript callbacks.

### Using Facebook
There are many Facebook operations that you can take advantage of. Before using any of them it is necessary to call `login()`, example:
  ```javascript
  sdkbox.PluginFacebook.login();
  ```

* You can share links, example:
  ```javascript
  FBShareInfo info;
  info.type  = FB_LINK;
  info.link  = "http://www.cocos2d-x.org";
  info.title = "cocos2d-x";
  info.text  = "Best Game Engine";
  info.image = "http://cocos2d-x.org/images/logo.png";
  sdkbox.PluginFacebook.share(info);
  ```
* You can share a link, but also comment on it at the same time, example:
  ```javascript
  FBShareInfo info;
  info.type  = FB_LINK;
  info.link  = "http://www.cocos2d-x.org";
  info.title = "cocos2d-x";
  info.text  = "Best Game Engine";
  info.image = "http://cocos2d-x.org/images/logo.png";
  sdkbox.PluginFacebook.dialog(info);
  ```

* You can share a photo example:
  ```javascript
  FBShareInfo info;
  info.type  = FB_PHOTO;
  info.title = "My Photo";
  info.image = __path to image__;
  sdkbox.PluginFacebook.share(info);
  ```

* You can share a photo, but also comment on it at the same time, example:
  ```javascript
  FBShareInfo info;
  info.type  = FB_PHOTO;
  info.title = "My Photo";
  info.image = __path to image__;
  sdkbox.PluginFacebook.dialog(info);
  ```

* Besides logging in, you also will need to request `read()` and `publish()` permissions to post. Example:
  ```javascript
  sdkbox.PluginFacebook.requestReadPermissions({FB_PERM_READ_USER_FRIENDS});
  sdkbox.PluginFacebook.requestPublishPermissions({FB_PERM_PUBLISH_POST});
  ```

* When are are finished, it is appropriate to call `logout()`, example:
  ```javascript
  sdkbox.PluginFacebook.logout();
  ```

### Catch Facebook events (optional)
This allows you to catch `Facebook` events so that you can perform operations after Facebook events have occurred.

* Allow your class to extend `sdkbox::FacebookListener` and override the functions listed:
```javascript
sdkbox.PluginFacebook.setListener({
		onLogin : function (isLogin, error) {
				// Called when logged in
		},
		onAPI : function (tag, jsonData) {
				// Called when API request completes
		},
		onSharedSuccess : function (message) {
				// Called when you successfully share
		},
		onSharedFailed : function (message) {
				// Called when sharing has failed
		},
		onSharedCancel : function (message) {
				// Called when sharing is canceled
		}
});
```
