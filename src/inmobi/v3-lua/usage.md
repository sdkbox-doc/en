### Initialize InMobi
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginInMobi:init()
```

### Show interstitial
After initialization you can begin to use the InMobi functionality:
```lua
local plugin = sdkbox.PluginInMobi
plugin:setListener(function(args)
    local event = args.event
    dump(args, "inmobi listener info:")
end)
plugin:init()

-- Manually Loading Ads
-- plugin:loadInterstitial();

-- show intestitial
if plugin:isInterstitialReady() then
    print('inmobi interstitial ad is ready');
    plugin:showInterstitial();
else
    print('inmobi interstitial ad is not ready');
end
```

### Set Log level
You can set log level with follow function
```
plugin:setLogLevel(sdkbox.PluginInMobi.SBIMSDKLogLevel.kIMSDKLogLevelDebug);
```

### Set user data
You can use following functions to set user data
```
-- setting if need
print("inmobi plugin version:" .. plugin:getVersion());
plugin:setLogLevel(sdkbox.PluginInMobi.SBIMSDKLogLevel.kIMSDKLogLevelDebug);
plugin:addIdForType("test", sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
plugin:removeIdType(sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
plugin:setAge(18);
plugin:setAreaCode("area code");
plugin:setAgeGroup(sdkbox.PluginInMobi.SBIMSDKAgeGroup.kIMSDKAgeGroupBetween18And20);
plugin:setYearOfBirth(1989);
plugin:setEducation(sdkbox.PluginInMobi.SBIMSDKEducation.kIMSDKEducationHighSchoolOrLess);
plugin:setEthnicity(sdkbox.PluginInMobi.SBIMSDKEthnicity.kIMSDKEthnicityHispanic);
plugin:setGender(sdkbox.PluginInMobi.SBIMSDKGender.kIMSDKGenderMale);
plugin:setHouseholdIncome(sdkbox.PluginInMobi.SBIMSDKHouseholdIncome.kIMSDKHouseholdIncomeBelow5kUSD);
plugin:setIncome(4500);
plugin:setInterests("game");
plugin:setLanguage("zh-cn");
plugin:setLocation("cd", "sc", "usa");
plugin:setLocation(102, 348);
plugin:setNationality("nationality");
plugin:setPostalCode("618000");
```

### Catch InMobi events (optional)
This allows you to catch the `InMobi` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginInMobi
plugin:setListener(function(args)
    local event = args.event -- event same with function name of InMobiListener
    dump(args, "inmobi listener info:")
end)
plugin:init()
```
