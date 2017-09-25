Although you can use these methods anywhere, some methods need Gameroom `handle` object in practice. So this document distinguishes the common `Methods` and the `Methods in Listener Callbacks`.

### Methods

```
static int init(const char* appID);
```

>   Initialize the Gameroom Plugin. `appID` is your Facebook Application ID. The method will return 0 if the plugin is Initialized successfully.

```
static std::string login();
```

>   Player login. It will return a string representing `GameroomReq`.

```
static std::string loginWithScopes(uint32_t scopeCount, const std::vector<std::string>& loginScopes);
```

>   Player login with some permissions. `scopeCount` is the total of the permissions. `loginScopes` is a vector which can include these values: `public_profile`, `email`, `user_friends` and `publish_actions`. The method will return a string representing `GameroomReq`.

```
static bool isLoggedIn();
```

>   Check whether the player has logged in.

```
static std::string feedShare(
    const char* toId,
    const char* link,
    const char* linkName,
    const char* linkCaption,
    const char* linkDescription,
    const char* pictureLink,
    const char* mediaSource
);
```

>   Share to Facebook. The meaning of each parameters is as its name. The method will return a string representing `GameroomReq`.

```
static std::string purchaseIAP(
    const char* product,
    uint32_t quantity,
    uint32_t quantityMin,
    uint32_t quantityMax,
    const char* requestId,
    const char* pricePointId,
    const char* testCurrency
);
```

