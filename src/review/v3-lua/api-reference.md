## API Reference

### Methods
```lua
sdkbox.PluginReview:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginReview:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginReview:show(force)
```
> Tells 'SDKBox review plugin' to try and show the prompt (a rating alert).
if you call `show` with `false` or null params,
the prompt will be showed if there is connection available,
the user hasn't declined to rate or hasn't rated current version.
if the item `tryPromptWhenInit` in sdkbox.config is false, you can call this try to show prompt
if you call `show` with `true` params
the prompt will be showed without checks (the prompt is always displayed).
The case where you should call this is if your app has an
explicit "Rate this app" command somewhere. This is similar to rateApp,
but instead of jumping to the review directly, an intermediary prompt is displayed.
another case is for debug

```lua
sdkbox.PluginReview:userDidSignificantEvent(canPromptForRating)
```

```lua
sdkbox.PluginReview:setTitle(title)
```

```lua
sdkbox.PluginReview:setMessage(message)
```

```lua
sdkbox.PluginReview:setCancelButtonTitle(cancelTitle)
```

```lua
sdkbox.PluginReview:setRateButtonTitle(rateTitle)
```

```lua
sdkbox.PluginReview:setRateLaterButtonTitle(rateLaterTitle)
```


### Listeners
```lua
onDisplayAlert()
```
> trigger when alert prompt show

```lua
onDeclineToRate()
```
> trigger when user refuse to rate

```lua
onRate()
```
> trigger when user want to rate

```lua
onRemindLater()
```
> trigger when user want to remind later


