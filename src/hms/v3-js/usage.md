### Register Javascript Functions
You need to register all the HMS JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginHMSJS.hpp"
#include "PluginHMSJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginHMSJS);
sc->addRegisterCallback(register_all_PluginHMSJS_helper);
```

### Initialize HMS
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.HMS.init();
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```javascript
sdkbox.HMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.HMS.login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```javascript
sdkbox.HMS.login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```javascript
sdkbox.HMS.logout();
```

### Handling Purchase Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.
```Javascript
sdkbox.HMS.setListener({
    onLogin : function (code, msg) {
        // login event
    }
});
```
