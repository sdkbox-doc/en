### Initialize SignInWithApple
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSignInWithApple:init()
```

### Login

Sign in with Apple

```lua
sdkbox.PluginSignInWithApple:sign();
```

if user have login before, you can invoke following when app init:

```lua
sdkbox.PluginSignInWithApple:signWithExistingAccount();
```


### Handling SignInWithApple Events
This allows you to catch the `SignInWithApple` events so that you can perform operations based upon the response from your players and SignInWithApple servers.

```lua
sdkbox.PluginSignInWithApple:setListener(function(args)
    if "onAuthorizationDidComplete" == args.event then
        -- authorization success
        dump(args, "onAuthorizationDidComplete:")
    else if "onAuthorizationCompleteWithError" == args.event then
        -- authorization fail
        dump(args, "onAuthorizationCompleteWithError:")
    else if "onAuthorizationStatus" == args.event then
        -- authorization status
        dump(args, "onAuthorizationStatus:")
    else
        print("unknow event ", args.event)
    end
end)
```
