### Initialize Achievement
Before initializing achievements for Playphone:
  - Register as a Playphone developer in the [Playphone Developer Portal](http://developer.playphone.com)
  - Create a new game and setup achievements for that game in the [Playphone
   Developer Portal](https://developer.playphone.com/games).
  - Setup Playphone configuration by following the JSON Configuration step as outlined in [Playphone plugin documentation](http://sdkbox- staging.github.io/en/plugins/playphone/v3 -cpp/#extra-steps)

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
