### Initialize LeadBolt
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginLeadBolt:init()
```

### Cache Ad
>NOTE: Leadbolt ads are cached before use for better user experience. Please allow time for ads to be cached.  Once an ad is cached, you will be able to see the ad. While caching is in progress, ads are not available for display.
```lua
sdkbox.PluginLeadbolt:loadModuleToCache("directdeal");
sdkbox.PluginLeadbolt:loadModuleToCache("rewardedvideo");
```

### Load/Display Ad
```lua
sdkbox.PluginLeadbolt:loadModule("directdeal");
sdkbox.PluginLeadbolt:loadModule("rewardedvideo");
```

### Check if Ad is available
```lua
if plugin:isAdReady('directdeal') then
    plugin:loadModule('directdeal')
else
    print('leadbolt ad is not ready')
end
```

### Catch LeadBolt events (optional)
This allows you to catch the LeadBolt ad events so that you can perform operations based upon responses. With rewarded video, the onMediaFinished event allows you to reward players for watching the video.
```lua
sdkbox.PluginLeadBolt:setListener(function(args)
	local event = args.event
	if "onModuleLoaded" == event then
	elif "onModuleClosed" == event then
	elif "onModuleClicked" == event then
	elif "onModuleCached" == event then
	elif "onModuleFailed" == event then
	elif "onMediaFinished" == event then
	end
end)
```
