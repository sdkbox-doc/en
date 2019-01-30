## Thrid Server Authenticate

### iOS

1. implement `onGenerateIdentityVerificationSignature` function in `SdkboxPlayListener`
2. invoke `sdkbox::PluginSdkboxPlay::generateIdentityVerificationSignature();`

### Android

* add `web_client_id` to `sdkbox_config.json`
```json
    "sdkboxplay" : {
        "web_client_id": "......."
    }
```
* sign
* `sdkbox::PluginSdkboxPlay::getPlayerAccountField("server_auth_code")` to get google server auth code

