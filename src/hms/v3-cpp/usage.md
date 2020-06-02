### Initialize HMS
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginHMS/PluginHMS.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::HMS::init();
}
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```cpp
sdkbox::HMS::login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```cpp
sdkbox::HMS::login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```cpp
sdkbox::HMS::login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```cpp
sdkbox::HMS::logout();
```

### Request Managed Products

```cpp
sdkbox::HMS::iapRequestProducts();
```
this method will trigger `onIAPProducts` event

### Purchase Managed Product

```cpp
sdkbox::HMS::iapPurchase("coin");
```
this method will trigger `onIAPPurchase` event

### Purchase Unmanaged Product

```cpp
const std::string productInfo = R"(
{
  "priceType": 0, //0:consumable 1:non-consumable 2:subscription
  "productName": "product name",
  "productId": "product id",
  "amount": "1.00",
  "currency": "CNY",
  "country": "CN",
  "sdkChannel": "1", // sdkChannel size must be between 0 and 4
  "serviceCatalog": "X58",
  "reservedInfor": "{\"a\": 1, \"b\":\"s\"}", // reservedInfor must be json string
  "developerPayload": "payload1"
}
)";
sdkbox::HMS::iapPurchaseWithPrice(productInfo);
```
this method will trigger `onIAPPurchase` event

### request owned purchase

will return current user own products, include non-consumable, subscription product and consumable product which have not be consumed.

```cpp
sdkbox::HMS::iapRequestOwnedPurchases();
```
this method will trigger `onIAPOwnedPurchases` event

### consume product

```cpp
sdkbox::HMS::iapConsume(purchaseToken);
```
this method will trigger `onIAPPConsume` event

### request owned purchase record

request current user's all purchase records.
```cpp
sdkbox::HMS::iapRequestOwnedPurchaseRecords(purchaseToken);
```
this method will trigger `onIAPOwnedPurchaseRecords` event

### Handling HMS Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.

* Allow your class to extend `sdkbox::HMSListener`:
```cpp
#include "PluginHMS/PluginHMS.h"
class MyClass : public sdkbox::HMSListener {
private:
  virtual void onLogin(int code, const std::string &msg) override;
  virtual void onIAPReady(int code, const std::string& msg) override;
  virtual void onIAPProducts(int code, const std::string& errorOrJson) override;
  virtual void onIAPPurchase(int code, const std::string& errorOrJson) override;
  virtual void onIAPPConsume(int code, const std::string& errorOrJson) override;
  virtual void onIAPOwnedPurchases(int code, const std::string& errorOrJson) override;
  virtual void onIAPOwnedPurchaseRecords(int code, const std::string& errorOrJson) override;
}
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::HMS::setListener(listener);
```
