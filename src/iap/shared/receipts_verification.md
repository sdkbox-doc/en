
## IAP Receipts Verification
It's very important to check for the IAP receipts to avoid fraud. There are two options: __client-side verification__ and __server-side verification__. You can use either one or both. Using both will have the best result. 

### Client-Side Receipts Verfication

* Client-side purchase receipt validation information is exposed to the developer if the she calls the method IAP::enableUserSideVerification(true). This method makes the plugin to avoid receipt/key validation and delegates this process to the user by a call to the plugin listener’s `onPurchaseNeedsValidation( const std::string& json_with_product_and_ciphered_payload )` method. 
* Currently, the product on Android is auto-consumed, and iOS’ transaction finished by explicit calls to consume and finishTransaction respectively. This will force the developer to do a big chunk of extra work to keep track of transactions that have been unable to contact the validation server.
* Consumtion/finishTransaction should be exposed as explicit calls and allow developers to benefit from the per-platform built-in transaction-queues/non-consumed-products features.
* Making these calls explicit won’t break the current IAP flow since this would happen after user-side remote validation and would hence only affect users that want to have server-side validation on their own.
* In any case, currently, the result to a call to __onPurchaseNeedsValidation__ is not being stored in any place.

### Server-Side Receipts Verification
[Click here to learn more.](/liveops/receipt-verification)
