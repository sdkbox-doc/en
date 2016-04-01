### Initialize Appnext
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAppnext:init()
```

### cache ad/video

```cpp
sdkbox.PluginAppnext:cacheAd("default")
sdkbox.PluginAppnext:cacheVideo("fullscreen")
```
**NOTE** : Appnext ads needs to be cached before use, auto-caching is not available with this plugin. It might take couple of minutes to cache ads, once cached you would be able to see the ads. While caching, ads are not available.


### refresh ad/video

```
sdkbox.PluginAppnext:refreshAds()
sdkbox.PluginAppnext:refreshVideo("fullscreen")
```
**NOTE** : refresh ad or video after it is closed.


### show ad/video
```cpp
sdkbox.PluginAppnext:showAd("default")
sdkbox.PluginAppnext:showVideo("fullscreen")
```

### hide ad
```cpp
sdkbox.PluginAppnext:hideAd()
```

### check ad/video available
```cpp
sdkbox.PluginAppnext:isAdReady()
sdkbox.PluginAppnext:isVideoReady("fullscreen")
```

### Implement AppnextListner
* You can implement AppnextListener if you want to receive callbacks like video finish playing.
```lua

sdkbox.PluginAppnext.setListener(function(args)
    local event = args.event
    if "onAdError" == event then
    elif "onAdLoaded" == event then
    elif "onAdOpened" == event then -- not support on android
    elif "onAdClosed" == event then
    elif "onAdClicked" == event then

    elif "onVideoLoaded" == event then  -- not support on ios
    elif "onVideoClicked" == event then -- not support on ios
    elif "onVideoClosed" == event then  -- not support on ios
    elif "onVideoEnded" == event then   -- not support on ios
    elif "onVideoError" == event then   -- not support on ios
    end
end)

```
