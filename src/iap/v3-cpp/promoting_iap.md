
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

more detail [Promoting IAP official Document](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html)

### Testing Promoted In-App Purchases

To test your promoted in-app purchases before your app is available in the App Store, you can use follow URL:

```
itms-services://?action=purchaseIntent&bundleId=com.Sdkbox.SdkboxIAPSample&productIdentifier=com.cocos2dx.non1
```

replace `com.Sdkbox.SdkboxIAPSample` and `com.cocos2dx.non1` with your application info.

and then send this URL to yourself in an email or iMessage and open it from your device. You will know the test is running when your app opens automatically. You can then test your promoted in-app purchase.

