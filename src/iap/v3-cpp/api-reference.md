## API Reference

### Methods
```cpp
static void init ( ) ;
```
> Initialize SDKBox IAP

```cpp
static void setDebug ( bool debug ) ;
```
> Enable/disable debug logging

```cpp
static void purchase ( const std::string & name ) ;
```
> Make a purchase request

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


### Listeners
```cpp
void onInitialized ( bool ok );
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


