## Important Notice
If you upgraded to Xcode7 you need to perform the following steps to your project for plugin to function correctly.

#### Disable App Transport Security
Adding the following entry to the plist:
```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
#### Disable Bitcode support
You have to turn off __Bitcode__ support. If you don't cocos2d-x will fail to build.

#### Set your game requires full screen
If your game doesn't support all screen orientations you will need to check `Requires full screen` in Xcode. If you do not, your app will fail Apple's submission process.

#### Whitelist canOpenURL function
This depends on what plugins are in your project. You may need to add the required entry to the `info.plist`, under `LSApplicationQueriesSchemes`.
