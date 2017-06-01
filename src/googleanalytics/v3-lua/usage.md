### Initialize Google Analytics
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginGoogleAnalytics:init()
```

You can always manually stop recording events at any time by calling:
```lua
sdkbox.PluginGoogleAnalytics:stopSession();
```

However, in-order to record events again you must then manually call:
```lua
sdkbox.PluginGoogleAnalytics:startSession();
```

Logged data usually shows up within one day.


### Use ECommerce API Sample

* make sure ecommerce tracking is enable [here](https://support.google.com/analytics/answer/1009612)

* track purchase

```lua
    local ecommerceInfo = {
        -- transaction info
        action = 'purchase',
        transaction = 'T12345',
        affiliation = 'Google Store - Online',
        transactionCouponCode = 'SUMMER2017',
        revenue = '37.39',
        tax = '2.85',
        shipping = '5.34',

        -- product info
        productID = 'P12345',
        productName = 'Android Warhol T-Shirt',
        category = 'Apparel/T-Shirts',
        brand = 'SDKBox',
        productVariant = 'black',
        productCouponCode = 'APPARELSALE',
        price = '29.20',
        quantity = '1',

        -- currency code
        -- https://support.google.com/analytics/answer/6205902?#supported-currencies
        currencyCode = 'EUR'
    }

    sdkbox.PluginGoogleAnalytics:logECommerce(ecommerceInfo)
```

* track refund
```js
    local ecommerceInfo = {
        // transaction info
        action = 'refund',
        transaction = 'T12345'
    };

    sdkbox.PluginGoogleAnalytics:logECommerce(ecommerceInfo);
```

* track partial refund
```js
    local ecommerceInfo = {
        // transaction info
        action = 'refund',
        transaction = 'T12345',

        // product info
        productID = 'P12345',
        quantity = '1'
    };

    sdkbox.PluginGoogleAnalytics:logECommerce(ecommerceInfo);
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
