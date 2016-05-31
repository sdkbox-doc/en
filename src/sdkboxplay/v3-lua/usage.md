### Initialize SdkboxAds
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginSdkboxPlay:init();
```

### Using SdkboxPlay


#### Intro
SdkboxPlay is an abstraction for Google Play and Game Center’s social services. Under a common API exposes access to Leaderboards and Achievements for each platform.
In order to keep the API fit to the two models, some tradeoffs have been made, which will be detailed in each section

##### Logged in user info

Calling the method `sdkbox.SdkboxPlay:getPlayerId()` to get an id per platform that uniquely identifies the logged-in user.
Additionally, you can query more information about the user. 

######iOS/Android fields

These fields are common to ios and android:
* player_id
* name
* display_name

making a call to `sdkbox.SdkboxPlay:getPlayerAccountField( field )` will return a string with the field
contents.
If the requested field does not exist, empty string will returned in exchange.
`player_id` will be returned by calling `sdkbox.SdkboxPlay:getPlayerId()` too.

######Android only fields

For Android platform, there are some other available fields:

* title
* icon_image_uri
* hires_image_uri
* last_play_timestamp
* retrieved_timestamp

use the same `getPlayerAccountField` to get these values as strings.

#####Achievements

Achievements are defined on the respective platform’s developer console.
There are differences in concept between GooglePlay and GameCenter’s achievements:
+ Google Play differentiates between achievements, and incremental achievements. Google keeps track of incremental achievements progress. Achievements are achieved only once.
+ For Game Center, all achievements are incremental, but Game center does not keep track of its progress. Achievements are expected to be achieved during a game session. Achievements can be set to be unlocked several times.
+ Google Play has the notion of newly unlocked achievement (first time unlocked), and Game Center has the notion of recurrently unlockable achievement. Both concepts are complementary.

To keep things consisten, SdkboxPlay API:

+ Allows you to define non-incremental achievements. For ios, are submitted with an incremental value of 100, which means it will be unlocked.
+ Allows you to define Incremental achievements. In Google play, incremental achievements have defined their unlocking value on the application console. 
+ For consistency, it is recommended to define Google Play’s achievements with a count of 100. This is the value Game Center expects to be reached to unlock an achievement.

##### Leaderboards

Leaderboards are defined on the respective platform’s developer console.
To keep things simple, the current SdkboxPlay implementation does not allow to define group leaderboards from iOS. For both platforms, an arbitrary number of leaderboards can be defined.
Though both, GooglePlay and GameCenter define leaderboards in the same way, in the runtime there are some differences:

+ Google Play creates automatically 3 time frames for each leaderboard: daily, weekly and all time best scores.
+ Game Center creates just one timeframe.

This will be resembled on the observer methods for leaderboard operations as described below.

#### Usage

A call to `sdkbox.SdkboxPlay:init()` will configure the plugin with the selected leaderboards and achievements present in the sdkbox_config.json file.

First, a connection to the games services must be done by calling:

```lua
sdkbox.PluginSdkboxPlay:signin();
```

If connection is successful, you'll be able to use the SdkboxPlay services with the following API:

##### Leaderboards

```lua
sdkbox.PluginSdkboxPlay:submitScore( leaderboard_name, score )
```

This method submits a update request to the given leaderboard. The leaderboard name must match any of the leaderboard names defined in the configuration block.
If a request is sent to a non existent leaderboard, nothing will happen.
Whether to store the new score or not, can be defined in the developer’s console (store always latest score, only maximum, etc.)
This method will invoke plugin’s observer method: 

```lua
sdkbox.PluginSdkboxPlay:onScoreSubmitted(
        leaderboard_name, 
        score, 
        maxScoreAllTime, 
        maxScoreWeek, 
        maxScoreToday )
```

For iOS, this method will have the three boolean flags as false.

```lua
sdkbox.PluginSdkboxPlay:showLeaderboard( leaderboard_name );
```

Request to show the leaderboard information. This will invoke a platform specific UI.
For iOS, there’s no different UI for requesting leaderboards and achievements, so this method will invoke the UI with the leaderboards view enabled.

##### Achievements

```lua
sdkbox.PluginSdkboxPlay:unlockAchievement( achievement_name );
```

Unlock a non incremental achievement. In the case of iOS, it will send a request to Game Center of unlock with 100 progress points.
If the achievement type is incorrectly defined in the configuration file (wrong id), or the play services determines it is of the wrong type (Google play) the method will fail silently.
Upon successful call, this method will invoke the listener’s method: onAchievementUnlocked( const std::string& achievement_name, bool newlyUnlocked ).

```lua
sdkbox.PluginSdkboxPlay:incrementAchievement( achievement_name, increment );
```

Increment an incremental achievement.
The method will silently fail if the achievement type is incorrectly defined in the configuration file (wrong or non existent id), or the play services determines it is of the wrong type (Google Play).
If the call is successful, this method may invoke two different methods:
+ `onIncrementalAchievementStep( achievement_name, step )` if the achievement is not unlocked.
+ `onIncrementalAchievementUnlocked( achievement_name, newlyUnlocked )` the first time it's been unlocked.

```lua
sdkbox.PluginSdkboxPlay:showAchievements( );
```

Request to show the default Achievements view. This view only shows public achievements.
t will show specific per platform information, like whether it’s been unlocked, remaining unlocking steps (Google Play only), total experience count, etc.


### SdkboxPlay events
This allows you to catch `SdkboxAds` events.

```lua
sdkbox.PluginSdkboxPlay:setListener(function(args)
    if "onConnectionStatusChanged" == args.name then
        local status = args.status;

    elseif "onScoreSubmitted" ==  args.name then
        local leaderboard_name = args.leaderboard_name;
        local score= args.score;
        local maxScoreAllTime= args.maxScoreAllTime;
        local maxScoreWeek= args.maxScoreWeek;
        local maxScoreToday= args.maxScoreToday;

    elseif "onIncrementalAchievementUnlocked" ==  args.name then
        local achievement_name = args.achievement_name;

    elseif "onIncrementalAchievementStep" ==  args.name then
        local achievement_name = args.achievement_name;
        local step = args.step;

    elseif "onAchievementUnlocked" ==  args.name then
        local achievement_name = args.achievement_name;
        local newlyUnlocked = args.newlyUnlocked;

    end
end)
```
