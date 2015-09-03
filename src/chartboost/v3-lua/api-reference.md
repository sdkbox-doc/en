## API Reference

### Methods
```lua
sdkbox.PluginChartboost:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginChartboost:show(name)
```
> show ad by specifying ad name.

```lua
sdkbox.PluginChartboost:setListener(listener)
```
> creates the an optional listener.

```lua
sdkbox.PluginChartboost:isAnyViewVisible()
```
> check to see if any views are visible.

```lua
sdkbox.PluginChartboost:isAvailable(name)
```
> is the specified ad available?

```lua
sdkbox.PluginChartboost:cache(name)
```

```lua
sdkbox.PluginChartboost:setAutoCacheAds(shouldCache)
```
> set to enable and disable the auto cache feature (Enabled by default).

```lua
sdkbox.PluginChartboost:getAutoCacheAds()
```
> get the current auto cache behavior (Enabled by default).

```lua
sdkbox.PluginChartboost:closeImpression()
```
> close any visible Chartboost impressions (interstitials, more apps, rewarded
video, etc..) and the loading view (if visible).

```lua
sdkbox.PluginChartboost:setStatusBarBehavior(behavior)
```
> set to control how the fullscreen ad units should interact with the status bar.
(CBStatusBarBehaviorIgnore by default).

```lua
sdkbox.PluginChartboost:didPassAgeGate(pass)
```
> confirm if an age gate passed or failed. When specified Chartboost will wait for
call before showing the IOS App Store.

```lua
sdkbox.PluginChartboost:setShouldPauseClickForConfirmation(shouldPause)
```
> decide if Chartboost SDK should block for an age gate.

```lua
sdkbox.PluginChartboost:handleOpenURL(url, sourceApp)
```
> opens a "deep link" URL for a Chartboost Custom Scheme.

```lua
sdkbox.PluginChartboost:setCustomID(customID)
```
> set a custom identifier to send in the POST body for all Chartboost API server requests.

```lua
sdkbox.PluginChartboost:getCustomID()
```
> get the current custom identifier being sent in the POST body for all Chartboost
API server requests.

```lua
sdkbox.PluginChartboost:setShouldRequestInterstitialsInFirstSession(shouldRequest)
```
> decide if Chartboost SDK should show interstitials in the first session.

```lua
sdkbox.PluginChartboost:setShouldDisplayLoadingViewForMoreApps(shouldDisplay)
```
> decide if Chartboost SDK should show a loading view while preparing to display
the "more applications" UI.

```lua
sdkbox.PluginChartboost:setShouldPrefetchVideoContent(shouldPrefetch)
```
> decide if Chartboost SDK will attempt to fetch videos from the Chartboost API
servers.


### Listeners
```lua
onChartboostCached(name)
```
> there is cached content

```lua
onChartboostShouldDisplay(name)
```
> should Chartboost display

```lua
onChartboostDisplay(name)
```
> Charboost ad has displayed

```lua
onChartboostDismiss(name)
```
> Chartboost ad has been dismissed

```lua
onChartboostClose(name)
```
> Chartboost is not running

```lua
onChartboostClick(name)
```
> Chartboost ad was clicked on

```lua
onChartboostReward(name, reward)
```
> Chartboost reward was given

```lua
onChartboostFailedToLoad(name, e)
```
> Chartboost failed to load

```lua
onChartboostFailToRecordClick(name, e)
```
> Chartboost failed to record click

```lua
onChartboostConfirmation()
```
> Chartboost confirmation

```lua
onChartboostCompleteStore()
```
> Chartboost complete store


