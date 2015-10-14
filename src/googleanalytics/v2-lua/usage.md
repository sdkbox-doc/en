### Initialize Google Analytics
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginGoogleAnalytics:init()
```

You can always manually stop recording events at any time by calling:
```cpp
sdkbox.PluginGoogleAnalytics:stopSession();
```

However, in-order to record events again you must then manually call:
```cpp
sdkbox.PluginGoogleAnalytics:startSession();
```

Logged data usually shows up within one day.
