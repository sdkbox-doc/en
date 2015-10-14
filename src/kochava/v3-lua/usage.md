### Initialize Kochava
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginKochava:init()
```

### Tracking Events
Kochava provides tracking __custom__, __spatial__ or __referral__ events.

* Tracking a __custom__ event:
```lua
sdkbox.PluginKochava:trackEvent("<EVENT>", "<VALUE>")
```

* Tracking a __spatial__ event, by providing a title and position in the world:
```lua
sdkbox.PluginKochava:spatialEvent("<TITLE>", <X>, <Y>, <Z>)
```

* Tracking a __referral__ event (also known as a deep link):
```lua
sdkbox.PluginKochava:sendDeepLink("<URI>", "<YOUR APP>")
```
 __Note:__ On Android, the 2nd parameter (__<YOUR APP>__) is not used. You just need to pass the __<URI>__.
