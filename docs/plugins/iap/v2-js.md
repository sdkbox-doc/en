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
### Modify `<YourGameName>.java`
* Modify `proj.android/src/<package identifier>/<YourGameName>.java` to add the following imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* Second, modify the class to edit the `onCreate(final Bundle savedInstanceState)` function to add a call to `SDKBox.init(this);`. Example of what this might look like for you:
```java
protected void onCreate(Bundle savedInstanceState){
  super.onCreate(savedInstanceState);
  SDKBox.init(this);
}
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


## API Reference

### Methods
```javascript
sdkbox.IAP.init();
```
> Initialize SDKBox IAP

```javascript
sdkbox.IAP.setDebug(debug);
```
> Enable/disable debug logging

```javascript
sdkbox.IAP.purchase(name);
```
> Make a purchase request

```javascript
sdkbox.IAP.refresh();
```
> Refresh the IAP data(title, price, description)

```javascript
sdkbox.IAP.restore();
```
> Restore purchase

```javascript
sdkbox.IAP.setListener(listener);
```
> Set listener for IAP

```javascript
sdkbox.IAP.removeListener();
```
> Remove listener for IAP

### Listeners
```javascript
sdkbox.IAP.onSuccess(product);
```
> Called when an IAP processed successfully

```javascript
sdkbox.IAP.onFailure(product, message);
```
> Called when an IAP fails

```javascript
sdkbox.IAP.onCanceled(product);
```
> Called when user canceled the IAP

```javascript
sdkbox.IAP.onRestored(product);
```
> Called when server returns the IAP items user already purchased

```javascript
sdkbox.IAP.onProductRequestSuccess(products);
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```javascript
sdkbox.IAP.onProductRequestFailure(message);
```
> Called when the product request fails

