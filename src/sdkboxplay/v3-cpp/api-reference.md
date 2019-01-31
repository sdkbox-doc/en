## API Reference

### Methods
```cpp
static bool init ( ) ;
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

<pre>
debug:
   is a common value to all plugins which enables debug info to be sent to the console. Useful when developing.
enabled:
   is a common value to all plugins, which enables or disables the plugin. If enabled is false, the plugin methods will do nothing.
connect_on_start:
   tells the plugin to make an automatic connection to Google Play Services on application startup.
leaderboards:
   a collection of objects of the form:
   {
       "id"   : // google play's assigned leaderboard id
       "name" : // human readable leaderboard name. You'll request leaderboard actions with this name.
   }
achievements:
   a collection of objects of the form:
   {
       "id"          : // google play's assigned achievement id.
       "name"        : // human readable achievement name. You'll request achievement actions with this name.
       "incremental" : // boolean
   }
</pre>

```cpp
static void setListener ( SdkboxPlayListener * listener ) ;
```
> Set SdkboxPlay plugin listener.

```cpp
static SdkboxPlayListener * getListener ( ) ;
```
> Get the plugin's listener.

```cpp
static void removeListener ( ) ;
```
> Remove the listener.
This plugin allows only for one listener which will be disabled after calling this method.

```cpp
static std::string getVersion ( ) ;
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```cpp
static void submitScore ( const std::string & leaderboard_name , long score ) ;
```
> Request submission of an score value to a leaderboard name defined in sdkbox_config.json file.
If the leaderboard name does not exists, or the id associated is not defined in the Developer Console for the application,
the call will silently fail.
If everything's right, it will notify the method <code>onScoreSubmitted</code>.

```cpp
static void showAllLeaderboards ( ) ;
```
> Request to show all leaderboards.

```cpp
static void showLeaderboard ( const std::string & leaderboard_name = "" ) ;
```
> Request to show the default Leaderboard view.
In this view you'll be able to interactively select between daily, weekly or all-time leaderboard time frames and the scope
to global or you google play's friends results.

<pre>
Android only:
 if empty string or __ALL__ is used as leaderboard_name, sdkbox play will invoke an activity
 with all game-defined leader boards.
</pre>

```cpp
static void getMyScore ( const std::string & leaderboard_name ,
                         int time_span ,
                         int collection_type ) ;
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

```cpp
static void getPlayerCenteredScores ( const std::string & leaderboard_name ,
                                      int time_span ,
                                      int collection_type ,
                                      int number_of_entries ) ;
```
> Get leaderboard information.
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

```cpp
static void loadAchievements ( bool force_reload ) ;
```
> Load achievements metadata.
A forece reload will force a cloud-side requery of the achievements information.
See `onAchievementsLoaded` for a description on the returned information.

```cpp
static void unlockAchievement ( const std::string & achievement_name ) ;
```
> Request to unlock an achievement defined by its name.
This method assumes the achievement is non incremental.
If the achievement type is incorrectly defined in the configuration file, or the play services determines it is of the wrong type,
this method will fail silently.
Otherwise, if everything is right, the method <code>onAchievementUnlocked</code> will be invoked on the plugin listener.

```cpp
static void incrementAchievement ( const std::string & achievement_name ,
                                   double increment ) ;
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

```cpp
static void showAchievements ( ) ;
```
> Request to show the default Achievements view.
In this view, you'll only see public achievements.
It will show wether or not achievements are unlocked, and the steps towards unlocking it for incremental achievements.
Total experience count is measured as well.

```cpp
static void reveal ( const std::string & achievement_name ) ;
```
> Reveal a hidden achievement.
This method will notify on plugin's listener `onReveal` or `onRevelError` methods.

```cpp
static void setSteps ( const std::string & achievement_name , double steps ) ;
```
> Set an incremental achievement to the given amount of steps.
If achievement's current steps are already equal or bigger the specified steps, nothing will happen.
This method will  notify on plugin's listener `onSetSteps` or `onSetStepsError` methods.

```cpp
static bool isConnected ( ) ;
```
> Fast method to know plugin's connection status.
@deprecated

```cpp
static bool isSignedIn ( ) ;
```
> Same as isConnected (deprecated) but more consistent with naming.

```cpp
static void signin ( bool showLoginUI = true ) ;
```
> Request connection to the platform-specific services backend.
This method will invoke plugin's listener <code>onConnectionStatusChanged</code> method.

```cpp
static void signout ( ) ;
```
> Request disconnection from the GooglePlay/Game Center backend.
This method will invoke plugin's listener <code>onConnectionStatusChanged</code> method.

```cpp
static std::string getPlayerId ( ) ;
```
> Get the currently logged in player's id.

```cpp
static std::string getPlayerAccountField ( const std::string & field ) ;
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
  + server_auth_code
If a field not valid is queried an empty string will be returned.

```cpp
static void resetAchievements ( ) ;
```
> Calling this class method deletes all progress towards achievements
previously reported for the local player. Hidden achievements that
were previously visible are now hidden again.

<pre>
iOS Only
</pre>

```cpp
static void loadAllData ( ) ;
```
> >>>>>> DEPRECATED >>>>>> Please use loadAllGameData to replace
load all saved user game data in clound
will trigger onGameData callback

```cpp
static void loadGameData ( const std::string & save_name ) ;
```
> >>>>>> DEPRECATED >>>>>> Please use loadAllGameData to replace
load one saved user game data in clound
will trigger onGameData callback

```cpp
static void saveGameData ( const std::string & save_name ,
                           const std::string & data ) ;
