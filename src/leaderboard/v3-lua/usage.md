### Initialize Leaderboard
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginLeaderboard:init();
sdkbox.IAP:init();
```

### Using Leaderboard
#### Submit score
```lua
sdkbox.PluginLeaderboard:submitScore(leaderboardId, score);
```

#### Get current score
```lua
sdkbox.PluginLeaderboard:getLeaderboard(leaderboardId);
```

### Leaderboard events
This allows you to catch `Leaderboard` events so that you can perform operations after Leaderboard events have occurred.

```lua
sdkbox.PluginLeaderboard:setListener(function(args)
    dump(args)
    if args.name == "onComplete" then
    elseif args.name == "onFail" then
    end
end)
```
