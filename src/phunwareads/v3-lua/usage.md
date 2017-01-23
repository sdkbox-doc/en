### Initialize PhunwareAds
* Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginPhunwareAds:init()
```

### Showing Ads
Display an ad where ever you want from your code:
```lua
// To use customized location
sdkbox.PluginPhunwareAds:show("your_ad_name")
```

### Cache Ads
```lua
sdkbox.PluginPhunwareAds:cache("your_ad_name")
```

### Hide Ads
```lua
sdkbox.PluginPhunwareAds:hide("your_ad_name")
```

### Catch PhunwareAds events (optional)
This allows you to catch the `PhunwareAds` events so that you can perform operations such as providing player rewards for viewing ads.

* Create a listener (demonstrated by logging events):
```lua
sdkbox.PluginPhunwareAds:setListener(function(args)

    if "adLoaded" = args.event then
        print(args.event, args.name)
    elseif adFailed" = args.event then
        print(args.event, args.errorCode, args.msg)
    elseif adWillPresent" = args.event then
        print(args.event, args.name)
    elseif adDidPresent" = args.event then
        print(args.event, args.name)
    elseif adWillDissmiss" = args.event then
        print(args.event, args.name)
    elseif adDidDismiss" = args.event then
        print(args.event, args.name)
    elseif willLeaveApp" = args.event then
        print(args.event, args.name)
    elseif reward" = args.event then
        print(args.event, args.name, args.amount, args.currency)
    end

end)
```
