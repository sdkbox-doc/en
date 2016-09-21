

### Initialize Google Play Games
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSdkboxGooglePlay::init();
}
```

### Authorization


### Achievements
### Leaderboards
### Turn-based multiplayer
### Real-time multiplayer
### Events and Quests
### Saved Games
### Nearby Connections (Android only)
### Player Statistics

For other Google Play Game Services functionalities please take a look at official google play games services [documentation](https://developers.google.com/games/services/cpp/GettingStartedNativeClient)
