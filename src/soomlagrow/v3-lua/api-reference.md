## API Reference

### Methods
```lua
sdkbox.PluginSoomlaGrow:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginSoomlaGrow:setListener(lis)
```
> Set listener to listen for different events (list below)

```lua
sdkbox.PluginSoomlaGrow:refreshInsights()
```
> Refreshed GROW's Insights information from the server

```lua
sdkbox.PluginSoomlaGrow:payRank(genre)
```
> get pay rank

```lua
sdkbox.PluginSoomlaGrow:purchaseLikelihood(dayquarter)
```
> purchase likelihood time


### Listeners
```lua
onGrowInitialized()
```
> This event is triggered once the highway initialized.

```lua
onGrowConnected()
```
> This event is triggered once the highway is connected to server.

```lua
onGrowDisconnected()
```
> This event is triggered once the highway disconnect from the server.

```lua
onGrowInsightsInitialized()
```
> This event is triggered once the grow insight initialized.

```lua
onInsightsRefreshFailed()
```
> This event is triggered once the grow insight refresh failed.

```lua
onInsightsRefreshFinished()
```
> This event is triggered once the grow insight refresh finished.

```lua
onInsightsRefreshStarted()
```
> This event is triggered once the grow insight refresh started.


