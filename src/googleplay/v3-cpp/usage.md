

### Initialize Google Play Games
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginGPG::init();
}
```

### Authorization
All Google Play Game services require user login, make sure you request user to login before using any of the services. For more information take a look at the [official documentation](https://developers.google.com/games/services/cpp/GettingStartedNativeClient#concepts)

### Achievements
For Achievements to work, make sure you linked Game Services with your game, also make sure the game is in "Published" state. For more information please take a look at [achievements documentation](https://developers.google.com/games/services/common/concepts/achievements)

### Leaderboards
For Leaderboards to work, make sure you linked Game Services with your game, also make sure the game is in "Published" state. For more information please take a look at [leaderboards documentation](https://developers.google.com/games/services/common/concepts/leaderboards)

### Saved Games
Saved Games feature requires to be turned on during initialization stage by calling `EnableSnapshots()` as well as Enable it in the Google Play Developer Console. For more information please take a look at [Saved Games documentation](https://developers.google.com/games/services/common/concepts/savedgames)

### Real-time multiplayer
For Real-time multiplayer to work, make sure you linked Game Services with your game, also make sure the game is in "Published" state. For more information please take a look at [Real-time Multiplayer documentation](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer)

### Turn-based multiplayer
For Turn-based multiplayer to work, make sure you linked Game Services with your game, also make sure the game is in "Published" state. For more information please take a look at [Turn-based Multiplayer documentation](https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer)

### Events and Quests
For Events and Quests to work, make sure you linked Game Services with your game, also make sure the game is in "Published" state. For more information please take a look at [Events and Quests documentation](https://developers.google.com/games/services/common/concepts/quests)

### Player Statistics
Player Stats adds useful analytics data to your game. For more information please take a look at [Player Stats documentation](https://developers.google.com/games/services/cpp/stats) 

### Nearby Connections
Nearby Connections enables local multiplayer and screen casting for your game. For more information please take a look at [Nearby documentation](https://developers.google.com/games/services/cpp/nearby)
