
### Initialize IAP
* Call `sdkbox.IAP.init();` where appropriate in your code. We
recommend to do this in the `app.js`

* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginIAPJS.hpp"
#include "PluginIAPJSHelper.hpp"
```

* Modify `AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginIAPJS);
sc->addRegisterCallback(register_all_PluginIAPJS_helper);
```
This registers the Javascript callbacks.

### Retrieve latest Product data
It's always a good idea to retrieve the latest product data from store when your game starts.

To retrieve latest IAP data, simply call `sdkbox.IAP.refresh()`.

> `onProductRequestSuccess` if retrieved successfully.

> `onProductRequestFailure` if exception occurs.

### Make a purchase
To make a purchase call `sdkbox.IAP.purchase(name)`

__Note:__ __name__ is the name of the IAP item in your config file under `items` tag, not the product id you set in iTunes or GooglePlay Store

> `onSuccess` will be triggered if purchase is successful.

> `onFailure` will be triggered if purchase fails.

> `onCanceled` will be triggered if purchase is canceled by user.

### Restore purchase
To restore purchase call `sdkbox.IAP.restore()`.

> `onRestored` will be triggered if restore is successful.

__Note:__ `onRestored` could be triggered multiple times

### Handling Purchase Events
This allows you to catch the `IAP` events so that you can perform operations based upon the response from your players and IAP servers.
```Javascript
sdkbox.IAP.setListener({
    onSuccess : function (product) {
        //Purchase success
    },
    onFailure : function (product, msg) {
        //Purchase failed
        //msg is the error message
    },
    onCanceled : function (product) {
        //Purchase was canceled by user
    },
    onRestored : function (product) {
        //Purchase restored
    },
    onProductRequestSuccess : function (products) {
        //Returns you the data for all the iap products
        //You can get each item using following method
        for (var i = 0; i < products.length; i++) {
            // loop
        }
    },
    onProductRequestFailure : function (msg) {
        //When product refresh request fails.
    }
});
```
