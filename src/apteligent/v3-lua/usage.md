### Initialize Apteligent
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginApteligent:init()
```

### Logging Breadcrumbs

```lua
-- leave a breadcrumb
sdkbox.PluginApteligent:addFilter("www.gmail.com")

-- perform all breadcrumb writes on a background thread
sdkbox.PluginApteligent:setAsyncBreadcrumbMode(true)
```


### Logging User Metadata

```lua
-- Adding a Username
sdkbox.PluginApteligent:setUsername("MrsCritter")

-- Adding Arbitrary User Metadata
sdkbox.PluginApteligent:setValueforKey("5", "Game Level")
```


### Logging Userflows
```lua
-- Beginning a Userflow
sdkbox.PluginApteligent:beginUserflow("login")

-- Ending a Userflow
sdkbox.PluginApteligent:endUserflow("login")

-- Failing a Userflow
sdkbox.PluginApteligent:failUserflow("login")

-- Cancelling a Userflow
sdkbox.PluginApteligent:cancelUserflow("login")
```

### Modifying the Value of a Userflow
```lua
int valueInCents = sdkbox.PluginApteligent:valueForUserflow("my_userflow")
valueInCents += 5
sdkbox.PluginApteligent:setValueforUserflow(valueInCents, "my_userflow")

```

### Logging Network Requests
```lua
sdkbox.PluginApteligent:logNetworkRequest("GET", "http://www.abc123def456.com", 2.0, 1000, 100, 200)
```


### Filtering Captured Data
```lua
sdkbox.PluginApteligent:addFilter("www.gmail.com")
```

### Configuring Location
```lua
-- Beijing, China
sdkbox.PluginApteligent:updateLocation(39.9042, 116.4074)
```

### Other Tasks
```lua
-- Allowing Users to Opt Out of Crittercism
sdkbox.PluginApteligent:setOptOutStatus(true)

-- Changing the verbosity of Crittercism’s Logs
sdkbox.PluginApteligent:setLoggingLevel(sdkbox.CRLoggingLevelInfo) -- CRLoggingLevelSilent / CRLoggingLevelError / CRLoggingLevelWarning

-- Send App Load Data
-- You must set `"delay_sending_appload":true` in `sdkbox_config.json` first
sdkbox.PluginApteligent:sendAppLoadData()
```

### Implement ApteligentListner
* You can implement ApteligentListener if you want to receive callbacks like video finish playing.
```lua

sdkbox.PluginApteligent.setListener(function(args)
    local event = args.event
    if "onCrashOnLastLoad" == event then -- not support on android
    end
end)

```
