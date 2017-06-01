## Cloud Save

SDKBoxPlay support iOS/Google cloud game save, developer can save user's game data in iColud/Google Drive.

### iOS Cloud Save

* The player must have an iCloud account to save games
* developer must [enable iCloud](https://developer.apple.com/library/content/documentation/DataManagement/Conceptual/CloudKitQuickStart/EnablingiCloudandConfiguringCloudKit/EnablingiCloudandConfiguringCloudKit.html#//apple_ref/doc/uid/TP40014987-CH2-SW2) in their App

### Usage

#### load all saved game data

```cpp
sdkbox::PluginSdkboxPlay::loadAllData();
```

#### load special saved game data

```cpp
sdkbox::PluginSdkboxPlay::loadGameData("key2");
```

#### save game data

```cpp
sdkbox::PluginSdkboxPlay::saveGameData("key1", "{\"game_name\": \"sdkbox go\", \"stage\": 3}");
```

iOS SavedGame [Document](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/GameKit_Guide/SavedGames/SavedGames.html)

Android SavedGame [Document](https://developers.google.com/games/services/common/concepts/savedgames)
