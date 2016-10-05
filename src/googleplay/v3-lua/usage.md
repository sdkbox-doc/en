
##Initialization
Currently the configuration process is done in Lua and passed into Google Play Services when creating the game services object. This object is managed for you, and is available from the ```gpg``` Lua namespace.

To create the game services instance, you need to pass in a table that contains the ```ClientID``` that represents the game you have created in the Google Play Console.

```
    local config = {ClientID="..."}
    gpg:CreateGameServices(config)
```

Note that the ```ClientID``` used is the forwards version from the Google Play Console. There is also a reversed version that is used in the plist. Make sure that you have the correct version, else the initialization will fail.

The full list of configuration data that can be passed is as follows.

```
{
    LogLevel        = 1 or 2,
    EnableSnapshots = true or false,
    ClientID        = forwards client id
}
```

##Callbacks

Most of the Google Play Services methods take a callback argument to return the results. This is mainly because the methods are performed asynchronously, and the results may only be available in the future.

Two types of callbacks are supported. Class method callbacks, and function callbacks (which includes lambda functions)

###Class method example

```
ExampleClass:CallbackMethod(result)
    -- use result here
end

local someClass = ExampleClass:new()

gpg:MethodWithCallback({someClass, ExampleClass.CallbackMethod})
```

Notice that in the class method example, you must pass in the instance of the class as well as the method.

###Lambda function example

```
gpg:MethodWithCallback(function(result)
    -- use result here
end)
```

##Authorization

Before you can do anything with Google Play Services, you must authenticate. If you have previously authenticated, then sdkbox will attempt to log you in automatically. You will still get the same events that you normally would if you are logged in automatically.

To begin the authentication process, you call the following, and pass in either a class method or a lambda method (see Callbacks) to recieve the response.

```
gpg:StartAuthorizationUI(function(result)
    if result.authStatus == gpg.AuthStatus.VALID then
        -- successfully authenticated
    end
end)
```


##Quests API

###Before you begin

