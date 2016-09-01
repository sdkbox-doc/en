##Usage##

##Configuring Google Play Services##

Currently the configuration process is done in Lua and passed into Google Play Services when creating the game services object. This object is managed for you, and is available from the ```gpg``` Lua namespace.

To create the game services instance, you need to pass in a table that contains the ```ClientID``` that represents the game you have created in the Google Play Console.

```
    local config = {ClientID="..."}
    gpg:CreateGameServices(config)
```

Note that the ```ClientID``` used is the forwards version from the Google Play Console. There is also a reversed version that is used in the plist. Make sure that you have the correct version, else the initialization will fail.

##Callbacks##

Most of the Google Play Services methods take a callback argument to return the results. This is mainly because the methods are performed asynchronously, and the results may only be available in the future.

Two types of callbacks are supported. Class method callbacks, and function callbacks (which includes lambda functions)

###Class method example###

```
ExampleClass:CallbackMethod(result)
    -- use result here
end

local someClass = ExampleClass:new()

gpg:MethodWithCallback({someClass, ExampleClass.CallbackMethod})
```

Notice that in the class method example, you must pass in the instance of the class as well as the method.

###Lambda function example###

```
gpg:MethodWithCallback(function(result)
    -- use result here
end)
```

##Authorization##

Before you can do anything with Google Play Services, you must authenticate. If you have previously authenticated, then sdkbox will attempt to log you in automatically. You will still get the same events that you normally would if you are logged in automatically.

To begin the authentication process, you call the following, and pass in either a class method or a lambda method (see Callbacks) to recieve the response.

```
gpg:StartAuthorizationUI(function(result)
    if result.authStatus == gpg.AuthStatus.VALID then
        -- successfully authenticated
    end
end)
```


##Quests API##

###Before you begin###

Make sure to checkout the Google Play Services Quests [documentation](https://developers.google.com/games/services/common/concepts/quests) in order to better understand how to setup quests using their portal, and for a reference on the API.

Before your game can access events and quests, you must define them first in the [Google Play Developer Console](https://play.google.com/apps/publish/)

###Submitting an event###

You send events to the Events service in order to let it know that something has happened. There is no result to this method, so no callback is needed.

```
gpg.Events:Increment("<event id>")
```

### Retrieving events###

To retrieve the current count of events, use one of the *Fetch* methods.

```
gpg.Events:Fetch("<event id>", function(result)
	-- use result.count here
end)

-- or

gpg.Events:FetchAll(function(results)
    for k,v in pairs(results.data) do
        -- k is the event id
        -- use v.count here
    end
end)
```

The complete list of members to callback results can be found in the callback result descriptions section at the end of this documentation.

###Displaying quests###

Google Play Services provides a UI to select quests, or you can provide your own using the quest data from callbacks.

To use the one provided, you can either display all available quests, or just a single quest UI.

```
gpg.Quests:ShowUI("<quest id>", function(result)
    -- use result.quest here
end)

-- or

gpg.Quests:ShowAllUI(function(result)
    -- use result.quest here
end)
``` 

###Handling quest acceptance###

If your game uses the built-in quest UI, then the callback result will have a valid Quest object, which you can test using ```quest.valid()``` otherwise if you are using your own UI, then you can call accept as follows.

```
gpg.Quests:Accept("<quest id>", function(result)
    -- use result.quest here
end)
```

###Handling quest completion###

After players accept a quest, you send events to the quest service to inform it of progress on the quest.

One all the criteria for the quest have been satisfied, you can claim the reward  in the built-in UI or your own.

You claim a quest milestone by calling the claim method.

```
gpg.Quests:ClaimMilestone("<milestone id>", function(result)
    if result.status == gpg.ClaimMilestoneResponse.VALID
        -- use result.milestone.completionRewardData here
    end
end)
```

##Player statistics##

For a complete description of what player statistics are, and how to use them, please refer to the Google Play Services section on the topic [here](https://developers.google.com/games/services/cpp/stats)

###Getting stats for the currently signed in player###

You can fetch stats for the current player like this.

```
gpg.Stats:FetchForPlayer(function(result)
	if result.status == gpg.FetchForPlayerResponse.VALID then
	    -- use PlayerStats here
	end
end)
```


