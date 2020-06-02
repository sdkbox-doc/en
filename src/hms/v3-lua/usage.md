### Initialize HMS
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.HMS:init()
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```lua
sdkbox.HMS:login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```lua
sdkbox.HMS:login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```lua
sdkbox.HMS:login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```lua
sdkbox.HMS:logout();
```

### Request Managed Products

```lua
sdkbox.HMS:iapRequestProducts();
```
this method will trigger `onIAPProducts` event

### Purchase Managed Product

```lua
sdkbox.HMS:iapPurchase("coin");
```
this method will trigger `onIAPPurchase` event

### Purchase Unmanaged Product

```lua
local productInfo = {
  priceType = 0, -- 0:consumable 1:non-consumable 2:subscription
  productName = 'product name',
  productId = 'product id',
  amount = '1.00',
  currency = 'CNY',
  country = 'CN',
  sdkChannel = '1', -- sdkChannel size must be between 0 and 4
  serviceCatalog = 'X58',
  reservedInfor = '{"a": 1, "b":"s"}', -- reservedInfor must be json string
  developerPayload = 'payload1'
};
sdkbox.HMS:iapPurchaseWithPrice(JSON:encode(productInfo));
```
this method will trigger `onIAPPurchase` event

### request owned purchase

will return current user own products, include non-consumable, subscription product and consumable product which have not be consumed.

```lua
sdkbox.HMS:iapRequestOwnedPurchases();
```
this method will trigger `onIAPOwnedPurchases` event

### consume product

```lua
sdkbox.HMS:iapConsume(purchaseToken);
```
this method will trigger `onIAPPConsume` event

### request owned purchase record

request current user's all purchase records.
```lua
sdkbox.HMS:iapRequestOwnedPurchaseRecords(purchaseToken);
```
this method will trigger `onIAPOwnedPurchaseRecords` event


### Handling Purchase Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.
```lua
sdkbox.HMS:setListener(function(args)
        if "onLogin" == args.event then
                local code = args.code
                local msg = args.msg
                dump(args, "onLogin:")
        else if "onIAPReady" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPProducts" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPPurchase" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPPConsume" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPOwnedPurchases" == args.event then
                local code = args.code
                local msg = args.msg
        else if "onIAPOwnedPurchaseRecords" == args.event then
                local code = args.code
                local msg = args.msg
        else
                print("unknown event ", args.event)
        end
end)
```
