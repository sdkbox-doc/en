### Register Javascript Functions
You need to register all the OneSignal JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginOneSignalJS.hpp"
#include "PluginOneSignalJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginOneSignalJS);
sc->addRegisterCallback(register_all_PluginOneSignalJS_helper);
```

### Initialize OneSignal
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginOneSignal.init();
```

### Tag a user based on an app event of your choosing so later you can create segments on onesignal.com to target these users.

```javascript
sdkboxPluginOneSignalsendTag("key", "value");
```

### Retrieve a list of tags that have been set on the user from the OneSignal server.
```javascript
sdkboxPluginOneSignalgetTags();
```

### Deletes a tag that was previously set on a user with sendTag
```javascript
sdkboxPluginOneSignaldeleteTag("key");
```

### Lets you retrieve the OneSignal user id and push token.
```javascript
sdkboxPluginOneSignalidsAvailable();
```

### You can call this method with false to opt users out of receiving all notifications through OneSignal.
```javascript
sdkboxPluginOneSignalsetSubscription(true);
```

### Allows you to send notifications from user to user or schedule ones in the future to be delivered to the current device.

You must build a json string for the API, you can use
- rapidjson
- picojson

See OneSignal [create notification POST](https://documentation.onesignal.com/v2.0/docs/notifications-create-notification) call for all options.

Here is a picojson example:
```javascript
var data = {
    "contents": {
        "en": "Js test message"
    },
    "include_player_ids": [
        "4db7cb0f-daca-49d6-b3dd-a96774de9f72",
        "33ad9d96-df00-42a2-b5ab-73417f777d42",
        "5ea075c5-016d-4f55-891c-3b6c4b393e49"
    ],
    "data": {
        "foo": "bar"
    }
};
//console.log(JSON.stringify(data));
sdkbox.PluginOneSignal.postNotification(JSON.stringify(data));
```

### Implement OneSignalListner
* You can implement OneSignalListener if you want to receive callbacks like video finish playing.
```javascript

sdkbox.PluginOneSignal.setListener({
    onSendTag :function (bool success, const std::string& key, const std::string& message) { },
    onGetTags :function (const std::string& jsonString) { },
    onIdsAvailable :function (const std::string& userId, const std::string& pushToken) { },
    onPostNotification :function (bool success, const std::string& message) { },
    onNotification :function (bool isActive, const std::string& message, const std::string& additionalData) {}
});

```
