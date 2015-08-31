## API Reference

### Methods
```cpp
static bool init();
```
>  initialize the plugin instance.

```cpp
static void setListener(ReviewListener* listener);
```
> Set listener to listen for adcolony events

```cpp
static ReviewListener* getListener();
```
> Get the listener

```cpp
static void removeListener();
```
> Remove the listener, and can't listen to events anymore

```cpp
static void tryToShowPrompt();
```
> Tells PluginReview to try and show the prompt (a rating alert). The prompt will be showed
  if there is connection available, the user hasn't declined to rate
  or hasn't rated current version.
  if the item `tryPromptWhenInit` in sdkbox.config is false, you can call this try to show prompt

```cpp
static void forceToShowPrompt(bool displayRateLaterButton = true);
```
> Tells PluginReview to show the prompt (a rating alert).
  Similar to tryToShowPrompt, but without checks (the prompt is always displayed).
  Passing false will hide the rate later button on the prompt.

  The case where you should call this is if your app has an
  explicit "Rate this app" command somewhere. This is similar to rateApp,
  but instead of jumping to the review directly, an intermediary prompt is displayed.

  another case is for debug

```cpp
static void userDidSignificantEvent(bool canPromptForRating);
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

```cpp
static void setCustomPromptTitle(const std::string& title);
```
> Set customized title for alert view.

```cpp
static void setCustomPromptMessage(const std::string& message);
```
> Set customized message for alert view.

```cpp
static void setCustomPromptCancelButtonTitle(const std::string& cancelTitle);
```
> Set customized cancel button title for alert view.

```cpp
static void setCustomPromptRateButtonTitle(const std::string& rateTitle);
```
> Set customized rate button title for alert view.

```cpp
static void setCustomPromptRateLaterButtonTitle(const std::string& rateLaterTitle);
```
> Set customized rate later button title for alert view.


### Listeners
```cpp
void didDisplayAlert();
```
> trigger when rate prompt display

```cpp
void didDeclineToRate();
```
> trigger when user refuse to rate

```cpp
void didToRate();
```
> trigger when user want to rate

```cpp
void didToRemindLater();
```
> trigger when user want to remind later
