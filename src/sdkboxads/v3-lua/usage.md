### Initialize SdkboxAds
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSdkboxAds:init();
```

### Using SdkboxAds

To request a default Ad for the default AdUnit and have a fast integration test:
```javascript
sdkbox.SdkboxAds:play()
```

To request Ads in the Default AdUnit:
```lua
sdkbox.SdkboxAds:play( zone_place_location, params );

// params is an object with string keys and values.
```
> Note: the params are defined per AdUnit, and should be checked in each AdUnit's documentation.

To request Ads for an specific AdUnit:
```lua
sdkbox.SdkboxAds:play( ad_unit_name, zone_place_location, params );
```

To request ads for a placement defined in the sdkbox_config.json file:
```lua
sdkbox.SdkboxAds:placement( placement_name );
```

To have fine grained cache control (for AdUnits that expose it):
```lua
sdkbox.SdkboxAds:cacheControl( ad_unit, cacheOpts );

// cacheOpts is an object with keys and values as strings. 
```
> Cache options are AdUnit specific and must be checked in each AdUnit's documentation.

### SdkboxAds events
This allows you to catch `SdkboxAds` events.

```lua
sdkbox.PluginSdkboxAds:setListener(function(args)
    if "onAdAction" == args.name then
        local ad_unit_id = args.ad_unit_id;
        local ad_name = args.ad_name;
        local ad_action_type = args.ad_action_type;
    elseif "onRewardAction" ==  args.name then
        local ad_unit_id = args.ad_unit_id;
        local ad_name = args.ad_name;
        local reward_amount = args.reward_amount;
        local reward_success = args.reward_success;
    end
end)
```
