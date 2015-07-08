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
