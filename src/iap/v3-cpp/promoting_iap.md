
## Promotion IAP

### Enable Promotion IAP

if you want to use iOS promotion iap

1. implement `onShouldAddStorePayment` of `IAPListener` class.
2. configure `itunes connect`

we return true by default in `onShouldAddStorePayment`. this will not cancel or defer user's purchase action.

### Promotion IAP Setting

You can also customize which promoted in-app purchases a user sees on a specific device with follow api:

1. `static void updateStorePromotionOrder(const std::vector<std::string>& productNames)`;
2. `static void updateStorePromotionVisibility(const std::string& productName, bool visibility)`;
3. `static void fetchStorePromotionOrder()`;
4. `static void fetchStorePromotionVisibility(const std::string& productName)`;

more detail[Promoting IAP official Document](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html)