```
> >>>>>> DEPRECATED >>>>>> Please use saveGameDataBinary(name, data, length) to replace
save user game data in cloud
will trigger onGameData callback

```cpp
static void fetchGameDataNames ( ) ;
```
> fetch game data names
will trigger onGameDataNames

```cpp
static void loadOneGameData ( const std::string & name ) ;
```
> load game data item
will trigger onLoadGameData

```cpp
static void loadAllGameData ( ) ;
```
> load all saved game data
will trigger onLoadGameData callback

```cpp
static void saveGameDataBinary ( const std::string & name ,
                                 const void * data ,
                                 int length ) ;
```
> save user game data
will trigger onSaveGameData callback

<pre>
Note: if you want to save string, please translate to void>
</pre>

```cpp
static void generateIdentityVerificationSignature();
```
> Generates a signature that allows a third party server to authenticate the local player.

> just vaild on iOS

> [iOS Ref Document](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515407-generateidentityverificationsign)

> Note: on Android, you can get server_auth_code from getPlayerAccountField


### Listeners
```cpp
void onConnectionStatusChanged ( int status );
```
> Call method invoked when the Plugin connection changes its status.
Values are as follows:
  + GPS_CONNECTED:       successfully connected.
  + GPS_DISCONNECTED:    successfully disconnected.
  + GPS_CONNECTION_ERROR:error with google play services connection.

```cpp
void onScoreSubmitted ( const std::string & leaderboard_name ,
                        long score ,
                        bool maxScoreAllTime ,
                        bool maxScoreWeek ,
                        bool maxScoreToday );
```
> Callback method invoked when an score has been successfully submitted to a leaderboard.
It notifies back with the leaderboard_name (not id, see the sdkbox_config.json file) and the
subbmited score, as well as whether the score is the daily, weekly, or all time best score.
Since Game center can't determine if submitted score is maximum, it will send the max score flags as false.

```cpp
void onMyScore ( const std::string & leaderboard_name ,
                 int time_span ,
                 int collection_type ,
                 long score ) 
```
> Callback method invoked from a call to `getMyScore` method.
`time_span` and `collection_type` are the supplied values to `getMyScore` method call.

```cpp
void onMyScoreError ( const std::string & leaderboard_name ,
                      int time_span ,
                      int collection_type ,
                      int error_code ,
                      const std::string & error_description ) 
```
> Callback method invoked from a call to `getMyScore` method and the method was errored.
`time_span` and `collection_type` are the supplied values to `getMyScore` method call.
`error_code` and `error_description` give extended info about the error.

```cpp
void onPlayerCenteredScores ( const std::string & leaderboard_name ,
                              int time_span ,
                              int collection_type ,
                              const std::string & json_with_score_entries ) 
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

```cpp
void onPlayerCenteredScoresError ( const std::string & leaderboard_name ,
                                   int time_span ,
                                   int collection_type ,
                                   int error_code ,
                                   const std::string & error_description ) 
```
> Callback method invoked from a call to `getPlayerCenteredScores` method was errored.
`time_span` and `collection_type` are the values supplied to `getPlayerCenteredScores` method.
`error_code` and `error_description` give extended info about the error.

```cpp
void onIncrementalAchievementUnlocked ( const std::string & achievement_name );
```
> Callback method invoked when the request call to increment an achievement is succeessful and
that achievement gets unlocked. This happens when the incremental step count reaches its maximum value.
Maximum step count for an incremental achievement is defined in the google play developer console.

```cpp
void onIncrementalAchievementStep ( const std::string & achievement_name ,
                                    double step );
```
> Callback method invoked when the request call to increment an achievement is successful.
If possible (Google play only) it notifies back with the current achievement step count.

```cpp
void onIncrementalAchievementStepError ( const std::string & name ,
                                         double steps ,
                                         int error_code ,
                                         const std::string & error_description ) 
```

```cpp
void onAchievementUnlocked ( const std::string & achievement_name ,
                             bool newlyUnlocked );
```
> Call method invoked when the request call to unlock a non-incremental achievement is successful.
If this is the first time the achievement is unlocked, newUnlocked will be true.

```cpp
void onAchievementUnlockError ( const std::string & achievement_name ,
                                int error_code ,
                                const std::string & error_description ) 
```

```cpp
void onAchievementsLoaded ( bool reload_forced ,
                            const std::string & json_achievements_info ) 
```
> Method invoked after calling plugin's `loadAchievements` method.
The `json_achievements_info` parameter is a json array encoded string.
#### Android fields:
each array element is of the form:
```json
  {
     "id"                        : string,
     "name"                      : string,
     "xp_value"                  : string,   // experience value
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
     current_steps"              : number,
     "total_steps"               : number
  }
```
#### IOS fields:
```json
  {
     "id"                        : string,
     "name"                      : string,
     "xp_value"                  : number, int
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
  }
```

```cpp
void onSetSteps ( const std::string & name , double steps ) 
```

```cpp
void onSetStepsError ( const std::string & name ,
                       double steps ,
                       int error_code ,
                       const std::string & error_description ) 
```

```cpp
void onReveal ( const std::string & name ) 
```

```cpp
void onRevealError ( const std::string & name ,
                     int error_code ,
                     const std::string & error_description ) 
```

```cpp
void onGameData ( const std::string & action ,
                  const std::string & name ,
                  const std::string & data ,
                  const std::string & error ) 
```
> >>>>>> DEPRECATED >>>>>>

```cpp
void onSaveGameData ( bool success , const std::string & error ) 
```
> 
```cpp
void onLoadGameData ( const SavedGameData * savedData ,
                      const std::string & error ) 
```
> 
```cpp
void onGameDataNames ( const std::vector <std::string> & names ,
                       const std::string & error ) 
```
> 

