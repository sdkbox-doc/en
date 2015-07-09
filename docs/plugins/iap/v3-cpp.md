<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/iap/v3-cpp
-->

#In-App Purchase

##Integration
Use the following command to install the SDKBOX IAP plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import -b iap
```

##Extra steps
### Modify `Cocos2dxActivity.java`
* If you're using cocos2d-x from source, assuming you are in the `proj.android` directory, `Cocos2dxActivity.java` is located:

    ```
    ../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/
    lib/Cocos2dxActivity.java
    ```

* If you're using the prebuilt cocos2d-x libraries assuming you are in the `proj.android` directory, `Cocos2dxActivity.java` is located:

    ```
    ./src/org/cocos2dx/lib/Cocos2dxActivity.java
    ```

  __Note:__ When using Cocos2d-x from source, different versions have `Cocos2dxActivity.java` in a different location. One way to find the location is to look in `proj.android/project.properties`. Example:
```
android.library.reference.1=../../cocos2d-x/cocos/platform/android/java
```

In this case, `Cocos2dxActivity.java` should be located at:

```
../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/lib/Cocos2dxActivity.java
```

* Modify `Cocos2dxActivity.java` to add the following imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* Second, modify `Cocos2dxActivity` to edit the `onCreate(final Bundle savedInstanceState)` function to add a call to `SDKBox.init(this);`. The placement of this call is important. It must be done after the call to `onLoadNativeLibraries();`. Example:
```java
onLoadNativeLibraries();
SDKBox.init(this);
```

* Last, we need to insert the proper __overrides__ code. There are a few rules here.
    * If the method listed has not been defined, __add it__.

    * If the method listed has been defined, add the calls to `SDKBox` in the __same__ existing function.
```java
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
          if(!SDKBox.onActivityResult(requestCode, resultCode, data)) {
            super.onActivityResult(requestCode, resultCode, data);
          }
    }
    @Override
    protected void onStart() {
          super.onStart();
          SDKBox.onStart();
    }
    @Override
    protected void onStop() {
          super.onStop();
          SDKBox.onStop();
    }
    @Override
    protected void onResume() {
          super.onResume();
          SDKBox.onResume();
    }
    @Override
    protected void onPause() {
          super.onPause();
          SDKBox.onPause();
    }
    @Override
    public void onBackPressed() {
          if(!SDKBox.onBackPressed()) {
            super.onBackPressed();
          }
    }
```


## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the IAP configuration, you need to replace `<put the product id for ios here>` with the product id from your [iTunes Connect](http://itunesconnect.apple.com) or  replace `<put your googleplay key here>` from your [Google Play Console](https://play.google.com/apps/publish)
```json
"ios" :
{
    "iap":{
        "items":{
            "remove_ads":{
                "id":"<put the product id for ios here>"
            }
        }
    }
},
"android":
{
    "iap":{
        "key":"<put your googleplay key here>",
        "items":{
          "remove_ads":{
              "id":"<put the product id for android here>"
          }
        }
    }
}
```

##Usage

### Initialize IAP
* Call `sdkbox::IAP::init();` where appropriate in your code. We
recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginIAP/PluginIAP.h"
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
        virtual void onSuccess(sdkbox::Product const& p) override;
        virtual void onFailure(sdkbox::Product const& p, const std::string &msg)
           override;
        virtual void onCanceled(sdkbox::Product const& p) override;
        virtual void onRestored(sdkbox::Product const& p) override;
        virtual void onProductRequestSuccess(std::vector<sdkbox::Product> const &products)
        override;
        virtual void onProductRequestFailure(const std::string &msg) override;
    }
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::IAP::setListener(listener);
```

## API Reference

### Methods
```cpp
static void init();
```
> Initialize SDKBox IAP

```cpp
static void setDebug(bool debug);
```
> Enable/disable debug logging

```cpp
static void purchase(const std::string& name);
```
> Make a purchase request

```cpp
static void refresh();
```
> Refresh the IAP data(title, price, description)

```cpp
static void restore();
```
> Restore purchase

```cpp
static void setListener(IAPListener* listener);
```
> Set listener for IAP

```cpp
static void removeListener();
```
> Remove listener for IAP

### Listeners
```cpp
virtual void onSuccess(const Product& p) = 0;
```
> Called when an IAP processed successfully

```cpp
virtual void onFailure(const Product& p, const std::string& msg) = 0;
```
> Called when an IAP fails

```cpp
virtual void onCanceled(const Product& p) = 0;
```
> Called when user canceled the IAP

```cpp
virtual void onRestored(const Product& p) = 0;
```
> Called when server returns the IAP items user already purchased

```cpp
virtual void onProductRequestSuccess(const std::vector<Product>& products) = 0;
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```cpp
virtual void onProductRequestFailure(const std::string& msg) = 0;
```
> Called when the product request fails

