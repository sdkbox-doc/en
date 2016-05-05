### Initialize OneSignal
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```cpp
#include "PluginOneSignal/PluginOneSignal.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginOneSignal::init();
}
```

### Tag a user based on an app event of your choosing so later you can create segments on onesignal.com to target these users.

```cpp
sdkbox::PluginOneSignal::sendTag("key", "value");
```

### Retrieve a list of tags that have been set on the user from the OneSignal server.
```cpp
sdkbox::PluginOneSignal::getTags();
```

### Deletes a tag that was previously set on a user with sendTag
```cpp
sdkbox::PluginOneSignal::deleteTag("key");
```

### Lets you retrieve the OneSignal user id and push token.
```cpp
sdkbox::PluginOneSignal::idsAvailable();
```

### You can call this method with false to opt users out of receiving all notifications through OneSignal.
```cpp
sdkbox::PluginOneSignal::setSubscription(true);
```

### Allows you to send notifications from user to user or schedule ones in the future to be delivered to the current device.

You must build a json string for the API, you can use

- rapidjson
- [picojson](https://github.com/kazuho/picojson)

See OneSignal [create notification POST](https://documentation.onesignal.com/v2.0/docs/notifications-create-notification) call for all options.

Here is a picojson example:
```cpp
// content
picojson::object c;
c["en"] = picojson::value("Test Message");

// ids
picojson::array ids;
ids.push_back(picojson::value("4db7cb0f-daca-49d6-b3dd-a96774de9f72")); // Nexus 5
ids.push_back(picojson::value("33ad9d96-df00-42a2-b5ab-73417f777d42")); // iphone 4s
ids.push_back(picojson::value("5ea075c5-016d-4f55-891c-3b6c4b393e49")); // ios simulator

// data
picojson::object data;
data["foo"] = picojson::value("bar");

//
picojson::object obj;
obj["contents"] = picojson::value(c);
obj["include_player_ids"] = picojson::value(ids);
obj["data"] = picojson::value(data);

picojson::value v(obj);
sdkbox::PluginOneSignal::postNotification(v.serialize());
```

### Implement OneSignalListner
* You can implement OneSignalListener if you want to receive callbacks like video finish playing.
```cpp
#include "PluginOneSignal/PluginOneSignal.h"
class MyClass : public sdkbox::OneSignalListener
{
private:
    void onSendTag(bool success, const std::string& key, const std::string& message) {}
    void onGetTags(const std::string& jsonString) {}
    void onIdsAvailable(const std::string& userId, const std::string& pushToken) {}
    void onPostNotification(bool success, const std::string& message) {}
    void onNotification(bool isActive, const std::string& message, const std::string& additionalData) {}
}
```
