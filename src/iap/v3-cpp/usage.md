### Initialize IAP
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginIAP/PluginIAP.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::IAP::init();
}
```

### Retrieve latest Product data
It's always a good idea to retrieve the latest product data from store when your game starts.

To retrieve latest IAP data, simply call `sdkbox::IAP::refresh()`.

> `onProductRequestSuccess` will be trigged if retrieved successfully.

> `onProductRequestFailure` will be trigged if exception occurs.

### Make a purchase
To make a purchase call `sdkbox::IAP::purchase(name)`

__Note:__ __name__ is the name of the IAP item in your config file under `items` tag, not the product id you set in iTunes or GooglePlay Store

> `onSuccess` will be triggered if purchase is successful.

> `onFailure` will be triggered if purchase fails.

> `onCanceled` will be triggered if purchase is canceled by user.

### Restore purchase
To restore purchase call `sdkbox::IAP::restore()`.

> `onRestored` will be triggered if restore is successful.

__Note:__ `onRestored` could be triggered multiple times

### Handling Purchase Events
This allows you to catch the `IAP` events so that you can perform operations based upon the response from your players and IAP servers.

* Allow your class to extend `sdkbox::IAPListener`:
```cpp
#include "PluginIAP/PluginIAP.h"
class MyClass : public sdkbox::IAPListener
{
private:
  virtual void onInitialized(bool ok) override;
  virtual void onSuccess(sdkbox::Product const& p) override;
  virtual void onFailure(sdkbox::Product const& p, const std::string &msg) override;
  virtual void onCanceled(sdkbox::Product const& p) override;
  virtual void onRestored(sdkbox::Product const& p) override;
  virtual void onProductRequestSuccess(std::vector<sdkbox::Product> const &products) override;
  virtual void onProductRequestFailure(const std::string &msg) override;
  void onRestoreComplete(bool ok, const std::string &msg);
}
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::IAP::setListener(listener);
```

### Verify IAP receipt
IAP receipt information is not sent by default, you can use the following API to turn on the IAP receipts
```cpp
sdkbox::IAP::enableUserSideVerification(true);
```
And check `product.receipt` and `product.receiptCipheredPayload` for IAP receipt data in `onSuccess` callback
> Note: only Google Play provides receipt data, iOS only provides ciphered payload for user to perform IAP verification