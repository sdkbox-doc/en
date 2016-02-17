## API Reference

### Methods
```javascript
sdkbox.PluginSoomlaGrow.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginSoomlaGrow.setListener(lis);
```
> Set listener to listen for different events (list below)

```javascript
sdkbox.PluginSoomlaGrow.refreshInsights();
```
> Refreshed GROW's Insights information from the server

```javascript
sdkbox.PluginSoomlaGrow.payRank(genre);
```
> get pay rank

```javascript
sdkbox.PluginSoomlaGrow.purchaseLikelihood(dayquarter);
```
> purchase likelihood time


### Listeners
```javascript
onGrowInitialized();
```
> This event is triggered once the highway initialized.

```javascript
onGrowConnected();
```
> This event is triggered once the highway is connected to server.

```javascript
onGrowDisconnected();
```
> This event is triggered once the highway disconnect from the server.

```javascript
onGrowInsightsInitialized();
```
> This event is triggered once the grow insight initialized.

```javascript
onInsightsRefreshFailed();
```
> This event is triggered once the grow insight refresh failed.

```javascript
onInsightsRefreshFinished();
```
> This event is triggered once the grow insight refresh finished.

```javascript
onInsightsRefreshStarted();
```
> This event is triggered once the grow insight refresh started.


