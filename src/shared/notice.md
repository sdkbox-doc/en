##Important Notice
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
You have to turn off Bitcode support otherwise you won't be able to build cocos2d-x


#### Set your game requires full screen 
if your game don't support all the orientations you will need to check `Requires full screen` in xcode, otherwise, you won't be able to submit your app to Apple.


#### Whitelist canOpenURL function
Depends on the plugins in your project, you need to add the required entry to the plist, under `LSApplicationQueriesSchemes`
