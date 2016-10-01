
### Register Javascript Functions
You need to register all the Google Play Games JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginSdkboxGooglePlayJS.hpp"
#include "PluginSdkboxGooglePlayJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
    sc->addRegisterCallback(register_all_PluginSdkboxGooglePlayJS);
    sc->addRegisterCallback(register_all_PluginSdkboxGooglePlayJS_helper);
```

### Initialize Google Play Games
Google Play initialization is thorughout a `gpg.Builder` object.
This is a valid copy-and-paste example for authenticating into the library:

```javascript

//Initialization
var config = new gpg.PlatformConfiguration();
config.SetClientID('777734739048-cdkbeieil19d6pfkavddrri5o19gk4ni.apps.googleusercontent.com');

new gpg.GameServices.Builder()
            .SetOnAuthActionStarted( function( result ) {
                // Auth started callback
            })
            .SetOnAuthActionFinished( function( result ) {
                // Auth finished callback
            })
            .SetLogging( gpg.LogLevel.INFO )	// Set Logging level
            .EnableSnapshots()					// Enable Snapshot (Saved Game) functionailty
            .Create( config, function( game_services ) {
                // 8
            } );
```

Let's dive into this process step by step.

###Initialization Process breakdown
Create a `gpg.PlatformConfiguration` object. The client id will be specific for your application, and only needed on iOS.

The next step is to create a GameServices object, it will provide the access to all Google Play Game Services.


#### Authorization Callback
There are two callback for GPG authentication `AuthActionStarted` and `AuthActionFinished`

#### Auth started

```javascript
//result.AuthOperation indicates if user wants sign in or sign out
.SetOnAuthActionStarted(
    function( result ) {
        cc.log('on auth action started: ' + result.AuthOperation);
    })
```

#### Auth finished

```javascript
.SetOnAuthActionFinished(
    function( result ) {
        cc.log('on auth action finished: ' + result.AuthOperation + ' ' + result.AuthStatus);
    })
```

#### Set Logging Level
Set Logging level is an optional step, but worth mentioning since this is the only place where GPG logging capabilities can be controlled from.


#### Enable Saved Game
If your game expects to save games on the cloud, this is step would be mandatory and you have to specify it during initialization.

#### Step 8
Until this steps, all previous code is authentication set up.
This `Create` call is the actual executable code to be authenticated, notified apropriately and agin access to the GPG objects.
GPG interation will happen by means of a `gpg.GameServices` object. This object will eventually been passed to the `Create` method's callback if everything went ok.

### Authorization

All Google Play Game services require user login. So after GPG has been initialized you should attempt to log user in with following API

```javascript
	game_services.StartAuthorizationUI();
```

### Achievements

Achievements can be a great way to increase your users' engagement within your game. You can implement achievements in your game to encourage players to experiment with features they might not normally use, or to approach your game with entirely different play styles. Achievements can also be a fun way for players to compare their progress with each other and engage in light-hearted competition.

For example, you could unlock `gpg.GameServices.Achievements.Unlock`, increment `gpg.GameServices.Achievements.Increment` or reveal an achievement `gpg.GameServices.Achievements.Reveal`.

For more information refer to: [Achievements documentation](https://developers.google.com/games/services/common/concepts/achievements)

### Leaderboards

Leaderboards can be a fun way to drive competition among your players, both for your most hardcore fans (who will be fighting for the top spot in a public leaderboard) and for your more casual players (who will be interested in comparing their progress to their friends').

For example, it gives access to metadata about a leaderboard `gpg.GameServices.Leaderboards.Fetch`, pages with user's scores `gpg.GameServices.Leaderboards.FetchScorePage`, etc.

For more information refer to: [Leaderboards documentation](https://developers.google.com/games/services/common/concepts/leaderboards)

### Saved Games

The Saved Games service gives you a convenient way to save your players' game progression to Google's servers. Your game can retrieve the saved game data to allow returning players to continue a game at their last save point from any device.
The Saved Games service makes it possible to synchronize a player's game data across multiple devices.

For more intormation refer to: [Saved Games documentation](https://developers.google.com/games/services/common/concepts/savedgames)

### Real-time multiplayer

Your game can use the real-time multiplayer API in Google Play games services to connect multiple players together in a single game session and transfer data messages between connected players. Using the real-time multiplayer API can help to simplify your game development effort because the API handles the following tasks on your behalf:

+ Manages network connections to create and maintain a real-time multiplayer room (a virtual construct that enables network communication between multiple players in the same game session and lets players send data directly to one another).
+ Provides a player selection user interface (UI) to invite players to join a room, look for random players for auto-matching, or a combination of both.
+ Stores participant and room state information on the Google Play games services servers during the lifecycle of the real-time multiplayer game.
+ Sends room invitations and updates to players. Notifications appear on all devices on which the player is logged in (unless disabled).

For more information refer to: [Real-time Multiplayer documentation](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer)

### Turn-based multiplayer

In a turn-based multiplayer game, a single shared state is passed between multiple players, and only one player has permission to modify the shared state at a time. Players take turns asynchronously according to an order of play determined by the game. Your game can use the turn-based multiplayer API provided by Google Play games services to manage the following tasks:

+ Invite players to join a turn-based multiplayer match, look for random players to be automatically matched to your game, or a combination of both. Google Play games services allows you to host up to eight participants in a match.
+ Store participant and match state information on Google's servers and share updated match data asynchronously with all participants over the lifecycle of the turn-based match.
+ Send match invitation and turn notifications to players. Notifications appear on all devices on which the player is logged in (unless disabled).

For more information refer to: [Turn-based Multiplayer documentation](https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer)

### Player Statistics

Gets and sets various player-related data.
For example, gives information about the current logged-in player `gpg.GameServices.Players.FetchSelf`, or about any player identified by an id `gpg.GameServices.Players.Fetch`.
Also, player stats can be obtained with interesting information such as a player's average session length, number of days since last played or the number of purchased he's done on the game. For more information please take a look at [Player Stats documentation](https://developers.google.com/games/services/cpp/stats) 


### Events and Quests

The Google Play Games events service allows you to collect cumulative data generated by your players during gameplay and store them in Google's servers for game analytics. You can flexibly define what player data your game should collect; this might include metrics such as how often:

+ Players use a particular item
+ Players reach a certain level
+ Players perform some specific game action

You can use the events data as feedback on how to improve your game. For example, you can adjust the difficulty level of certain levels in your game that players are finding too hard to complete.

For example you could accept a Quest `gpg.GameServices.Quests.Accept` or claim milestones on a given quest `gpg.GameServices.Quests.AcceptMilestone`.

For more information refer to: [Events and Quests documentation](https://developers.google.com/games/services/common/concepts/quests)

### Nearby Connections
Nearby Connections enables local multiplayer and screen casting for your game. For more information please take a look at [Nearby documentation](https://developers.google.com/games/services/cpp/nearby)
