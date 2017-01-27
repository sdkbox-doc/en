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
sdkbox.PluginSdkboxPlay.showAllLeaderboards();
```
> Request to show all leaderboards.

```javascript
sdkbox.PluginSdkboxPlay.showLeaderboard(leaderboard_name);
```
> Request to show the default Leaderboard view.
In this view you'll be able to interactively select between daily, weekly or all-time leaderboard time frames and the scope
to global or you google play's friends results.

```javascript
sdkbox.PluginSdkboxPlay.getMyScore(leaderboard_name, time_span, collection_type);
```
> Get The signed-in user score for an specified leaderboard.
This method notifies its result in a call to SdkboxPlay's listener <code>onMyScore</code> method.
<code>time_span</code> offers the abbility to filter leaderboard for one of the three time spans each
leaderboard offers. Values are:
 + 0 : daily time span
 + 1 : weekly time span
 + any other value : all time time span.
<code>collection_type</code> is to filter the leaderboard between social or global scopes.
Values are:
 + 1 : social collection type
 + any other value : global collection type

```javascript
sdkbox.PluginSdkboxPlay.getPlayerCenteredScores(leaderboard_name,
                                                 time_span,
                                                 collection_type,
                                                 number_of_entries);
```
> Android Only !!!
Get leaderboard information.
This method notifies its result in a call to SdkboxPlay's listener `onPlayerCenteredScores` method.
The information supplied is a json array encoded string.
Each json element contains the following information:
```json
  {
     "display_rank"          : string,
     "display_score"         : string,
     "rank"                  : number,   // long
     "score"                 : number,   // long,
     "holder_display_name"   : string,
     "hires_imageuri"        : string,    // content:// protocol
     "lowres_imageuri"       : string,
     "tag"                   : string,
     "timestamp_millis"      : long
   }
```
<code>time_span</code> offers the abbility to filter leaderboard for one of the three time spans each
leaderboard offers. Values are:
 + 0 : daily time span
 + 1 : weekly time span
 + any other value : all time time span.
<code>collection_type</code> is to filter the leaderboard between social or global scopes.
Values are:
 + 1 : social collection type
 + any other value : global collection type

```javascript
sdkbox.PluginSdkboxPlay.loadAchievements(force_reload);
```
> Load achievements metadata.
A forece reload will force a cloud-side requery of the achievements information.
See `onAchievementsLoaded` for a description on the returned information.

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
On Android, the achievement is set to a fixed number of incremental steps. On iOS, the achievment is set as
a percentage value (0..100). In either case, the `increment` value will be added to the current achievement's
value.

```javascript
sdkbox.PluginSdkboxPlay.showAchievements();
```
> Request to show the default Achievements view.
In this view, you'll only see public achievements.
It will show wether or not achievements are unlocked, and the steps towards unlocking it for incremental achievements.
Total experience count is measured as well.

```javascript
sdkbox.PluginSdkboxPlay.reveal(achievement_name);
```
> Reveal a hidden achievement.
This method will notify on plugin's listener `onReveal` or `onRevelError` methods.

```javascript
sdkbox.PluginSdkboxPlay.setSteps(achievement_name, steps);
```
> Set an incremental achievement to the given amount of steps.
If achievement's current steps are already equal or bigger the specified steps, nothing will happen.
This method will  notify on plugin's listener `onSetSteps` or `onSetStepsError` methods.

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
  + icon_image_uri
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
onMyScore(leaderboard_name, time_span, collection_type, score);
```
> Callback method invoked from a call to `getMyScore` method.
`time_span` and `collection_type` are the supplied values to `getMyScore` method call.

```javascript
onMyScoreError(leaderboard_name,
                time_span,
                collection_type,
                error_code,
                error_description);
```
> Callback method invoked from a call to `getMyScore` method and the method was errored.
`time_span` and `collection_type` are the supplied values to `getMyScore` method call.
`error_code` and `error_description` give extended info about the error.

```javascript
onPlayerCenteredScores(leaderboard_name,
                        time_span,
                        collection_type,
                        json_with_score_entries);
```
> Callback method invoked from a call to `getPlayerCenteredScores` method.
`json_with_score_entries` is an json array enconded string, each of which elements is of the form:
Each json element contains the following information:
```json
  {
     "display_rank"          : string,
     "display_score"         : string,
     "rank"                  : number,   // long
     "score"                 : number,   // long,
     "holder_display_name"   : string,
     "hires_imageuri"        : string,    // content:// protocol
     "lowres_imageuri"       : string,
     "tag"                   : string,
     "timestamp_millis"      : long
   }
```
`time_span` and `collection_type` are the values supplied to `getPlayerCenteredScores` method.

```javascript
onPlayerCenteredScoresError(leaderboard_name,
                             time_span,
                             collection_type,
                             error_code,
                             error_description);
```
> Callback method invoked from a call to `getPlayerCenteredScores` method was errored.
`time_span` and `collection_type` are the values supplied to `getPlayerCenteredScores` method.
`error_code` and `error_description` give extended info about the error.

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
onIncrementalAchievementStepError(name, steps, error_code, error_description);
```

```javascript
onAchievementUnlocked(achievement_name, newlyUnlocked);
```
> Call method invoked when the request call to unlock a non-incremental achievement is successful.
If this is the first time the achievement is unlocked, newUnlocked will be true.

```javascript
onAchievementUnlockError(achievement_name, error_code, error_description);
```

```javascript
onAchievementsLoaded(reload_forced, json_achievements_info);
```
> Method invoked after calling plugin's `loadAchievements` method.
The `json_achievements_info` parameter is a json array encoded string.

#### Android fields:
each array element is of the form:
```json
  {
     "id"                        : string,
     "name"                      : string,
     "xp_value"                  : number,
     "last_updated_timestamp"    : number,
     "description"               : string,
     "type"                      : number,   // 0 = standard, 1 = incremental
     "state"                     : number,   // 0 = unlocked, 1 = revealed,   2 = hidden
     "unlocked_image_uri"        : string,   // content:// protocol
     "revealed_image_uri"        : string,   // content:// protocol
  }
```
  If the achievement is incremental, these fileds will also be available:
```json
  {
     "formatted_current_steps"   : string,
     "formatted_total_steps"     : string,
     "current_steps"             : number,
     "total_steps"               : number
  }
```
#### IOS fields:
```json
  {
     "id"                        : string,
     "name"                      : string,
     "xp_value"                  : number,
     "last_updated_timestamp"    : number,
     "description"               : string,   // maybe empty if no achievemnt submission happened before.
     "state"                     : number,   // 0 = unlocked, 1 = revealed,   2 = hidden
     "type"                      : 1,        // on ios all achievemtns are incremental.
     "current_steps"             : number,   // double value. percentage 0.0 .. 100.0
     "total_steps"               : number,   // 100.0
  }
```

iOS only fields:
```json
  {
     "replayable"                : boolean,
     "unachieved_description"    : string
  }
```

```javascript
onSetSteps(name, steps);
```

```javascript
onSetStepsError(name, steps, error_code, error_description);
```

```javascript
onReveal(name);
```

```javascript
onRevealError(name, error_code, error_description);
```


