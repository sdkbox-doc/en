### Initialize SignInWithApple
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginSignInWithApple/PluginSignInWithApple.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSignInWithApple::init();
}
```

### Login

Sign in with Apple

```cpp
sdkbox::PluginSignInWithApple::sign();
```

if user have login before, you can invoke following when app init:

```cpp
sdkbox::PluginSignInWithApple::signWithExistingAccount();
```

### Handling SignInWithApple Events
This allows you to catch the `SignInWithApple` events so that you can perform operations based upon the response from your players and SignInWithApple servers.

* Allow your class to extend `sdkbox::SignInWithAppleListener`:
```cpp
#include "PluginSignInWithApple/PluginSignInWithApple.h"
class MyClass : public sdkbox::SignInWithAppleListener {
private:
  void onAuthorizationDidComplete(const std::string& authInfo) override;
  void onAuthorizationCompleteWithError(const std::string& authInfo) override;
  void onAuthorizationStatus(const std::string& authState) override;
}
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginSignInWithApple::setListener(listener);
```
