
## IAP Receipts Verification
If you're using remote configration for SDKBOX IAP Receipts verification is turn on by default [Click here to learn more.](/liveops/receipt-verification).

### Implement your own verification
You can get the receipt data and verify it with your own server by calling following method
```
sdkbox::IAP::enableUserSideVerification(true);
```
And then you should be able to access iap receipts using the following fields
```
product.receipt;
product.receiptCipheredPayload;
```
>Note: iOS don't provide purchase receipt, only ciphered payload

