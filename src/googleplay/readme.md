[&#8249; Google Play Games Services Doc Home](./)

<h1>Google Play Games Services Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX Google Play Games Services plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import googleplay 
```

<<[../shared/post_installation_steps.md]

<<[../../shared/notice.md]

##Usage

### Pre-requisites

Your must create your app on [Google Play Developer console](https://play.google.com/apps/publish) and have game services enabled.

Leaderboards, Achievements, Quests, Events, Realtime Multiplayer and Turn Based multiplayer support must be explicitly enabled and configured in the console.

Please follow [this guide](https://developers.google.com/games/services/console/enabling) to setup Google Play Games Services for your game. After the setup, you can follow [this guide](https://developers.google.com/games/services/console/configuring) to enable different Games Services for your game.

> Note: Your Games Services will use your release keystore by default, so if you want to test your game in debug settings, please link an additional app with [debug keystore](http://stackoverflow.com/questions/17612928/should-i-use-debug-keystore-with-google-play-game-services-during-development)

<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]


