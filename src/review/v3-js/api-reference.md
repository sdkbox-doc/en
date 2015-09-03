## API Reference

### Methods
```javascript
sdkbox.PluginReview.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginReview.setListener(listener);
```
> Set listener to listen for adcolony events

```javascript
sdkbox.PluginReview.getListener();
```
> Get the listener

```javascript
sdkbox.PluginReview.removeListener();
```
> Remove the listener, and can't listen to events anymore

```javascript
sdkbox.PluginReview.tryToShowPrompt();
```
> Tells PluginReview to try and show the prompt (a rating alert). The prompt will be showed
  if there is connection available, the user hasn't declined to rate
  or hasn't rated current version.
  if the item `tryPromptWhenInit` in sdkbox.config is false, you can call this try to show prompt

```javascript
sdkbox.PluginReview.forceToShowPrompt();
```
> Tells PluginReview to show the prompt (a rating alert).
  Similar to tryToShowPrompt, but without checks (the prompt is always displayed).
  Passing false will hide the rate later button on the prompt.

  The case where you should call this is if your app has an
  explicit "Rate this app" command somewhere. This is similar to rateApp,
  but instead of jumping to the review directly, an intermediary prompt is displayed.

  another case is for debug

```javascript
sdkbox.PluginReview.userDidSignificantEvent(false);
```
> Tells PluginReview that the user performed a significant event. A significant
  event is whatever you want it to be. If you're app is used to make VoIP
  calls, then you might want to call this method whenever the user places
  a call. If it's a game, you might want to call this whenever the user
  beats a level boss.

  If the user has performed enough significant events and used the app enough,
  you can suppress the rating alert by passing NO for canPromptForRating. The
  rating alert will simply be postponed until it is called again with YES for
  canPromptForRating. The rating alert can also be triggered by appLaunched:
  and appEnteredForeground: (as long as you pass YES for canPromptForRating
  in those methods).

```javascript
sdkbox.PluginReview.setCustomPromptTitle(title);
```
> Set customized title for alert view.

```javascript
sdkbox.PluginReview.setCustomPromptMessage(message);
```
> Set customized message for alert view.

```javascript
sdkbox.PluginReview.setCustomPromptCancelButtonTitle(cancelTitle);
```
> Set customized cancel button title for alert view.

```javascript
sdkbox.PluginReview.setCustomPromptRateButtonTitle(rateTitle);
```
> Set customized rate button title for alert view.

```javascript
sdkbox.PluginReview.setCustomPromptRateLaterButtonTitle(rateLaterTitle);
```
> Set customized rate later button title for alert view.


### Listeners
```javascript
didDisplayAlert();
```
> trigger when rate prompt display

```javascript
didDeclineToRate();
```
> trigger when user refuse to rate

```javascript
didToRate();
```
> trigger when user want to rate

```javascript
didToRemindLater();
```
> trigger when user want to remind later
