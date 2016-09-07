##Usage
### Register Javascript Functions
You need to register all the Google Play Games JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginSdkboxGooglePlay.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginSdkboxGooglePlay);
```

### Pre-requisites

Your application must be registered on the Google Developer console, and have play services enabled.
Leaderboards, Achievements, Quests, Events, Realtime Multiplayer and Turn Based multiplayer support must be explicitly enabled and configured in the console.

For more information please refer to:
+ Client Ids: https://developers.google.com/games/services/console/enabling
+ Configure services: https://developers.google.com/games/services/console/configuring

Make sure your applications are **always** signed with your release certificate. 

### Initialize Google Play Games (GPG)
Google Play initialization is thorughout a `gpg.Builder` object.
This is a valid copy-and-paste example for authenticating into the library:

```

// 1
var config = new gpg.PlatformConfiguration();

if ( !_game_services || !_game_services->IsAuthorized() ) {
        _game_services = gpg::GameServices::Builder()
                .SetOnAuthActionStarted([this](gpg::AuthOperation op) {
                    // 2
                    
                })
                .SetOnAuthActionFinished([this](gpg::AuthOperation op, gpg::AuthStatus status) {
                    
                    // 3
                    
                    if ( status==gpg::AuthStatus::VALID ) {
                        // 4
                        _signed_in = true;                       
                    } else {
                        // 5
                        _signed_in = false;
                    }
                    
                })
                .SetDefaultOnLog( gpg::LogLevel::VERBOSE )  // 6
                .EnableSnapshots()                          // 7
                .Create( config );                          // 8
    } 
```

Let's dive into this process step by step.

#### // 1
Create a `gpg.PlatformConfiguration` object. The client id will be specific for your application, and only needed on iOS.
It is thus an optional call, but won't hurt having it set for Android as well.

This object is needed to create a GameServices object, which is the object that will proxy to the whole Google Play library objects.

The GPG authentication process, either sign-in or sign-out, spans into two phases:

#### // 2 Auth started.
This function needs a callback of the form:

```
/**
 * @typedef {{AuthOperation:gpg.AuthOperation}}
 */
var AuthActionStartedCallbackParams;

/**
 * @callback AuthActionStartedCallback
 * @param {AuthActionStartedCallbackParams} result;
 */
```

This function is mostly informative. See `gpg.AuthOperation` enum for more details.

#### // 3 Auth finished.
This function needs a callback of the form:

```
/**
 * @typedef {{AuthOperation:number, AuthStatus:number}}
 */
var AuthActionFinishedCallbackParams;

/**
 * @callback AuthActionFinishedCallback
 * @param {AuthActionFinishedCallbackParams} result;
 */
```

The callback be invoked with the operation type `AuthOperation` :sign-in or sign-out and the operation result `AuthStatus`.
This steps, is very important since it will tell whether the user got authenticated `// 4` or not `// 5`.
The `gpg.IsSuccess(...)` will be the common idiom to verify whether an operation's been succesful or not.

#### // 4
This will be a good point to get local user information, as well as modify the UI to signal authorized.

#### // 5
Things did not work as expected.

#### // 6
This is an optional step, but worth mentioning since this is the only place where GPG loggin capabilities can be controlled from.

This is an optional step.

#### // 7
If your game expects to save games on the cloud, this is step would be mandatory, and optional otherwise.

#### // 8
This `Create` call is the actual executable code to be authenticated, notified appropriately and agin access to the GPG objects.
GPG interaction will happen by means of a `gpg::GameServices` object. This object will eventually been passed to the `Create` method's callback if everything went ok.

#### Signed in.

After following the previous code, your system can be signed_in or not to GPG. A common idiom about how to deal with a login ui or sign out, could be this code:

```
	if ( _game_services ) {
	    if ( _signed_in ) {
	        _game_services.SignOut();
	    } else {
	        _game_services.StartAuthorizationUI();
	    }
	}
```

