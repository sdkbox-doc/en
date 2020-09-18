[&#8249; SignInWithApple Doc Home](./)

<h1>Sign in with Apple Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

## Integration
Open a terminal and use the following command to install the SDKBOX SignInWithApple plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import signinwithapple
```

<<[../../shared/notice.md]

## Extra steps

Add `Sign In with Apple` Capability in Xcode. path: `Xcode` -> `Signing & Capabilities` -> `+Capability` -> `Sign In with Apple`.

## Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app.

Here is an example of the SignInWithApple configuration.

```json
"ios" :
{
    "SignInWithApple":{
    }
},
"android":
{
    "SignInWithApple":{
    }
}
```

### SignInWithApple for Android

-   SignInWithApple is not supported Android, we implement empty on Android.

##Usage
<<[usage.md]

<<[../../shared/remote_application_config.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]


