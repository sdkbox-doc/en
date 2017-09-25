About the details of these methods depicted below, you can access the section [API Reference](#api_reference). And if you wanna know the corresponding functions in Facebook Gameroom SDK, you can refer to [Facebook Gameroom SDK website](https://developers.facebook.com/docs/games/gameroom/sdk).

### Initialize Plugin Gameroom

Before you call other APIs, you should Initialize the plugin. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```
#ifdef SDKBOX_ENABLED
#include "PluginGameroom.h"
#endif


bool AppDelegate::applicationDidFinishLaunching() {
#ifdef SDKBOX_ENABLED
    // fill your Facebook Application ID
    sdkbox::PluginGameroom::init("1234567890");
#endif
}
```

### Set Listener

As other SDKBOX plugins, you need to set a listener class to handle events.

```
sdkbox::PluginGameroom::setListener(pointer_to_listener_class);
```

The listener class should inherit from `sdkbox::GameroomListener`.

```
class HelloWorldListener : public sdkbox::GameroomListener
{
    public:
        // ...

        virtual void onLoginAccessTokenMsg(sdkbox::AccessTokenHandle);
        virtual void onFeedShareMsg(sdkbox::FeedShareHandle);
        virtual void onPurchaseIAPMsg(sdkbox::PurchaseHandle);
        virtual void onHasLicenseMsg(sdkbox::HasLicenseHandle);
        virtual void onAppRequestMsg(sdkbox::AppRequestHandle);

};
```

Each callback will be explained below.

### User Login

After the plugin is initialized, when your game starts, you should make a login call to retrieve player information. You can use a simple method `login()` or another method `loginWithScopes` for it.

The different between these two methods is that `login()` method will always apply 3 permissions of the player: `user_friends`, `email` and `public_profile`.

```
SDKBOX::PluginGameroom::login();
```

But you can pass some parameters to `loginWithScopes()` method to designate witch permissions are applied. In this example, `user_friends` and `email` will be applied.

```
std::vector<std::string> loginScopes{ "user_friends", "email" };
sdkbox::PluginGameroom::loginWithScopes(2, loginScopes);
```

You can also check whether the player has logged in:

```
auto ret = sdkbox::PluginGameroom::isLoggedIn();
if (!ret) {
    // do something
}
```

The player login action will trigger `onLoginAccessTokenMsg` callback in your listener class. For examle, you can use some methods to retrieve the player's login information via the parameter `accessTokenHandle`.

```
void HelloWorld::onLoginAccessTokenMsg(sdkbox::AccessTokenHandle accessTokenHandle) {
    auto isValid = sdkbox::PluginGameroom::accessTokenIsValid(accessTokenHandle);
    if (!isValid) {
        // user not logged in
        return;
    }
    auto userid = sdkbox::PluginGameroom::accessTokenGetUserID(accessTokenHandle);

    char token_string[512];
    auto size = sdkbox::PluginGameroom::accessTokenGetTokenString(accessTokenHandle, token_string, 512);
    auto expiration_timestamp = sdkbox::PluginGameroom::accessTokenGetExpirationTimestamp(accessTokenHandle);

    fbgLoginScope permissions[512];
    auto permission_size = sdkbox::PluginGameroom::accessTokenGetPermissions(accessTokenHandle, permissions, 512);

    ::CCLOG(
        "OnLoginAccessTokenMsg, User ID: %lld\nAccess Token: %s\nExpiration Timestamp: %lld, Permission Count: %zu\nPermissions: ",
        (long long)userid,
        token_string,
        (long long)expiration_timestamp,
        permission_size
    );

    for (size_t i = 0; i < permission_size; i++) {
        ::CCLOG("%s", sdkbox::PluginGameroom::loginScopeToString(permissions[i]));
    }
    ::CCLOG("\n");
}
```

### Feed Share

In your game, you can offer the sharing function to the players:

```
sdkbox::PluginGameroom::feedShare(
    nullptr,
    "https://www.facebook.com",
    "Testing Link Name",
    "Testing Link Caption",
    "Testing Link Description",
    "http://www.pamperedpetz.net/wp-content/uploads/2015/09/Puppy1.jpg",
    nullptr
);

```

Above example shares an image to the player's Facebook.

In your listener class, `onFeedShareMsg` will be called after sharing with the argument `feedShareHandle`. `Post ID` can be returned if you call the method `feedShareGetPostID()`.

```
void HelloWorld::onFeedShareMsg(sdkbox::FeedShareHandle feedShareHandle) {
    auto postId = sdkbox::PluginGameroom::feedShareGetPostID(feedShareHandle);
    ::CCLOG(
        "onFeedShareMsg, Feed Share Post ID: %ld\n",
        (long)postId
    );
}
```

### IAP

IAP funciton includes 3 aspects:

-   IAP with a product ID configured in your Facebook App.

```
sdkbox::PluginGameroom::purchaseIAP(
    "sdkbox_product_2",
    1,
    1,
    1,
    nullptr,
    nullptr,
    nullptr
);
```

-   IAP with an url link.

```
sdkbox::PluginGameroom::purchaseIAPWithProductURL(
    "https://friendsmash-unity.herokuapp.com/payments/100coins.php",
    1,
    1,
    1,
    nullptr,
    nullptr,
    nullptr
);
```

-   Purchase a premium version or license.

```
sdkbox::PluginGameroom::payPremium();
```

These 3 types of IAP will trigger `onPurchaseIAPMsg` callback. Here is an example to show how to handle the IAP operation.

```
void HelloWorld::onPurchaseIAPMsg(sdkbox::PurchaseHandle payHandle) {
    size_t size;
    char paymentId[512];
    size = sdkbox::PluginGameroom::purchaseGetPaymentID(payHandle, paymentId, 512);

    auto amount = sdkbox::PluginGameroom::purchaseGetAmount(payHandle);

    char currency[512];
    size = sdkbox::PluginGameroom::purchaseGetCurrency(payHandle, currency, 512);

    auto purchaseTime = sdkbox::PluginGameroom::purchaseGetPurchaseTime(payHandle);

    char productId[512];
    size = sdkbox::PluginGameroom::purchaseGetProductID(payHandle, productId, 512);

    char purchaseToken[512];
    size = sdkbox::PluginGameroom::purchaseGetPurchaseToken(payHandle, purchaseToken, 512);

    auto quantity = sdkbox::PluginGameroom::purchaseGetQuantity(payHandle);

    char requestId[512];
    size = sdkbox::PluginGameroom::purchaseGetRequestID(payHandle, requestId, 512);

    char status[512];
    size = sdkbox::PluginGameroom::purchaseGetStatus(payHandle, status, 512);

    char signedRequest[512];
    size = sdkbox::PluginGameroom::purchaseGetSignedRequest(payHandle, signedRequest, 512);

    auto errorCode = sdkbox::PluginGameroom::purchaseGetErrorCode(payHandle);

    char errorMessage[512];
    size = sdkbox::PluginGameroom::purchaseGetErrorMessage(payHandle, errorMessage, 512);

    ::CCLOG(
        "onPurchaseIAPMsg, Purchase Handle: %s\nAmount: %d\nCurrency: %s\nPurchase Time: %lld\n"
        "Product Id:%s\nPurchase Token: %s\nQuantity: %d\nRequest Id: %s\n"
        "Status: %s\nSignedRequest: %s\nError Code: %lld\nErrorMessage: %s\n",
        paymentId,
        (int)amount,
        currency,
        (long long)purchaseTime,
        productId,
        purchaseToken,
        (int)quantity,
        requestId,
        status,
        signedRequest,
        (long long)errorCode,
        errorMessage
    );
}
```

In addtion, you can use `hasLicense()` method to check whether the player has got the license or premium version.

```
sdkbox::PluginGameroom::hasLicense();
```

Please note that this checking operation will trigger a callback named `onHasLicenseMsg`. Bizarrely, you should get the license ID via the method `purchaseGetLicense()` in callback(Faceebook Gameroom SDK demands these behaviors).

```
void HelloWorld::onHasLicenseMsg(sdkbox::HasLicenseHandle hasLicenseHandle) {
    auto hasLicense = sdkbox::PluginGameroom::purchaseGetLicense(hasLicenseHandle);
    ::CCLOG(
            "onHasLicenseMsg, Has License: %llu",
            hasLicense
    );
}
```

### Send App Events

You can log app events for Facebook Analytics via the following functions:

```
auto formData = sdkbox::PluginGameroom::formDataCreateNew();
char key[sdkbox::FBG_BUFFER_SIZE]{"sdkbox_key"};
char value[sdkbox::FBG_BUFFER_SIZE]{"3.1415"};
sdkbox::PluginGameroom::formDataSet(formData, key, sdkbox::FBG_BUFFER_SIZE, value, sdkbox::FBG_BUFFER_SIZE);
sdkbox::PluginGameroom::logAppEvent("test_event", formData);

::CCLOG("Gameroom Send App Event with sum value");
sdkbox::PluginGameroom::logAppEventWithValueToSum("test_event", formData, 1024.2);
sdkbox::PluginGameroom::formDataDispose(formData);
```

The key-value pairs are carried in `FormData` structure. And if you intend to offer an extra value in an event, you should use `logAppEventWithValueToSum` method.

### Send App Requests

To invoke an app request within your game, you may use the following call to trigger the dialog:

```
sdkbox::PluginGameroom::appRequest(
    "hello world, try this gameroom sdk demo.",
    nullptr,
    nullptr,
    "faceboo_user_id_1,facebook_user_id_2",

    nullptr,
    nullptr,
    20,
    nullptr,
    "hello"
);
```

In common, you don't need to set the users' ID in order to let the player choose which friends he want to send the requests.

```
sdkbox::PluginGameroom::appRequest(
    "hello world, try this gameroom sdk demo.",
    nullptr,
    nullptr,
    nullptr,
    nullptr,
    nullptr,
    20,
    nullptr,
    "hello"
);
```

In the callback of sending app requests,  you can hanedle the result:

```
void HelloWorld::onAppRequestMsg(fbgAppRequestHandle appRequestHandle) {
    char objectID[sdkbox::FBG_BUFFER_SIZE];
    //auto size = sdkbox::PluginGameroom::appRequestGetRequestObjectID(appRequestHandle, objectID, sdkbox::FBG_BUFFER_SIZE);
    auto size = fbg_AppRequest_GetRequestObjectId(appRequestHandle, objectID, sdkbox::FBG_BUFFER_SIZE);
    ::CCLOG("onAppRequestMsg");
    ::CCLOG("size = %lu\n", size);  // return 0 here, indicating that appRequestHandle is invalid.

    char toUser[sdkbox::FBG_BUFFER_SIZE];
    size = sdkbox::PluginGameroom::appRequestGetTo(appRequestHandle, toUser, sdkbox::FBG_BUFFER_SIZE);
    ::CCLOG("size = %lu\n", size);

    ::CCLOG(
            "object id: %s, to user: %s",
            objectID,
            toUser
    );
}
```
