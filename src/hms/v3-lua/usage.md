### Initialize HMS
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.HMS:init()
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```lua
sdkbox.HMS:login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```lua
sdkbox.HMS:login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```lua
sdkbox.HMS:login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```lua
sdkbox.HMS:logout();
```

### Handling Purchase Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.
```lua
sdkbox.HMS:setListener(function(args)
        if "onLogin" == args.event then
                local code = args.code
                local msg = args.msg
                dump(args, "onLogin:")
        else
                print("unknown event ", args.event)
        end
end)
```
