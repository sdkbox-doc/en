### Initialize AdMob
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAdMob:init()
```

### cache ad
```lua
sdkbox.PluginAdMob:cache("home")
sdkbox.PluginAdMob:cache("gameover")
```

### show ad
```lua
sdkbox.PluginAdMob:show("home")
sdkbox.PluginAdMob:show("gameover")
```

### hide ad
You can not hide an interstitial ad
```lua
sdkbox.PluginAdMob:hide("home")
```

### check ad available
```lua
sdkbox.PluginAdMob:isAvailable("home")
sdkbox.PluginAdMob:isAvailable("gameover")
```

### Implement AdMobListner
* You can implement AdMobListener if you want to receive callbacks like video finish playing.
```lua

sdkbox.PluginAdMob.setListener(function(args)
    local event = args.event
    if "adViewDidReceiveAd" == event then
    elif "adViewDidFailToReceiveAdWithError" == event then
    elif "adViewWillPresentScreen" == event then
    elif "adViewDidDismissScreen" == event then
    elif "adViewWillDismissScreen" == event then
    elif "adViewWillLeaveApplication" == event then
    elif "reward" == event then
    end
end)

```
