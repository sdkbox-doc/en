Steps For Facebook Plugin
----

* sign up to be a [Facebook Developer](http://developers.facebook.com)

* create a __Test App__

* create a __Test User__

* integrate sdkbox `sdkbox import facebook`

* in the info.plist file you need to specify a few additional keys
```xml
<key>CFBundleURLTypes</key>
<array>
<dict>
    <key>CFBundleURLName</key>
    <string></string>
    <key>CFBundleURLSchemes</key>
    <array>
        <string>fb655158077954837</string>
    </array>
</dict>
</array>
<key>FacebookAppID</key>
<string>655158077954837</string>
<key>FacebookDisplayName</key>
<string>MyTestApp</string>
```
