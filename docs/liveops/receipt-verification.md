<h1>LiveOps - Server-Side Receipt Verification</h1>

## Overview
In addition to the client-side receipt validation that you can do in the [SDKBOX IAP plugin](../plugins/iap), you can also optionally enable server-side validation provided by SDKBOX LiveOps. 

If enabled, whenever a purchase happens it will be automatically (and transparently) checked against Google or Apple servers for authenticity. Without any code change on the developers side, the purchase receipts will be safely authenticated. Same as the local validation, there are two public plugins interface methods: `onSuccess()` and `onFailure()`. They will be notified with the verification result. 

If the remote verification request fails, the system will automatically fallback to local receipt verification, for example, when timeout or networking errors when communicating with SDKBOX LiveOps. 

!!!note 
    It is important to note that this feature requires the app using the [Remote Configuration](./remote-config) with the IAP plugin. 


## Remote verification flow

### iOS
1. Player makes a purchase (pays for an item)
2. CompleteTransaction is called, and cyphered receipt info is obtained.
3. If developer requested to do receipt validation [App has remote config or not]:
    1. onPayResult is called with PaymentTransactionNeedsVerification set as code. The Product notified on plugin’s listener has cyphered payload info so the developer can launch his own purchase verification process.
    2. The purchase transaction is finished.
4. If developer did not request to do receipt validation:
    1. if Application does not have remote configuration enabled: 
        1. onPayResult is called with code: PaymentTransactionStatePurchased.
        2. The transaction is finished.
    2. if Application has remote configuration enabled: remote IAP validation, by calling checkAuthenticity method is started.This method does the remote verification of the purchase cyphered payload.
        1. A request to sdkbox.com server is sent for purchase payload verification.
	    1. If timeout or error in request: onPayResult is called with code: kPaySuccessAndValidationError. These are error situations with the validation server.
	    2. If request is aborted by user: onPayResult is called with code: kPaySuccessAndValidationError. (Same as before)
	    3. The verification request processed normally, and a Json response is gotten as a result:
	        1. Verification is not successful: onPayResult is called with code: kPaySuccessAndValidationNotAuthenticated.
		2. Verification is successful: onPayResult is called with code: kPaySuccessAndValidationAuthenticated.
        2. The transaction is always finished.

### Android IAP flow
1. Player makes a purchase request, and pays for it.
2. If the purchase is canceled, onPayResult is called with code PAYRESULT_CANCEL.
3. If the purchase is errored, onPayResult is called with code PAYRESULT_FAIL.
4. If the purchase is successful
    1. Receipt and cyphered payload info is obtained.
    2. If the developer requested to do receipt validation, onPayResult is called with PAYRESULT_NEEDS_VERIFICATION. The Product passed to the plugin listener has receipt and cyphered payload information, which is sufficient info to verify purchase authenticity.
    3. else
        1. If Application has not remote configuration set: local validation process is executed:
	    1. Application’s private key must be present in the sdkbox_config.json file.
	    2. If verification succeeds: onPayResult is called with code PAYRESULT_SUCCESS.
	    3. if verification fails: onPayResult is called with code PAYRESULT_FAIL.
	2. If Application has remote configuration set: a remote validation request is started.
	    1. If the validation request is errored or timeout (both situations refer to our server or network status), the verification process falls back to local verification [4.3.1]
	    2. If the validation request is is aborted, onPayResult is called with code PAYRESULT_FAIL.
	    3. If the validation request executes normally:
	        1. If validation is not successful, the verification process falls back to local verification [4.3.1]
		2. if validation is successful, onPayResult is called with code PAYRESULT_SUCCESS.
5. If the purchase is a Consumable item the purchase will always be consumed.


## Setup 

### For Android Play
* Make sure to enable [Remote Configuration](./remote-config) in your app.
* Create or select the configuration for Android, and add `Google Play IAP` plugin in __Essentials__. You need to fill-in the __Google Play__ developer console’s application private key. If the __private key__ is not supplied, the local verification will always notify `onFail()`.

### For Apple App Store
* TBD