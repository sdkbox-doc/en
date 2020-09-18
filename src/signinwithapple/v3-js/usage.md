### Register Javascript Functions
You need to register all the SignInWithApple JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```javascript
#include "PluginSignInWithAppleJS.hpp"
#include "PluginSignInWithAppleJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```javascript
sc->addRegisterCallback(register_all_PluginSignInWithAppleJS);
sc->addRegisterCallback(register_all_PluginSignInWithAppleJS_helper);
```

### Initialize SignInWithApple
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginSignInWithApple.init();
```

### Login

Sign in with Apple

```javascript
sdkbox.PluginSignInWithApple.sign();
```

if user have login before, you can invoke following when app init:

```javascript
sdkbox.PluginSignInWithApple.signWithExistingAccount();
```


### Handling SignInWithApple Events
This allows you to catch the `SignInWithApple` events so that you can perform operations based upon the response from your players and SignInWithApple servers.


```Javascript
sdkbox.PluginSignInWithApple.setListener({
    onAuthorizationDidComplete: function(authInfo) {},
    onAuthorizationCompleteWithError: function(authInfo) {},
    onAuthorizationStatus: function(authState) {},
});
```
