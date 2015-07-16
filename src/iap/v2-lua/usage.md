### Modify `AppDelegate.cpp`
* Modify `AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginIAPLua.hpp"
#include "PluginIAPLuaHelper.hpp"
```

* Second, We need to register the plugin with Lua. This is done by making a call to `register_all_PluginIAPLua(<lua_State*>);`. It is important to note that this call must be made after `lua_State *tolua_s = pStack->getLuaState();` and before `tolua_extensions_ccb_open(tolua_s);`. Here is an example of what this might look like for you:
```lua
lua_State *tolua_s = pStack->getLuaState();
register_all_PluginIAPLua(tolua_s);
register_all_PluginIAPLua_helper(tolua_s);
tolua_extensions_ccb_open(tolua_s);
```

### Initialize IAP
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.IAP:init()
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
