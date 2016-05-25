## API Reference

### Methods
```javascript
sdkbox.PluginSdkboxPlay.init();
```
> Initialize the plugin instance.
The plugin initializes from the sdkbox_config.json file, and reads a configuration of the form:
{
    "leaderboards"     : LeaderboardObject[],
    "achievements"     : AchievementObject[],
    "connect_on_start" : boolean,
    "debug"            : boolean,
    "enabled"          : boolean
}

```javascript
sdkbox.PluginSdkboxPlay.setListener(listener);
```
> Set SdkboxPlay plugin listener.

```javascript
sdkbox.PluginSdkboxPlay.removeListener();
```
> Remove the listener.
This plugin allows only for one listener which will be disabled after calling this method.

```javascript
sdkbox.PluginSdkboxPlay.getVersion();
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```javascript
sdkbox.PluginSdkboxPlay.submitScore(leaderboard_name, score);
```
> Request submission of an score value to a leaderboard name defined in sdkbox_config.json file.
If the leaderboard name does not exists, or the id associated is not defined in the Developer Console for the application,
the call will silently fail.
If everything's right, it will notify the method <code>onScoreSubmitted</code>.

```javascript
sdkbox.PluginSdkboxPlay.showLeaderboard(leaderboard_name);
```
> Request to show the default Leaderboard view.
In this view you'll be able to interactively select between daily, weekly or all-time leaderboard time frames and the scope
to global or you google play's friends results.

```javascript
sdkbox.PluginSdkboxPlay.unlockAchievement(achievement_name);
```
> Request to unlock an achievement defined by its name.
This method assumes the achievement is non incremental.
If the achievement type is incorrectly defined in the configuration file, or the play services determines it is of the wrong type,
this method will fail silently.
Otherwise, if everything is right, the method <code>onAchievementUnlocked</code> will be invoked on the plugin listener.

```javascript
sdkbox.PluginSdkboxPlay.incrementAchievement(achievement_name, increment);
```
> Request to increment the step count of an incremental achievement by the specified number of steps.
This method assumes the achievement is incremental.
If the achievement type is incorrectly defined in the configuration file, or the play services determines it is of the wrong type,
this method will fail silently.
If the call is successful, this method may invoke two different methods:
  + <code>onIncrementalAchievementStep</code> if the achievement is not unlocked.
  + <code>onIncrementalAchievementUnlocked</code> the first time it's been newly unlocked.

```javascript
sdkbox.PluginSdkboxPlay.showAchievements();
```
> Request to show the default Achievements view.
In this view, you'll only see public achievements.
It will show wether or not achievements are unlocked, and the steps towards unlocking it for incremental achievements.
Total experience count is measured as well.

```javascript
sdkbox.PluginSdkboxPlay.isConnected();
```
> Fast method to know plugin's connection status.
@deprecated

```javascript
sdkbox.PluginSdkboxPlay.isSignedIn();
```
> Same as isConnected (deprecated) but more consistent with naming.

```javascript
sdkbox.PluginSdkboxPlay.signin();
```
> Request connection to the platform-specific services backend.
This method will invoke plugin's listener <code>onConnectionStatusChanged</code> method.

```javascript
sdkbox.PluginSdkboxPlay.signout();
```
> Request disconnection from the GooglePlay/Game Center backend.
This method will invoke plugin's listener <code>onConnectionStatusChanged</code> method.

```javascript
sdkbox.PluginSdkboxPlay.getPlayerId();
```
> Get the currently logged in player's id.

```javascript
sdkbox.PluginSdkboxPlay.getPlayerAccountField(field);
```
> Get a field from the user account's info obtained after authentication.
Current values are:
iOS/Android
-----------
  + display_name
  + name
  + player_id
Android only:
-------------------
  + title
  + con_image_uri
  + hires_image_uri
  + last_play_timestamp
  + retrieved_timestamp
If a field not valid is queried an empty string will be returned.


### Listeners
```javascript
onConnectionStatusChanged(status);
```
> Call method invoked when the Plugin connection changes its status.
Values are as follows:
  + GPS_CONNECTED:       successfully connected.
  + GPS_DISCONNECTED:    successfully disconnected.
  + GPS_CONNECTION_ERROR:error with google play services connection.

```javascript
onScoreSubmitted(leaderboard_name,
                  score,
                  maxScoreAllTime,
                  maxScoreWeek,
                  maxScoreToday);
```
> Callback method invoked when an score has been successfully submitted to a leaderboard.
It notifies back with the leaderboard_name (not id, see the sdkbox_config.json file) and the
subbmited score, as well as whether the score is the daily, weekly, or all time best score.
Since Game center can't determine if submitted score is maximum, it will send the max score flags as false.

```javascript
onIncrementalAchievementUnlocked(achievement_name);
```
> Callback method invoked when the request call to increment an achievement is succeessful and
that achievement gets unlocked. This happens when the incremental step count reaches its maximum value. 
Maximum step count for an incremental achievement is defined in the google play developer console.

```javascript
onIncrementalAchievementStep(achievement_name, step);
```
> Callback method invoked when the request call to increment an achievement is successful.
If possible (Google play only) it notifies back with the current achievement step count.

```javascript
onAchievementUnlocked(achievement_name, newlyUnlocked);
```
> Call method invoked when the request call to unlock a non-incremental achievement is successful.
If this is the first time the achievement is unlocked, newUnlocked will be true.


