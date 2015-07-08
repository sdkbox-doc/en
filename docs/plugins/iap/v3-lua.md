<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/iap/v3-cpp
-->

##Overview
Provides you one stop solution for IAP integration across multiple platform, SDKBOX IAP offers easy to use yet powerful API, really simplify the tedious process of implementing IAPs in your game.

##Integration

Use the following command to install SDKBOX IAP plugin, Make sure you setup SDKBOX installer correctly.
```bash
sdkbox import -b iap
```

##Extra steps

### Edit `Cocos2dxActivity.java`
*   `Cocos2dxActivity.java` is located:

    ```
  /frameworks/runtime-src/proj.android/src/org/cocos2dx/
  lib/Cocos2dxActivity.java
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

Here is an example of IAP configuration, you need to replace `<put the product id for ios here>` with the product id from your [iTunes Connect](http://itunesconnect.apple.com) or [Google Play Console](https://play.google.com/apps/publish)
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
        "key":"put your googleplay key here",
        "items":{
          "remove_ads":{
              "id":"<put the product id for android here>"
          }
        }
    }
}
```
##Usage
### Modify Lua Code
Modify `lua_module_register.h` to include the necessary headers and calls to register `IAP` with Lua. Note this takes a parameter of __lua_State*__:
```cpp
#include "PluginIAPLua.hpp"
#include "PluginIAPLuaHelper.h"
```
```cpp
register_all_PluginIAPLua(L);
register_PluginIAPLua_helper(L);
```

### Initialize IAP
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.IAP:init();
```

### Retrieve latest Product data
It's always a good idea to retrieve the latest product data from store when your game starts.

To retrieve latest IAP data, simply call `sdkbox.IAP:refresh()`.

> `onProductRequestSuccess` if retrieved successfully.

> `onProductRequestFailure` if exception occurs.

### Make a purchase
To make a purchase call `sdkbox.IAP:purchase(name)`

__Note:__ __name__ is the name of the IAP item in your config file under `items` tag, not the product id you set in iTunes or GooglePlay Store

> `onSuccess` will be triggered if purchase is successful.

> `onFailure` will be triggered if purchase fails.

> `onCanceled` will be triggered if purchase is canceled by user.

### Restore purchase
To restore purchase call `sdkbox.IAP:restore()`.

> `onRestored` will be triggered if restore is successful.

__Note:__ `onRestored` could be triggered multiple times

### Handling Purchase Events
This allows you to catch the `IAP` events so that you can perform operations based upon the response from your players and IAP servers.
```lua
sdkbox.IAP:setListener(function(args)
        if "onSuccess" == args.event then
                local product = args.product
                dump(product, "onSuccess:")
        elseif "onFailure" == args.event then
                local product = args.product
                local msg = args.msg
                dump(product, "onFailure:")
                print("msg:", msg)
        elseif "onCanceled" == args.event then
                local product = args.product
                dump(product, "onCanceled:")
        elseif "onRestored" == args.event then
                local product = args.product
                dump(product, "onRestored:")
        elseif "onProductRequestSuccess" == args.event then
                local products = args.products
                dump(products, "onProductRequestSuccess:")
        elseif "onProductRequestFailure" == args.event then
                local msg = args.msg
                print("msg:", msg)
        else
                print("unknow event ", args.event)
        end
end)
```

## API Reference

### Methods
```lua
sdkbox.IAP:init();
```
> Initialize SDKBox IAP

```lua
sdkbox.IAP:setDebug(debug);
```
> Enable/disable debug logging

```lua
sdkbox.IAP:purchase(name);
```
> Make a purchase request

```lua
sdkbox.IAP:refresh();
```
> Refresh the IAP data(title, price, description)

```lua
sdkbox.IAP:restore();
```
> Restore purchase

```lua
sdkbox.IAP:setListener(listener);
```
> Set listener for IAP

```lua
sdkbox.IAP:removeListener();
```
> Remove listener for IAP

### Listeners
```lua
sdkbox.IAP:onSuccess(product);
```
> Called when an IAP processed successfully

```lua
sdkbox.IAP:onFailure(product, message);
```
> Called when an IAP fails

```lua
sdkbox.IAP:onCanceled(product);
```
> Called when user canceled the IAP

```lua
sdkbox.IAP:onRestored(product);
```
> Called when server returns the IAP items user already purchased

```lua
sdkbox.IAP:onProductRequestSuccess(products);
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```lua
sdkbox.IAP:onProductRequestFailure(message);
```
> Called when the product request fails


