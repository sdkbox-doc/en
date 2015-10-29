### Initialize Achievement
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAchievement:init();
sdkbox.IAP:init();
```

### Using Achievement
#### unlock achievement
```lua
sdkbox.PluginAchievement:unlock(achievementId)
```
