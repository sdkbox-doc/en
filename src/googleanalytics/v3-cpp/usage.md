### Initialize Google Analytics
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginGoogleAnalytics/PluginGoogleAnalytics.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginGoogleAnalytics::init();
}
```

You can always manually stop recording events at any time by calling:
```cpp
sdkbox::PluginGoogleAnalytics::stopSession();
```

However, in-order to record events again you must then manually call:
```cpp
sdkbox::PluginGoogleAnalytics::startSession();
```

Logged data usually shows up within one day.

### Use ECommerce API Sample

* make sure ecommerce tracking is enable [here](https://support.google.com/analytics/answer/1009612)

* track purchase

```cpp
    std::map<std::string, std::string> info;

    // transaction info
    info["action"] = "purchase";
    info["transaction"] = "T12345";
    info["affiliation"] = "Google Store - Online";
    info["transactionCouponCode"] = "SUMMER2017";
    info["revenue"] = "37.39";
    info["tax"] = "2.85";
    info["shipping"] = "5.34";

    // product info
    info["productID"] = "P12345";
    info["productName"] = "Android Warhol T-Shirt";
    info["category"] = "Apparel/T-Shirts";
    info["brand"] = "SDKBox";
    info["productVariant"] = "black";
    info["productCouponCode"] = "APPARELSALE";
    info["price"] = "29.20";
    info["quantity"] = "1";

    // currency code
    // https://support.google.com/analytics/answer/6205902?#supported-currencies
    info["currencyCode"] = "EUR";

    PluginGoogleAnalytics::logECommerce(info);
```

* track refund
```cpp
    std::map<std::string, std::string> info;

    // transaction info
    info["action"] = "refund";
    info["transaction"] = "T12345";

    PluginGoogleAnalytics::logECommerce(info);
```

* track partial refund
```cpp
    std::map<std::string, std::string> info;

    // transaction info
    info["action"] = "refund";
    info["transaction"] = "T12345";

    // product info
    info["productID"] = "P12345";
    info["quantity"] = "1";

    PluginGoogleAnalytics::logECommerce(info);
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