Make sure to checkout the Google Play Services Quests [documentation](https://developers.google.com/games/services/common/concepts/quests) in order to better understand how to setup quests using their portal, and for a reference on the API.

Before your game can access events and quests, you must define them first in the [Google Play Developer Console](https://play.google.com/apps/publish/)

###Submitting an event

You send events to the Events service in order to let it know that something has happened. There is no result to this method, so no callback is needed.

```
gpg.Events:Increment("<event id>")
```

### Retrieving events

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

###Displaying quests

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

###Handling quest acceptance

If your game uses the built-in quest UI, then the callback result will have a valid Quest object, which you can test using ```quest.valid()``` otherwise if you are using your own UI, then you can call accept as follows.

```
gpg.Quests:Accept("<quest id>", function(result)
    -- use result.quest here
end)
```

###Handling quest completion

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

##Player statistics

For a complete description of what player statistics are, and how to use them, please refer to the Google Play Services section on the topic [here](https://developers.google.com/games/services/cpp/stats)

###Getting stats for the currently signed in player

You can fetch stats for the current player like this.

```
gpg.Stats:FetchForPlayer(function(result)
    if result.status == gpg.FetchForPlayerResponse.VALID then
        -- use PlayerStats here
    end
end)
```

## Achievements

For the complete documentation, check out [achievements](https://developers.google.com/games/services/common/concepts/achievements)

###State

Achievements can be hidden, revealed, and unlocked.

Achievements can be designated as standard or incremental. Generally, an incremental achievement involves a player making gradual progress towards earning the achievement over a longer period of time

### Showing the UI
```
    gpg.Achievements:ShowAllUI(function(result)
        -- handle the result here
    end)
```

### Fetch Achievements
```
    gpg.Achievements:FetchAll(nil, function(result)
        log:d(log:to_str(result))
    end)
```

### Fetch Achievement
```
    gpg.Achievements:Fetch('CgkI6KjppNEWEAIQBQ', nil, function(result)
        log:d(log:to_str(result))
    end)
```

### Increment Achievement
```
   gpg.Achievements:Increment('CgkI6KjppNEWEAIQBQ')
```

### Unlock Achievement
```
   gpg.Achievements:Unlock('CgkI6KjppNEWEAIQBQ')
```

### Reveal Achievement
```
    gpg.Achievements:Reveal('CgkI6KjppNEWEAIQBQ')
```

## Leaderboards

Checkout additional docs for leaderboards [here](https://developers.google.com/games/services/common/concepts/leaderboards)

### Show UI
```
    gpg.Leaderboards:ShowUI("achievement id")
```

### ShowAllUI
```
    gpg.Leaderboards:ShowAllUI()
```

###Submit Score
```
    gpg.Leaderboards:SubmitScore("achievement id", score, "meta data", function(result)
    end)
```

###FetchAllScoreSummaries
```
    gpg.Leaderboards:FetchAllScoreSummaries("achievement id", data source, function(result)
    end)
```

###FetchAll
```
    gpg.Leaderboards:FetchAll(datasource, function(result)
    end)
```

###FetchScorePage
```
    gpg.Leaderboards:FetchScorePage("achievement id", datasource, time, timespan, collection, maxitmes, function(result)
    end)
```

###FetchNextScorePage
```
    gpg.Leaderboards:FetchNextScorePage(datasource, max items, function(result)
    end)
```

## Realtime Multiplayer

Before you begin, familiarize yourself with the Google Play Games real time multiplayer game concepts [here](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer).

In order to use real time multiplayer, you must [enable](https://developers.google.com/games/services/cpp/realtimeMultiplayer) it in the Google Play Developer Console.

To begin a real time multiplayer game, there are three ways to connect with other players to start a real time multiplayer games.

###Quick game

Lets the player play against randomly selected opponents (via auto-matching).

```
    gpg.Realtime:CreateRealTimeRoom(
        {
            type = "quick_match", -- select automatching
            quick_match_params = 
            {
                maximumAutomatchingPlayers = 1,
                minimumAutomatchingPlayers = 1
            }
        },
        listener, 
        function(result)
            if (gpg:IsSuccess(result.result)) then
                -- use result.room here
            end    
        end
    )
```

###Invite players

This lets you choose specific players to invite.

```
    gpg.Realtime:CreateRealTimeRoom(
        {
            type = "ui", -- select invite players UI
            ui_params = 
            {
                maximumPlayers = 1,
                minimumPlayers = 1
            }
        },
        listener, 
        function(result)
            if (gpg:IsSuccess(result.result)) then
                -- use result.room here
            end           
        end
    )
```

###Accept an invitation

In the case of choosing specific players, you will receive and invitation that you can either accept or decline.

```
    -- you can fetch all pending invitations like this
    -- this will call you back with a result and array of invitations
    gpg.Realtime:FetchInvitations(function(result)
        if (gpg:IsSuccess(result.result)) then
            -- do something with result.invitations
        end
    end)
    
    -- or you can use the UI to accept or decline an invitation
    gpg.Realtime:ShowRoomInboxUI(function(result)
        if (gpg:IsSuccess(result.result)) then
            -- do something with result.invitation
        end
    end)
```

###The listener

The room creation methods, including accepting an invitation, take a listener object. This is so that when things happen in the room, the listener can be informed.

This is also where you will receive data messages from other players, via the ```onDataReceived``` callback method.

```
listener = 
{
    -- called when something about the room changes
    onRoomStatusChanged = function(room)
    end,
    
    -- called when something about the connection changes
    onConnectedSetChanged = function(room)
    end,
    
    -- called when you get connected
    onP2PConnected = function(room, participant) 
    end,
    
    -- called when you get disconnected
    onP2PDisconnected = function(room, participant) 
    end,
    
    -- called if the status of one of the room participants changes
    onParticipantStatusChanged = function(room, participant) 
    end,
    
    -- called whenever someone sends you a message
    onDataReceived = function(room, from_participant, data, is_reliable) 
    end
}
```

### Sending messages to other players

There are two types of messages you can send, reliable and unreliable. 
Reliable messages are guaranteed, and will automatically resend if they get lost. 
There is some overhead to this, so if you don't need reliability, then you can send an unreliable message which is a little more efficient at the cost of reliability.


```
gpg.Realtime:SendReliableMessage(room_id, participant_id, message, function(result)
    if (gpg:IsSuccess(result.result)) then
        -- message send was successful
    end
end)
```

Sending an unreliable message takes a json encoded string for the parameters.
There is no callback, since being unreliable, there is no return status.

```
gpg.Realtime:SendUnreliableMessage(json.encode({
    data = message,
    room_id = room_id
    participant_ids = {}
}))
```

### Leaving a room

```
gpg.Realtime:LeaveRoom(room_id, function(result)
end)
```

### Accepting / declining and dismissing invitations

For accepting invitations, you must provide a listener that will handle all the events for the room you are joining.

```
gpg.Realtime:AcceptInvitation(invitation_id, listener, function(result)
end)
```

Decline and Dismiss do not take callbacks, they just inform the server that you are no longer interested in the invitation.
Dismissing an invitation is for when the game is over, but the invitation is still in your inbox.
```
gpg.Realtime:DeclineInvitation(invitation_id)
```

```
gpg.Realtime:DismissInvitation(invitation_id)
```


## Turn Based Multiplayer

Before you begin make sure to checkout Google's documentation [here](https://developers.google.com/games/services/cpp/turnbasedMultiplayer) and also checkout the turn based multiplayer game concepts [here](https://developers.google.com/games/services/common/concepts/turnbasedMultiplayer)

To start a turn based multiplayer game, there are two ways to do so. You can either use a UI to select players (either Google's or your own), or you can start a quick match which will choose players for you.

###Quick Match
```
local minimumPlayers = 1
local maximumPlayers = 2
local allowAutoMatching = false
gpg.Turnbased:ShowPlayerSelectUI(minimumPlayers, maximumPlayers, allowAutoMatching, function(result)
    params = {
        type = "quick_match",
        minimumAutomatchingPlayers = result.minimumAutomatchingPlayers,
        maximumAutomatchingPlayers = result.maximumAutomatchingPlayers,
        playerIds = result.playerIds
    }
    gpg.Turnbased:CreateTurnBasedMatch(params, function(result)
        if gpg:IsSuccess(result.result) then
            -- use result.match to start playing
        end
    end)
end)
```

###Choose Players UI
```
params = {
    type = "ui",
    minimumAutomatchingPlayers = 1,
    maximumAutomatchingPlayers = 2
}
gpg.Turnbased:CreateTurnBasedMatch(params, function(result)
	if gpg:IsSuccess(result.result) then
	    -- use result.match to start playing
	end
end)
```

### Handling match events

There are two events that need to be handled for turn based multiplayer. You can register for two callbacks (see Callbacks) in order to handle these events.

```
gpg.Turnbased:addMatchEventCallback(
	gpg.DefaultCallbacks.TURN_BASED_MATCH_EVENT, 
	function(event) 
	    gpg.Turnbased:ShowMatchInboxUI(function(result)
	        if gpg:IsSuccess(result.result) then
	            -- start using result.match here
	        end
	    end)	
	end
)
    
-- or

gpg.Turnbased:addMatchEventCallback(
	gpg.DefaultCallbacks.MULTIPLAYER_INVITATION_EVENT, 
	{instance, method}
)

function class:method()
	gpg.Turnbased:ShowMatchInboxUI(function(result)
		if gpg:IsSuccess(result.result) then
			local match = result.match
			if match.matchStatus == gpg.MatchStatus.MY_TURN then
				-- do something with match, take a turn
			elseif match.matchStatus == gpg.MatchStatus.THEIR_TURN then
				-- update for their turn
			elseif match.matchStatus == gpg.MatchStatus.COMPLETED then
				-- complete match, dismiss
			else match.matchStatus == gpg.MatchStatus.EXPIRED then
				-- dismiss 
	    	end
	    end
	end)
end
```

###Taking a turn
To take a turn, you must update the match data with your turn data, and pass it to the next participant. You can use the id "AUTOMATCHING_PARTICIPANT" if you would like the next participant to be automatched.

```
local results = match.participantResults
if winnig then
    results = gpg.Turnbased:createParticipantResult(match_id, match.pendingParticipant.id, my_rank, win_token)
elseif losing then
    results = gpg.Turnbased:createParticipantResult(match.id, match.pendingParticipant.id, my_rank, lose_token)
end
    
local nextParticipant = "AUTOMATCHING_PARTICIPANT"
if match.suggestedNextParticipant.valid and 
   match.suggestedNextParticipant.id ~= "" then
	nextParticipant = match.suggestedNextParticipant.id
end
gpg.Turnbased:TakeMyTurn(match_id, match.pendingParticipant.id, nextParticipant, data, function(result)
end)	
```

###Creating participant results
Sometimes you need to pass participant results to a method. In c++ this is done directly using a struct, but in Lua you need to use an id. This id is used to lookup the struct and pass it for you. You can reuse existing participant ids or just create your own. The method will also return the struct as a Lua object.

```
local results = gpg.Turnbased:CreateParticipantResult(match_id, participant_id, placement, match_result)
-- use results, or call method and pass participant_id
```

###Completing a match
```
gpg.Turnbased:FinishMatchDuringMyTurn(match_id, participant_results_id, data, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

###Leaving a match
You can leave a match at any time, but you need to call the right method, either of the following.

```
gpg.Turnbased:LeaveMatchDuringMyTurn(match_id, next_participant_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end	
end)

-- or

gpg.Turnbased:LeaveMatchDuringTheirTurn(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

###Cancelling a match

```
gpg.Turnbased:CancelMatch(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

###Dismissing a match

```
gpg.Turnbased:CancelMatch(match_id)
```

###Starting rematch

```
gpg.Turnbased:Rematch(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

###Fetching a previous match

```
gpg.Turnbased:FetchMatch(match_id, function(result)
	if gpg:IsSuccess(result.result) then
		-- success
	end
end)
```

### Fetch all matches

```
gpg.Turnbased:FetchMatches(function(result)
	if gpg:IsSuccess(result.result) then
		-- use result.matches here
	end
end)
```

## NearbyConnections

For the complete documentation, check out [Nearby Connections](https://developers.google.com/games/services/cpp/nearby)

### Init

init nearby connection, if not support current platfrom, will return false

```lua
local support = gpg.NearbyConnections:Init("{\"LogLevel\":1}",
    function(result)
        if result.InitializationStatus then
            print('GPG Nearby init success')
        else
            print('GPG Nearby init failed')
        end
    end)
if not support then
    print('GPG Nearby is not support ios')
end
```

### Get local endpoint id

get local endpoint id when connect success

```lua
local endpoint = gpg.NearbyConnections:GetLocalEndpointId();
print('Local Endpoint Id:' .. endpoint)
```

### Get local device id

```lua
local deviceid = gpg.NearbyConnections:GetLocalDeviceId();
print('Local device id:' .. deviceid)
```

### Advertising

start advertising

```lua
gpg.NearbyConnections:StartAdvertising(
    "\"name\":\"\",\"duration\":0,\"app_identifiers\":{\"identifier\":\"com.sdkbox.gpg\"},",
    function(result)
        -- start advertising result

        if (1 == result.start_advertising_result.status) then
            print("GPG start advertising result:" .. result.client_id
                .. " status:" .. result.start_advertising_result.status
                .. " local_endpoint_name:" .. result.start_advertising_result.local_endpoint_name)
        else
            print('start advertising failed:' .. result.start_advertising_result.status)
        end
    end,
    function(result)
        --request connect callback

        local remote_endpoint_id = result.request.remote_endpoint_id
        local payload = result.request.payload

        log:d('GPG receive connect request:' .. remote_endpoint_id)

        -- auto accept or query user
        -- 1. accept connect request
        -- invoke AcceptConnectionRequest
        -- gpg.NearbyConnections:AcceptConnectionRequest(remote_endpoint_id, payload, function (result) end)

        -- 2. reject connect request
        -- invoke RejectConnectionRequest
    end)
```

### Stop advertising

```lua
gpg.NearbyConnections:StopAdvertising()
```

### Accept connect request

```lua
gpg.NearbyConnections:AcceptConnectionRequest(
    remote_endpoint_id,
    payload,
    function (result)
        print('event:' .. result.event)
        if 'OnMessageReceived' == result.event then
            print('OnMessageReceived client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id)
                .. ' payload:' .. tostring(result.payload)
                .. ' is_reliable:' .. tostring(result.is_reliable))
        elseif 'OnDisconnected' == result.event then
            print('OnDisconnected client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id))
        else
            print('Unknown event:' .. result.event);
        end
    end)

```

### Reject connect request

```lua
gpg.NearbyConnections:RejectConnectionRequest(remote_endpoint_id)
```

### Start Discovery

duration in milliseconds

```lua
gpg.NearbyConnections:StartDiscovery(server_id, duration,
    function (result)
        if 'OnEndpointFound' == result.event then
            print('found client_id:' .. tostring(result.client_id)
                .. ' endpoint_id:' .. tostring(result.endpoint_details.endpoint_id)
                .. ' device_id:' .. tostring(result.endpoint_details.device_id)
                .. ' name:' .. tostring(result.endpoint_details.name)
                .. ' service_id:' .. tostring(result.endpoint_details.server_id))
        elseif 'OnEndpointLost' == result.event then
            print('endpoint lost')
        else
            print('unknown event')
        end
    end)
```

### Stop Discovery

```lua
gpg.NearbyConnections:StopDiscovery()
```

### Send Connect Request
```lua
gpg.NearbyConnections:SendConnectionRequest(
    name, remote_endpoint_id, payload,
    function(result)
        -- connect response callback
        if (1 == result.response.status) then
            print('Connect advertising success');
            local remote_endpoint_id = result.response.remote_endpoint_id;
        else
            print('Connect advertising failed');
        end
    end,
    function(result)
        if 'OnMessageReceived' == result.event then
            print('OnMessageReceived client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id)
                .. ' payload:' .. tostring(result.payload)
                .. ' is_reliable:' .. tostring(result.is_reliable))
        elseif 'OnDisconnected' == result.event then
            print('OnDisconnected client_id:' .. tostring(result.client_id)
                .. ' remote_endpoint_id:' .. tostring(result.remote_endpoint_id))
        else
            print('Unknown event:' .. result.event);
        end
    end)
```

### Send Reliable Message

```lua
gpg.NearbyConnections:SendReliableMessage(remote_endpoint_id1, message)
gpg.NearbyConnections:SendReliableMessage([remote_endpoint_id1, remote_endpoint_id2], message);
```

### Send Unreliable Message

```lua
gpg.NearbyConnections:SendUnreliableMessage(remote_endpoint_id1, message)
gpg.NearbyConnections:SendUnreliableMessage([remote_endpoint_id1, remote_endpoint_id2], message);
```

### Disconnect

```lua
gpg.NearbyConnections:Disconnect(remote_endpoint_id)
```

### Stop

```lua
gpg.NearbyConnections:Stop()
```