### gpg::GameServices

An instance of this object will be granted once the Authentication process works.
It will grant access to the GPG library functionality, by exposing the following:

#### gpg::PlayerManager and gpg::StatsManager

Gets and sets various player-related data.
For example, gives information about the current logged-in player `FetchSelf`, or about any player identified by an id `Fetch`.
Also, player stats can be obtained with interesting information such as a player's average session length, number of days since last played or the number of purchased he's done on the game.

#### gpg::SnapshotManager

The Saved Games service gives you a convenient way to save your players' game progression to Google's servers. Your game can retrieve the saved game data to allow returning players to continue a game at their last save point from any device.
The Saved Games service makes it possible to synchronize a player's game data across multiple devices.

For more intormation refer to: https://developers.google.com/games/services/common/concepts/savedgames

#### gpg::LeaderboardManager

Leaderboards can be a fun way to drive competition among your players, both for your most hardcore fans (who will be fighting for the top spot in a public leaderboard) and for your more casual players (who will be interested in comparing their progress to their friends').

For example, it gives access to metadata about a leaderboard `Fetch`, pages with user's scores `FetchScorePage`, etc.

For more information refer to: https://developers.google.com/games/services/common/concepts/leaderboards

#### gpg::AchievementManager

Achievements can be a great way to increase your users' engagement within your game. You can implement achievements in your game to encourage players to experiment with features they might not normally use, or to approach your game with entirely different play styles. Achievements can also be a fun way for players to compare their progress with each other and engage in light-hearted competition.

For example, you could unlock `Unlock`, increment `Increment` or reveal an achievement `Reveal`.

For more information refer to: https://developers.google.com/games/services/common/concepts/achievements

#### gpg::QuestManager, gpg.EventManager

The Google Play Games events service allows you to collect cumulative data generated by your players during gameplay and store them in Google's servers for game analytics. You can flexibly define what player data your game should collect; this might include metrics such as how often:

+ Players use a particular item
+ Players reach a certain level
+ Players perform some specific game action

You can use the events data as feedback on how to improve your game. For example, you can adjust the difficulty level of certain levels in your game that players are finding too hard to complete.

For example you could accept a Quest `Accept` or claim milestones on a given quest `AcceptMilestone`.

For more information refer to: https://developers.google.com/games/services/common/concepts/quests

#### gpg::TurnBasedMultiplayer

In a turn-based multiplayer game, a single shared state is passed between multiple players, and only one player has permission to modify the shared state at a time. Players take turns asynchronously according to an order of play determined by the game. Your game can use the turn-based multiplayer API provided by Google Play games services to manage the following tasks:

+ Invite players to join a turn-based multiplayer match, look for random players to be automatically matched to your game, or a combination of both. Google Play games services allows you to host up to eight participants in a match.
+ Store participant and match state information on Google's servers and share updated match data asynchronously with all participants over the lifecycle of the turn-based match.
+ Send match invitation and turn notifications to players. Notifications appear on all devices on which the player is logged in (unless disabled).

For more information refer to: https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer

#### gpg::RealTimeMultiplayer

Your game can use the real-time multiplayer API in Google Play games services to connect multiple players together in a single game session and transfer data messages between connected players. Using the real-time multiplayer API can help to simplify your game development effort because the API handles the following tasks on your behalf:

+ Manages network connections to create and maintain a real-time multiplayer room (a virtual construct that enables network communication between multiple players in the same game session and lets players send data directly to one another).
+ Provides a player selection user interface (UI) to invite players to join a room, look for random players for auto-matching, or a combination of both.
+ Stores participant and room state information on the Google Play games services servers during the lifecycle of the real-time multiplayer game.
+ Sends room invitations and updates to players. Notifications appear on all devices on which the player is logged in (unless disabled).

For more information refer to: https://developers.google.com/games/services/common/concepts/realtimeMultiplayer

#### Nearby Connections (Android only)

