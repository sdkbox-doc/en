### Initialize AdColony
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAdColony:init()
```

### Showing Ads
Display an ad wherever you want from your code, by specifying ad type:
```lua
sdkbox.PluginAdColony:show("video")
```
or:
```lua
sdkbox.PluginAdColony:show("v4vc")
```

### Catch AdColony events (optional)
This allows you to catch the `AdColony` events so that you can perform operations such as providing player rewards for watching the video.

* Create a listener (demonstrated by logging events):
```lua
sdkbox.PluginAdColony:setListener(function(args)
    if args.name == "onAdColonyChange" or args.name == "onAdColonyReward" or args.name == "onAdColonyStarted" or args.name == "onAdColonyFinished" then
        print("those four event is deprecated")
        return
    end

    dump(args)
    if "adColonyReward" ==  args.name then
    elseif "adColonyInterstitialDidLoad" ==  args.name then
    elseif "adColonyInterstitialDidFailToLoad" ==  args.name then
    elseif "adColonyAdViewDidLoad" ==  args.name then
    elseif "adColonyAdViewDidFailToLoad" ==  args.name then
    end
end)
```