>   Purchase a product with a prouduct ID. `quantity` is the number of product, `quantityMin` is the minimum number of quantity of product, `quantityMax` is the maximum of quantity of product. For other parameters, you can refer to [Facebook Gameroom SDK](https://developers.facebook.com/docs/games/gameroom/sdk) and [SDKBOX Gameroom Plugin Sample](https://github.com/sdkbox/sdkbox-sample-gameroom). The method will return a string representing `GameroomReq`.

```
static std::string purchaseIAPWithProductURL(
    const char* product,
    uint32_t quantity,
    uint32_t quantityMin,
    uint32_t quantityMax,
    const char* requestId,
    const char* pricePointId,
    const char* testCurrency
);
```

>   Purchase a product with a prouduct url link. `quantity` is the number of product, `quantityMin` is the minimum number of quantity of product, `quantityMax` is the maximum of quantity of product. For other parameters, you can refer to [Facebook Gameroom SDK](https://developers.facebook.com/docs/games/gameroom/sdk). The method will return a string representing `GameroomReq`.

```
static std::string payPremium();
```

>   Purchase a premium version or license. It will return a string representing `GameroomReq`.

```
static std::string hasLicense();
```

>   Check whether the player has license or premium version. The method will return a string representing `GameroomReq`.

```
static std::string logAppEvent(const char* eventName, const FormDataHandle formData);
```

>   Send an event to Facebook Analytics. `FormDataHandle` is created and set by other APIs. The method will return a string representing `GameroomReq`.

```
static std::string logAppEventWithValueToSum(const char* eventName, const FormDataHandle formData, float valueToSum);
```

>   Send an event to Facebook Analytics with an extra value `valueToSum`. `FormDataHandle` is created and set by other APIs. The method will return a string representing `GameroomReq`.

```
static const FormDataHandle formDataCreateNew();
```

>   Create a `FormDataHandle` object to store key-value pairs in an app event.

```
static void formDataSet(
    const FormDataHandle obj,
    char *fieldNameBuffer,
    size_t fieldNameBufferLen,
    char *valueBuffer,
    size_t valueBufferLen
);
```

>   Store a key-value pair into `FormDataHandle` object.

```
static size_t formDataGet(
    const FormDataHandle obj,
    char *fieldNameBuffer,
    size_t fieldNameBufferLen,
    char *valueBuffer,
    size_t valueBufferLen
);
```

>   Get a key-value pair from `FormDataHandle` object.

```
static void formDataDelete(const FormDataHandle obj, char *fieldNameBuffer, size_t fieldNameBufferLen);
```

>   Delete a key-value pair from `FormDataHandle` object.

```
static bool formDataHas(const FormDataHandle obj, char* fieldNameBuffer, size_t fieldNameBufferLen);
```

>   Check whether the `FormDataHandle` object has a specified key-value pair.

```
static void formDataDispose(const FormDataHandle obj);
```

>   Destory `FormDataHandle` object.

```
static std::string appRequest(
    const char* message,
    const char* actionType,
    const char* objectID,
    const char* to,
    const char* filters,
    const char* excludeIDs,
    uint32_t maxRecipients,
    const char* data,
    const char* title
);
```

>   Send an app request to some users. if parameter `to` is `nullptr`, this method will let player to choose which users he want to send the request. For other parameters, please refer to [Facebook Game Service Requests](https://developers.facebook.com/docs/games/services/gamerequests) and [SDKBOX Gameroom Plugin Sample](https://github.com/sdkbox/sdkbox-sample-gameroom). The method will return a string representing `GameroomReq`.

### Listener Callbacks

```
virtual void onLoginAccessTokenMsg(sdkbox::AccessTokenHandle);
```
>   Triggered by `login()` or `loginWithScopes()`.

```
virtual void onFeedShareMsg(sdkbox::FeedShareHandle);
```

>   Triggered by `feedShare()`.

```
virtual void onPurchaseIAPMsg(sdkbox::PurchaseHandle);
```

>   Triggered by `purchaseIAP()`, `purchaseIAPWithProductURL()` or `payPremium()`.

```
virtual void onHasLicenseMsg(sdkbox::HasLicenseHandle);
```

>   Triggered by `hasLicense()`.

```
virtual void onAppRequestMsg(sdkbox::AppRequestHandle);
```

>   Triggered by `appRequest()`.

```
static int setListener(GameroomListener *);
```

>   Set a pointer to listener object.

```
static GameroomListener* removeListener();
```

>   Delete current listener object, return the pointer to it.

```
static GameroomListener* listener();
```

>   Return the pointer to current listener object.

### Methods in Listener Callbacks

####  These methods can be called in `onLoginAccessTokenMsg` to get some information from the `AccessTokenHandle` object.

```
static bool accessTokenIsValid(AccessTokenHandle obj);
```

>   Check the access token is valid.

```
static FacebookID accessTokenGetUserID(AccessTokenHandle obj);
```

>   Get the Facebook User ID.

```
static size_t accessTokenGetTokenString(AccessTokenHandle obj, char* buffer, size_t bufferLen);
```

>   Get the access token string.

```
static uint64_t accessTokenGetExpirationTimestamp(AccessTokenHandle obj);
```

>   Get the expired time of access Token.

```
static size_t accessTokenGetPermissions(AccessTokenHandle obj, LoginScope* buffer, size_t bufferLen);
```

>   Get the applied permissions.

```
static const char* loginScopeToString(LoginScope loginScope);
```

>   Get the string name of applied permission.

#### This method can be called in `onFeedShareMsg` to get the post ID.

```
static FacebookID feedShareGetPostID(FeedShareHandle obj);
```

>   Get the post ID.

####  These methods can be called in `onPurchaseIAPMsg` to get some information from the `PurchaseHandle` object.

```
static size_t purchaseGetPaymentID(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the payment ID.


```
static uint32_t purchaseGetAmount(PurchaseHandle obj);
```

>   Get the of purchasing.

```
static size_t purchaseGetCurrency(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the currency of purchasing.

```
static uint64_t purchaseGetPurchaseTime(PurchaseHandle obj);
```

>   Get the time of purchasing.

```
static size_t purchaseGetProductID(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the product ID.

```
static size_t purchaseGetPurchaseToken(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the token of purchasing.


```
static uint32_t purchaseGetQuantity(PurchaseHandle obj);
```

>   Get the quantity of purchasing.

```
static size_t purchaseGetRequestID(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the request ID of purchasing.

```
static size_t purchaseGetStatus(PurchaseHandle obj, char* buffer, size_t bufferLen);

```

>   Get the status of purchasing.

```
static size_t purchaseGetSignedRequest(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the signed request.

```
static uint64_t purchaseGetErrorCode(PurchaseHandle obj);
```

>   Get the error code of purchasing.

```
static size_t purchaseGetErrorMessage(PurchaseHandle obj, char* buffer, size_t bufferLen);
```

>   Get the error message of purchasing.

#### This method can be called on `onHasLicenseMsg` to get license ID.

```
static FacebookID purchaseGetLicense(HasLicenseHandle obj);
```

>   Get the license ID.

#### This methods can be called on `onAppRequestMsg` to get some information of app request.

```
static size_t appRequestGetRequestObjectID(const AppRequestHandle obj, char *buffer, size_t bufferLen);
```

>   Get the request ID of app request.


```
static size_t appRequestGetTo(const AppRequestHandle obj, char *buffer, size_t bufferLen);
```

>   Get the receivers of app request.


