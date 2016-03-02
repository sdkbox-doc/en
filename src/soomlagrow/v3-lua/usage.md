### Initialize SoomlaGrow
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSoomlaGrow:init()
```

### Using GROW's Insights module
After initialization you can begin to use the Insights functionality. Use `refreshInsight`, `getUserInsightInfo` wherever you want from your code:
```lua
sdkbox.PluginSoomlaGrow:payRank(sdkbox.PluginSoomlaGrow.EGenre.Word)
sdkbox.PluginSoomlaGrow:purchaseLikelihood(sdkbox.PluginSoomlaGrow.EDayQuarter._12am_6am)

sdkbox.PluginSoomlaGrow:refreshInsight()
sdkbox.PluginSoomlaGrow:getUserInsightInfo()
```

all value of `sdkbox.PluginSoomlaGrow.EGenre`
```lua
sdkbox.PluginSoomlaGrow.EGenre = {
    Action=0,
    Adventure=1,
    Arcade=2,
    Board=3,
    Card=4,
    Casino=5,
    Casual=6,
    Educational=7,
    Family=8,
    Music=9,
    Puzzle=10,
    Racing=11,
    Role_Playing=12,
    Simulation=13,
    Sports=14,
    Strategy=15,
    Trivia=16,
    Word=17
}
```

all value of `sdkbox.PluginSoomlaGrow.EDayQuarter`
```lua
sdkbox.PluginSoomlaGrow.EDayQuarter = {
    _12am_6am=0,
    _6am_12pm=1,
    _12pm_6pm=2,
    _6pm_12am=3
}
```

### Catch GROW events (optional)
This allows you to catch the `SOOMLA Grow` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginSoomlaGrow:setListener(function(data)
            if "onGrowInitialized" == data.event then
                //highway initialized
            elseif "onGrowConnected" == data.event then
                //highway connected
            elseif "onGrowDisconnected" == data.event then
                //highway disconnected
            elseif "onGrowInsightsInitialized" == data.event then
                //soomla grow insight initialized
            elseif "onInsightsRefreshFailed" == data.event then
                //soomla grow insight refresh failed
            elseif "onInsightsRefreshFinished" == data.event then
                //soomla grow insight refresh finished
            elseif "onInsightsRefreshStarted" == data.event then
                //soomla grow insight refresh started
            end
        end)
sdkbox.PluginSoomlaGrow:init()
```
