## API Reference

### Methods
```cpp
static void init ( const char * jsonconfig = 0 ) ;
```
> Initialize SDKBox IAP

```cpp
static void setDebug ( bool debug ) ;
```
> Enable/disable debug logging

```cpp
static std::vector <Product> getProducts ( ) ;
```
> Get all the products

```cpp
static void purchase ( const std::string & name ) ;
```
> Make a purchase request

<pre>
@Param name is the name of the item specified in sdkbox_config.json
</pre>

```cpp
static void refresh ( ) ;
```
> Refresh the IAP data(title, price, description)

```cpp
static void restore ( ) ;
```
> Restore purchase

```cpp
static void setListener ( IAPListener * listener ) ;
```
> Set listener for IAP

```cpp
static void removeListener ( ) ;
```
> Remove listener for IAP

```cpp
static void enableUserSideVerification ( bool ) ;
```

```cpp
static bool isAutoFinishTransaction ( ) ;
```
> get auto invoke finishTransaction flag

```cpp
static void setAutoFinishTransaction ( bool b ) ;
```
> set auto invoke finishTransaction flag

```cpp
static void finishTransaction ( const std::string productid ) ;
```
> to invoke ios finishTransaction api

```cpp
static void fetchStorePromotionOrder ( ) ;
```

```cpp
static void updateStorePromotionOrder ( const std::vector <std::string> & productNames ) ;
```

```cpp
static void fetchStorePromotionVisibility ( const std::string & productName ) ;
```

```cpp
static void updateStorePromotionVisibility ( const std::string & productName ,
                                             bool visibility ) ;
```

```cpp
static void getPurchaseHistory();
```
> get all purchase history, include cancelled, expired

```cpp
static void getInitializedErrMsg();
```
> get initialized error message

```cpp
static void requestUpdateTransaction();
```
> request all unfinish transaction, and retrigger onSuccess, onFailed or onCancel event with corresponding transaction.
>
> just valid on iOS
>
> e.g. if there have two transaction (one is success, on is canceled) havn't been finish,
>      after invoke requestUpdateTransaction, onSuccess will trigger with the success transaction, onCancelled will trigger with the cancelled transaction.
>
> Note: for most developer, this api is needn't, onSuccess, onFailed or onCancel will auto trigger when transaction updated.
>


### Listeners
```cpp
void onInitialized ( bool success );
```
> Called when IAP initialized

```cpp
void onSuccess ( const Product & p );
```
> Called when an IAP processed successfully

```cpp
void onFailure ( const Product & p , const std::string & msg );
```
> Called when an IAP fails

```cpp
void onCanceled ( const Product & p );
```
> Called when user canceled the IAP

```cpp
void onRestored ( const Product & p );
```
> Called when server returns the IAP items user already purchased
@note this callback will be called multiple times if there are multiple IAP

```cpp
void onProductRequestSuccess ( const std::vector <Product> & products );
```
> Called the product request is successful, usually developers use product request to update the latest info(title, price) from IAP

```cpp
void onProductRequestFailure ( const std::string & msg );
```
> Called when the product request fails

```cpp
void onRestoreComplete ( bool ok , const std::string & msg );
```
> Called when the restore completed

```cpp
bool onShouldAddStorePayment ( const std::string & productName ) 
```

```cpp
void onFetchStorePromotionOrder ( const std::vector <std::string> & productNames ,
                                  const std::string & error ) 
```

```cpp
void onFetchStorePromotionVisibility ( const std::string productName ,
                                       bool visibility ,
                                       const std::string & error ) 
```

```cpp
void onUpdateStorePromotionOrder ( const std::string & error ) 
```

```cpp
void onUpdateStorePromotionVisibility ( const std::string & error ) 
```

```cpp
void onPurchaseHistory(const std::string& purchases) 
```

```cpp
void onConsumed(const Product& p, const std::string& error) 
```

```cpp
void onDeferred(const Product& p) 
```
> Called when IAP pay deferred
>
> Note: Pay deferred status is a middle status, for most developer, needn't case this status
> this status will change to success or failed or cancel, its final status is pending external action.
>
> Please DO NOT finishTransaction when status is deferred.

