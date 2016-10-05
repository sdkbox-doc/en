## API Reference

##Callback result descriptions##

### Result Codes
```
{
    VALID                           = 1,
    VALID_BUT_STALE                 = 2,
    VALID_WITH_CONFLICT             = 3,
    FLUSHED                         = 4,
    ERROR_LICENSE_CHECK_FAILED      = -1,
    ERROR_INTERNAL                  = -2,
    ERROR_NOT_AUTHORIZED            = -3,
    ERROR_VERSION_UPDATE_REQUIRED   = -4,
    ERROR_TIMEOUT                   = -5,
    ERROR_CANCELED                  = -6,
    ERROR_MATCH_ALREADY_REMATCHED   = -7,
    ERROR_INACTIVE_MATCH            = -8,
    ERROR_INVALID_RESULTS           = -9,
    ERROR_INVALID_MATCH             = -10,
    ERROR_MATCH_OUT_OF_DATE         = -11,
    ERROR_UI_BUSY                   = -12,
    ERROR_QUEST_NO_LONGER_AVAILABLE = -13,
    ERROR_QUEST_NOT_STARTED         = -14,
    ERROR_MILESTONE_ALREADY_CLAIMED = -15,
    ERROR_MILESTONE_CLAIM_FAILED    = -16,
    ERROR_REAL_TIME_ROOM_NOT_JOINED = -17,
    ERROR_LEFT_ROOM                 = -18
}
```

### Events

####Event description####
```
{
    "valid"       : 1 or 0
    "id"          : event id,
    "name"        : event name,
    "description" : event description text,
    "visibility"  : whether or not event can be seen,
    "count"       : current count of events of this type,
    "imageUrl"    : URL to the event image
}
```

####Events:FetchAll####
```
{
    "status" : 1 or 0 indication success or failure,
    "data"   : {
		event_id : Event,
		...
    }
}
```

####Events:Fetch####
```
{
	"result" : 1 or 0,
	"event"  : Event
}
```

###Quests###

####Quest description####
```
{
	"valid"            : 1 or 0,
	"id"               : quest id,
	"name"             : name of quest,
	"description"      : text description of quest,
	"iconUrl"          : URL to quest icon,
	"bannerUrl"        : URL to quest banner image,
	"currentMilestone" : QuestMileStone,
	"questState"       : quest state, accepted or not,
	"startTime"        : time the quest starts,
	"expirationTime"   : time the quest expires,
	"acceptedTime"     : time that the quest was accepted
}
```

####QuestMilestone description####
```
{
	"valid"                : 1 or 0,
	"id"                   : milestone id,
	"questId"              : quest id for this milestone,
	"eventId"              : event id,
	"state"                : milestone state,
	"currentCount"         : current count,
	"targetCount"          : count to complete milestone,
	"completionRewardData" : string containing reward data from console
}
```

####Quests:Fetch####
```
{
	"result" : 1 or 0,
	"quest"  : Quest
}
```

####Quests:FetchList####
```
{
	"status" : 1 or 0,
	"data    : 1 based array of Quest
}
```

####Quests:Accept####
```
{
	"status" : 1 or 0,
	"quest"  : Quest
}
```

####Quests:ClaimMilestone####
```
{
	"status"    : 1 or 0,
	"milestone" : QuestMilestone
	"quest"     : Quest
}
```

####Quests:ShowUI####
```
{
	"status" : 1 or 0,
	"result" : 1 or 0,
	"quest"  : Quest
}
```

####Quests:ShowAllUI####
```
{
	"status" : 1 or 0,
	"result" : 1 or 0,
	"quest"  : Quest
}
```

###PlayerStats###

####PlayerStats description####
```
{
	"valid"                   : 1 or 0,
	"hasAverageSessionLength" : 1 if valid,
	"averageSessionLength"    : length of session in ?,
	"hasChurnProbability"     : 1 if valid,
	"churnProbability"        : 0 - 1 likelyhood of retention,
	"hasDaysSinceLastPlayed"  : 1 if valid,
	"daysSinceLastPlayed"     : count of days,
	"hasNumberOfPurchases"    : 1 if valid,
	"numberOfPurchases"       : total number of purchases,
	"hasNumberOfSessions"     : 1 if valid,
	"numberOfSessions"        : number of sessions played,
	"hasSessionPercentile"    : 1 if valid,
	"sessionPercentile"       : what percentile they are in,
	"hasSpendPercentile"      : 1 if valid,
	"spendPercentile"         : what spend percentile they are in
}
```

### Achievements

