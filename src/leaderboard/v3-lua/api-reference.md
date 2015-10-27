## API Reference

### Methods
```lua
sdkbox.PluginLeaderboard:init()
```
> Initialize SDKBox Leaderboard

```lua
sdkbox.PluginLeaderboard:setListener(listener)
```
> Set listener for Leaderboard

```lua
sdkbox.PluginLeaderboard:getListener()
```
> Get listener of Leaderboard

```lua
sdkbox.PluginLeaderboard:removeListener()
```
> Remove listener for Leaderboard

```lua
sdkbox.PluginLeaderboard:submitScore(leaderboardId, score)
```

```lua
sdkbox.PluginLeaderboard:getLeaderboard(leaderboardId)
```


### Listeners
```lua
onComplete(leaderboard)
```

```lua
onFail()
```


