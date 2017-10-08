About the details of these methods depicted below, you can access the section [API Reference](#api_reference). And if you wanna know the corresponding functions in Facebook Gameroom SDK, you can refer to [Facebook Gameroom SDK website](https://developers.facebook.com/docs/games/gameroom/sdk).

### Initialize Plugin Gameroom

Before you call other APIs, you should Initialize the plugin in `app.js`.
```
sdkbox.PluginGameroom.init('your_facebook_app_id');
```

### Set Listener

As other SDKBOX plugins, you need to set a listener object to handle events.

```
sdkbox.PluginGameroom.setListener({
    onLoginAccessTokenMsg: function (handle) {
    },

    onFeedShareMsg: function (handle) {
    },

    onPurchaseIAPMsg: function (handle) {
    },

    onHasLicenseMsg: funciton (handle) {
    },

    onAppRequestMsg: function (handle) {
    }
});
```

Each callback will be explained below.

### User Login

After the plugin is initialized, when your game starts, you should make a login call to retrieve player information. You can use a simple method `login()` or another method `loginWithScopes` for it.

The different between these two methods is that `login()` method will always apply 3 permissions of the player: `user_friends`, `email` and `public_profile`.

```
sdkbox.PluginGameroom.login()
```

But you can pass some parameters to `loginWithScopes()` method to designate witch permissions are applied. In this example, `public_profile` and `email` will be applied.

```
sdkbox.PluginGameroom.loginWithScopes(2, ['public_profile', 'email']);
```

You can also check whether the player has logged in:

```
ret = sdkbox.PluginGameroom.isLoggedIn();
```

The player login action will trigger `onLoginAccessTokenMsg` callback in your listener object. For examle, you can use some properties to retrieve the player's login information via the parameter `handle`.

```
onLoginAccessTokenMsg: function (handle) {
    cc.log('============');
    cc.log('onLoginAccessTokenMsg');
    cc.log(JSON.stringify(handle, null, 2));
    if (handle.isValidToken) {
        self.showText('login successful');
    }
    else {
        self.showText('login failed');
    }
}
```

### Feed Share

In your game, you can offer the sharing function to the players:

```
sdkbox.PluginGameroom.feedShare(
        '',
        'https://www.facebook.com',
        'Testing Link Name',
        'Testing Link Caption',
        'Testing Link Description',
        'http://www.pamperedpetz.net/wp-content/uploads/2015/09/Puppy1.jpg',
        ''
);
```

Above example shares an image to the player's Facebook.

In your listener object, `onFeedShareMsg` will be called after sharing with the argument `handle`. `Post ID` can be returned if you access the property of `handle`.

```
onFeedShareMsg: function (handle) {
    cc.log('============');
    cc.log('onFeedShareMsg');
    self.showText('onFeedShareMsg');
    cc.log('shared post id = ' + handle.postID);

}
```

### IAP

IAP funciton includes 3 aspects:

-   IAP with a product ID configured in your Facebook App.

```
sdkbox.PluginGameroom.purchaseIAP(
        'sdkbox_product_1',
        1,
        1,
        1,
        '',
        '',
        ''
);
```

-   IAP with an url link.

```
sdkbox.PluginGameroom.purchaseIAPWithProductURL(
        'https://friendsmash-unity.herokuapp.com/payments/100coins.php',
        1,
        1,
        1,
        '',
        '',
        ''
);
```

-   Purchase a premium version or license.

```
sdkbox.PluginGameroom.payPremium();
```

These 3 types of IAP will trigger `onPurchaseIAPMsg` callback. Here is an example to show how to handle the IAP result.

```
onPurchaseIAPMsg: function (handle) {
    cc.log('============');
    cc.log('onPurchaseIAPMsg');
    self.showText('onPurchaseIAPMsg');
    cc.log('payment ID = '+ handle.paymentID);
    cc.log('amount = ' + handle.amount);
    cc.log('curency = ' + handle.currency);
    cc.log('purchase time = ' + handle.purchaseTime);
    cc.log('product ID = ' + handle.productID);
    cc.log('purchase token = ' + handle.purchaseToken);
    cc.log('quantity = ' + handle.quantity);
    cc.log('request id = ' + handle.requestID);
    cc.log('status = ' + handle.status);
    cc.log('signed req = ' + handle.signedReq);
    cc.log('error code = ' + handle.errorCode);
    cc.log('error msg = ' + handle.errorMsg);

}
```

In addtion, you can use `hasLicense()` method to check whether the player has got the license or premium version.

```
sdkbox.PluginGameroom.hasLicense();
```

Please note that this checking operation will trigger a callback named `onHasLicenseMsg`. Bizarrely, you should get the license ID via the property `hasLicense` of `handle` object in callback(Faceebook Gameroom SDK demands these behaviors).

```
onHasLicenseMsg: function (handle) {
    cc.log('============');
    cc.log('onHasLicenseMsg');
    self.showText('onHasLicenseMsg');
    cc.log('has license = ' + handle.hasLicense);
}

```

### Send App Events

You can log app events for Facebook Analytics via the following functions:

```
sdkbox.PluginGameroom.logAppEvent('test_event_1', { 'key1': 'val1', 'key2': 'val2' });
sdkbox.PluginGameroom.logAppEventWithValueToSum('test_event_2', { 'key3': 'val3', 'key4': 'val4' }, 10.24);
```

The key-value pairs are carried in an JavaScript object. And if you intend to offer an extra value in an event, you should use `logAppEventWithValueToSum()` method.

### Send App Requests

To invoke an app request within your game, you may use the following call to trigger the dialog:

```
sdkbox.PluginGameroom.appRequest('hello, try this js demo.', '', '', 'faceboo_user_id_1, facebook_user_id_2', '', '', 20, '', 'hello');
```

In common, you don't need to set the users' ID in order to let the player choose which friends he want to send the requests.

```
sdkbox.PluginGameroom.appRequest('hello, try this js demo.', '', '', '', '', '', 20, '', 'hello');
```

In the callback of sending app requests,  you can hanedle the result:

```
onAppRequestMsg: function (handle) {
    cc.log('============');
    cc.log('onAppRequestMsg');
    self.showText('onAppRequestMsg');
    cc.log('objectID = ' + handle.objectID);
    cc.log('to user: ' + handle.toUser);
}
```
