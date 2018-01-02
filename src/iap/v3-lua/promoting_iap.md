
## Promotion IAP

### Enable Promotion IAP

if you want to use iOS promotion iap

1. implement `onShouldAddStorePayment` of `IAPListener` class.
2. configure `itunes connect`

we return true by default in `onShouldAddStorePayment`. this will not cancel or defer user's purchase action.

### Promotion IAP Setting

You can also customize which promoted in-app purchases a user sees on a specific device with follow api:

1. `sdkbox.IAP.updateStorePromotionOrder({"remove_ads"})`;
2. `sdkbox.IAP.updateStorePromotionVisibility('remove_ads', true)`;
3. `sdkbox.IAP.fetchStorePromotionOrder()`;
4. `sdkbox.IAP.fetchStorePromotionVisibility('remove_ads')`;

more detail[Promoting IAP official Document](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html)