####Achievement description
```
{
	"currentSteps"     : Current steps completed of the achievement,
	"description"      : Description of the achievement.
	"id"               : String Id,
	"lastModifiedTime" : Time last modified,
	"name"             : Name of the achievement,
	"revealedIconUrl"  : URL for the revealed icon,
	"state"            : State, hidden, revealed, unlocked,
	"totalSteps"       : Total number of steps,
	"type"             : Incremental or standard,
	"unlockedIconUrl"  : URL for the unlocked icon,
	"valid"            : 1 or 0 if valid,
	"xp"               : Amount of XP awarded
}
```

#### Achievements:ShowAllUI
```
{
	"result" : result code
}
```

#### Achievements:FetchAll
```
	"result"            : result code,
	"achievement_array" : array of Achievements
```

#### Achievements:Fetch
```
	"result"		 : result code,
	"achievement" : Achievement
```

### Multiplayer

####Player
```
{
    "valid",
    "id",
    "name",
    "avatarUrlHiRes",
    "avatarUrlIconRes",
    "hasLevelInfo",
    "currentLevel",
    "nextLevel",
    "currentXP",
    "lastLevelUpTime",
    "title",
}
```

####PlayerLevel
```
{
    "valid",
    "levelNumber",
    "minimumXP",
    "maximumXP"
}
```

####Participant
```
{
    "valid",
    "displayName",
    "avatarUrl",
    "id",
    "hasPlayer",
    "player",
    "participantStatus",
    "hasMatchResult",
    "matchResult",
    "matchRank",
    "icConnectedToRoom"
}
```

####Room
```
{
    "valid",
    "id",
    "variant",
    "automatchWaitEstimate",
    "creatingParticipant",
    "creationTime",
    "description",
    "participants",
    "remainingAutomatchingSlots",
    "status"
}
```

####MultiplayerInvitation
```
{
    "valid",
    "id",
    "variant",
    "automatchingSlotsAvailable",
    "creationTime",
    "invitingParticipant",
    "type",
    "participants"
}
```

####ParticipantResults
```
{
    "valid",
    "hasResultsForParticipant",
    "placeForParticipant",
    "matchResultForParticipant"
}
```

####TurnBasedMatch
```
{
    "valid",
    "id",
    "creationTime",
    "lastUpdateTime",
    "creatingParticipant",
    "lastUpdatingParticipant",
    "pendingParticipant",
    "matchStatus",
    "automatchingSlotsAvailable",
    "variant",
    "description",
    "number",
    "version"
}
```

### NearbyConnections

#### NearbyConnections:Init
```
{
    "InitializationStatus" : initialization result
}
```

#### NearbyConnections:StartAdvertising
```
{
    "client_id" : client id,
    "start_advertising_result" :
    {
        "status"    : start advertising result,
        "local_endpoint_name"   : local endpoint name
    }
},
{
    "client_id" : client id,
    "request" :
    {
        "remote_endpoint_id" : remote endpoint id,
        "remote_device_id" : remote device id
        "remote_endpoint_name": remote endpoint name
        "payload" : payload message
    }
}
```

#### NearbyConnections:AcceptConnectionRequest
```
{
    "event" : "OnMessageReceived" or "OnDisconnected",
    "client_id" : client id,
    "remote_endpoint_id" : remote endpoint id,
    "payload" : payload message, valid when event is "OnMessageReceived",
    "is_reliable" : if message is reliable, valid when event is "OnMessageReceived"
}
```

#### NearbyConnections:StartDiscovery
```
{
    "event" : "OnEndpointFound" or "",
    "client_id" : client id,
    "remote_endpoint_id", remote endpoint id, valid when event is "OnEndpointLost"
    "endpoint_details" : endpoint info, valid when event is "OnEndpointFound"
    {
        "endpoint_id" : endpoint id,
        "device_id" : device id,
        "name" : name,
        "service_id" : service id
    }
}
```

#### NearbyConnections:SendConnectionRequest

second callback function result is same with NearbyConnections:AcceptConnectionRequest
```
{
    "client_id" : client id,
    "response" : connection response
    {
        "remote_endpoint_id" : remote endpoint id,
        "status" : status code;
        "payload" : payload message;
    }
},
{
    "event" : "OnMessageReceived" or "OnDisconnected",
    "client_id" : client id,
    "remote_endpoint_id" : remote endpoint id,
    "payload" : payload message, valid when event is "OnMessageReceived",
    "is_reliable" : if message is reliable, valid when event is "OnMessageReceived"
}
```