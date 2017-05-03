### Register Javascript Functions
You need to register all the Google Analytics JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginGoogleAnalyticsJS.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginGoogleAnalyticsJS);
```

### Initialize Google Analytics
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginGoogleAnalytics.init();
```

You can always manually stop recording events at any time by calling:
```javascript
sdkbox.PluginGoogleAnalytics.stopSession();
```

However, in-order to record events again you must then manually call:
```javascript
sdkbox.PluginGoogleAnalytics.startSession();
```

Logged data usually shows up within one day.

### Use ECommerce API Sample

* make sure ecommerce tracking is enable [here](https://support.google.com/analytics/answer/1009612)

* track purchase

```js
    const ecommerceInfo = {
        // transaction info
        action: 'purchase',
        transaction: 'T12345',
        affiliation: 'Google Store - Online',
        transactionCouponCode: 'SUMMER2017',
        revenue: '37.39',
        tax: '2.85',
        shipping: '5.34',

        // product info
        productID: 'P12345',
        productName: 'Android Warhol T-Shirt',
        category: 'Apparel/T-Shirts',
        brand: 'SDKBox',
        productVariant: 'black',
        productCouponCode: 'APPARELSALE',
        price: '29.20',
        quantity: '1',

        // currency code
        // https://support.google.com/analytics/answer/6205902?#supported-currencies
        currencyCode: 'EUR'
    };

    sdkbox.PluginGoogleAnalytics.logECommerce(ecommerceInfo);
```

* track refund
```js
    const ecommerceInfo = {
        // transaction info
        action: 'refund',
        transaction: 'T12345',
    };

    sdkbox.PluginGoogleAnalytics.logECommerce(ecommerceInfo);
```

* track partial refund
```js
    const ecommerceInfo = {
        // transaction info
        action: 'refund',
        transaction: 'T12345',

        // product info
        productID: 'P12345',
        quantity: '1',
    };

    sdkbox.PluginGoogleAnalytics.logECommerce(ecommerceInfo);
```

"action" key value:

 - "detail"
 - "click"
 - "add"
 - "remove"
 - "checkout"
 - "checkout_option"
 - "purchase"
 - "refund"

"quantity" key value is `int` fromat, DO NOT use float format

more info, take a look at here [ios](https://developers.google.com/analytics/devguides/collection/ios/v3/enhanced-ecommerce) and [android](https://developers.google.com/analytics/devguides/collection/android/v4/enhanced-ecommerce)
