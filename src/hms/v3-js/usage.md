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

### Request Managed Products

```javascript
sdkbox.HMS.iapRequestProducts();
```
this method will trigger `onIAPProducts` event

### Purchase Managed Product

```javascript
sdkbox.HMS.iapPurchase("coin");
```
this method will trigger `onIAPPurchase` event

### Purchase Unmanaged Product

```javascript
let productInfo = {
  priceType: 0, // 0:consumable 1:non-consumable 2:subscription
  productName: 'product name',
  productId: 'product id',
  amount: '1.00',
  currency: 'CNY',
  country: 'CN',
  sdkChannel: '1', // sdkChannel size must be between 0 and 4
  serviceCatalog: 'X58',
  reservedInfor: '{"a": 1, "b":"s"}', // reservedInfor must be json string
  developerPayload: 'payload1'
};
sdkbox.HMS.iapPurchaseWithPrice(JSON.stringify(productInfo));
```
this method will trigger `onIAPPurchase` event

### request owned purchase

will return current user own products, include non-consumable, subscription product and consumable product which have not be consumed.

```javascript
sdkbox.HMS.iapRequestOwnedPurchases();
```
this method will trigger `onIAPOwnedPurchases` event

### consume product

```javascript
sdkbox.HMS.iapConsume(purchaseToken);
```
this method will trigger `onIAPPConsume` event

### request owned purchase record

request current user's all purchase records.
```javascript
sdkbox.HMS.iapRequestOwnedPurchaseRecords(purchaseToken);
```
this method will trigger `onIAPOwnedPurchaseRecords` event

### Handling Purchase Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.
```Javascript
sdkbox.HMS.setListener({
    onLogin : function (code, msg) {
        // login event
    },
    onIAPReady: function(code, msg) {
        self.log('HMS Listener onIAPReady:' + code);
        cc.log(msg);
    },
    onIAPProducts: function(code, msg) {
        self.log('HMS Listener onIAPProducts:' + code);
        cc.log(msg);
    },
    onIAPPurchase: function(code, msg) {
        self.log('HMS Listener onIAPPurchase:' + code);
        cc.log(msg);
    },
    onIAPPConsume: function(code, msg) {
        self.log('HMS Listener onIAPPConsume:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchases: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchases:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchaseRecords: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchaseRecords:' + code);
        cc.log(msg);
    }
});
```
