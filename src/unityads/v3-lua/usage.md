### Initialize UnityAds
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginUnityAds:init()
```

### Show interstitial
After initialization you can begin to use the UnityAds functionality:
```lua
local placement = ""
if (sdkbox.PluginUnityAds:isReady(placement)) then
    sdkbox.PluginUnityAds:show(placement)
else
    printf("unityads ad is not ready")
end
```

### Catch UnityAds events (optional)
This allows you to catch the `UnityAds` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginUnityAds
plugin:setListener(function(args)
    local event = args.event -- event same with function name of UnityAdsListener
    dump(args, "unityads listener info:")
end)
plugin:init()
```
