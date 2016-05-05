### Initialize OneSignal
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginOneSignal:init()
```

### Tag a user based on an app event of your choosing so later you can create segments on onesignal.com to target these users.

```lua
sdkbo.PluginOneSignal::sendTag("key", "value");
```

### Retrieve a list of tags that have been set on the user from the OneSignal server.
```lua
sdkbo.PluginOneSignal::getTags();
```

### Deletes a tag that was previously set on a user with sendTag
```lua
sdkbo.PluginOneSignal::deleteTag("key");
```

### Lets you retrieve the OneSignal user id and push token.
```lua
sdkbo.PluginOneSignal::idsAvailable();
```

### You can call this method with false to opt users out of receiving all notifications through OneSignal.
```lua
sdkbo.PluginOneSignal::setSubscription(true);
```

### Allows you to send notifications from user to user or schedule ones in the future to be delivered to the current device.

You must build a json string for the API, you can use
- rapidjson
- picojson

See OneSignal [create notification POST](https://documentation.onesignal.com/v2.0/docs/notifications-create-notification) call for all options.

Here is a picojson example:
```lua
local data = {
    contents = {
        en = "Test Message"
    },
    data = {
        foo = "bar"
    },
    include_player_ids = {
        "5ea075c5-016d-4f55-891c-3b6c4b393e49",
        "4db7cb0f-daca-49d6-b3dd-a96774de9f72",
        "33ad9d96-df00-42a2-b5ab-73417f777d42","5ea075c5-016d-4f55-891c-3b6c4b393e49"
    }
}
require "json"
sdkbo.PluginOneSignal::postNotification(json.encode(data));
```

### Implement OneSignalListner
* You can implement OneSignalListener if you want to receive callbacks like video finish playing.
```lua

sdkbox.PluginOneSignal.setListener(function(args)
    dump(args)
    local event = args.event
    if "onSendTag" == event then
        -- args.success, args.key, args.message
    elif "onGetTags" == event then
        -- args.jsonString
        -- cjson.decode(args.jsonString)
    elif "onIdsAvailable" == event then
        -- args.userId, args.pushToken
    elif "onPostNotification" == event then
        -- args.success, args.message
    elif "onNotification" == event then
        -- args.isActive, args.message, args.additionalData
    end
end)

```
