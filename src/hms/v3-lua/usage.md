### Initialize HMS
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginHMS:init()
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```lua
sdkbox.PluginHMS:login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```lua
sdkbox.PluginHMS:login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```lua
sdkbox.PluginHMS:login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```lua
sdkbox.PluginHMS:logout();
```

### Request Managed Products

```lua
sdkbox.PluginHMS:iapRequestProducts();
```
this method will trigger `onIAPProducts` event

### Purchase Managed Product

```lua
sdkbox.PluginHMS:iapPurchase("coin");
```
this method will trigger `onIAPPurchase` event

### Purchase Unmanaged Product

```lua
local productInfo = {
  priceType = 0, -- 0:consumable 1:non-consumable 2:subscription
  productName = 'product name',
  productId = 'product id',
  amount = '1.00',
  currency = 'CNY',
  country = 'CN',
  sdkChannel = '1', -- sdkChannel size must be between 0 and 4
  serviceCatalog = 'X58',
  reservedInfor = '{"a": 1, "b":"s"}', -- reservedInfor must be json string
  developerPayload = 'payload1'
};
sdkbox.PluginHMS:iapPurchaseWithPrice(JSON:encode(productInfo));
```
this method will trigger `onIAPPurchase` event

### request owned purchase

will return current user own products, include non-consumable, subscription product and consumable product which have not be consumed.

```lua
sdkbox.PluginHMS:iapRequestOwnedPurchases();
```
this method will trigger `onIAPOwnedPurchases` event

### consume product

```lua
sdkbox.PluginHMS:iapConsume(purchaseToken);
```
this method will trigger `onIAPPConsume` event

### request owned purchase record

request current user's all purchase records.
```lua
sdkbox.PluginHMS:iapRequestOwnedPurchaseRecords(purchaseToken);
```
this method will trigger `onIAPOwnedPurchaseRecords` event


### Player Info

#### GetPlayer Info

will trigger listener event `onPlayerInfo`
```lua
sdkbox.PluginHMS:playerRequestInfo();
```

#### GetPlayer ExtraInfo

Will return follow info of current player: isadult, playtime and so on
will trigger listener event `onPlayerExtraInfo`
```lua
sdkbox.PluginHMS:playerRequestInfo();
```

#### Submit GameBegin

submit player game begin event. if your game will sell in china, you should submit game begin event.
will trigger listener event `onPlayerGameBegin`
```lua
sdkbox.PluginHMS:playerSubmitGameBegin();
```

#### Submit GameEnd

submit player game begin event. if your game will sell in china, you should submit game end event.

will trigger listener event `onPlayerGameEnd`

```lua
sdkbox.PluginHMS:playerSubmitGameEnd();
```

### Achievement

#### Request Achievement List

request achivement list, then you can show achievement list by yourself

will trigger listener event `onAchievementList`

```lua
sdkbox.PluginHMS:achievementRequestList();
```

#### AchievementShow

show achivement with hms default ui

will trigger listener event `onAchievementShow`

```lua
sdkbox.PluginHMS:achievementShow();
```

#### achievementVisualize

will trigger listener event `onAchievementVisualize`
```lua
sdkbox.PluginHMS:achievementVisualize();
```

#### achievementGrow

will trigger listener event `onAchievementGrow`
```lua
sdkbox.PluginHMS:achievementGrow();
```

#### achievementMakeSteps

will trigger listener event `onAchievementMakeSteps`
```lua
sdkbox.PluginHMS:achievementMakeSteps();
```

#### achievementReach

```lua
sdkbox.PluginHMS:achievementReach();
```

### Event

#### eventGrow

```lua
sdkbox.PluginHMS:eventGrow();
```

#### eventRequestList

will trigger listener event `onEventList`
```lua
sdkbox.PluginHMS:eventRequestList();
```

### Ranking

#### Check ranking switch status

before invoke ranking related api, you must make sure player is allow to open score.

will trigger listener event `onRankingSwitchStatus`
```lua
sdkbox.PluginHMS:rankingRequestSwitchStatus();
```

will trigger listener event `onRankingSetSwitchStatus`
```lua
sdkbox.PluginHMS:rankingSetSwitchStatus();
```

#### submit score

will trigger listener event `onRankingSubmitScore`

```lua
sdkbox.PluginHMS:rankingSubmitScore(rankingName, score, score_unit);
```

#### Show ranking

show ranking by self.

will trigger listener event `onRankingList`

```lua
local realtime = true; -- true, will request data from hms server; false, will use local cache data
sdkbox.PluginHMS:rankingRequestList(realtime, rankingName);
```

show with hms default ui

will trigger listener event `onRankingShow`

```lua
local timeDimension = 2; -- 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS:rankingShow(timeDimension, rankingName);
```

#### get scores

current player score

will trigger listener event `onRankingCurPlayerScore`

```lua
local timeDimension = 2; -- 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS:rankingRequestCurPlayerScore(rankingName, timeDimension);
```

request player centered score

will trigger listener event `onRankingPlayerCenteredScores`

```lua
local timeDimension = 2; -- 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS:rankingRequestPlayerCenteredScores(rankingName, timeDimension, realtime);
```

### Archive

add archive

will trigger listener event `onArchiveAdd`

```lua
local bmBytes -- cover image data
local dataBytes -- archive binary data
sdkbox.PluginHMS:archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesType,
                               dataBytes);
```

update archive

will trigger listener event `onArchiveUpdate`

```lua
local bmBytes -- cover image data
local dataBytes -- archive binary data
sdkbox.PluginHMS:archiveUpdate(archiveId,
                          playedTime, progress, description,
                          bmBytes, bmBytesType,
                          dataBytes);
```

load archive

will trigger listener event `onArchiveLoad`

```lua
local conflictPolicy = 3;
//-1 -> hms willn't hand conflict, 
//1  -> hms will resolved conflict by played time, 
//2  -> hms will resolved conflict by progress,
//3  -> hms will resolved conflict by last update time
sdkbox.PluginHMS:archiveLoad(archiveId, conflictPolicy);
```

### BUOY

if you game sell in china, you should show buoy
```lua
sdkbox.PluginHMS:buoyShow();
//or
sdkbox.PluginHMS:buoyHide();
```

### Advertisement

caceh ad

```lua
sdkbox.PluginHMS:adCache(adName);
```

show ad

```lua
if (sdkbox.PluginHMS:adIsAvailable(adName)) {
    sdkbox.PluginHMS:adShow(adName);
}
```

hide banner

```lua
sdkbox.PluginHMS:adHide(adName);
```

ad request settings (Optional)

```lua
--[[
adContentClassification:
  "W"->Content suitable for toddlers and older audiences;
 "PI"->Content suitable for kids and older audiences
  "J"->Content suitable for teenagers and older audiences.
  "A"->Content suitable only for adults.
   ""->Unknown rating.
]]--
sdkbox.PluginHMS:adSetAdContentClassification("A");

--[[
tagForUnderAgeOfPromise:
 0->Do not process ad requests as directed to users under the age of consent;
 1->Process ad requests as directed to users under the age of consent;
-1->Whether to process ad requests as directed to users under the age of consent is not specified;
]]--
sdkbox.PluginHMS:adSetTagForUnderAgeOfPromise(0);

--[[
tagForChildProtection:
 0->Do not process ad requests according to the COPPA;
 1->Process ad requests according to the COPPA;
-1->Whether to process ad requests according to the COPPA is not specified;
]]--
sdkbox.PluginHMS:adSetTagForChildProtection(0);

--[[
nonPersonalizedAd
 0->Request both personalized and non-personalized ads (default);
 1->Request only non-personalized ads;
]]--
sdkbox.PluginHMS:adSetNonPersonalizedAd(0);
```

reward ad setting (Optional)

reward data must be URL-encoded and length must be less than 1024

```lua
-- reward ad custom data
sdkbox.PluginHMS:adSetRewardData("cdata");

-- uid for reward ad
sdkbox.PluginHMS:adSetRewardUserId("uid666");
```

### Handling HMS Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.

all listener include code param, you can find code in follow url:

* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/game-return-code-v4
* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/hms-error-code

here we list a specific code:

- 7020: havn't find data in local cache
- 7022: is not adult
- 7024: `huawei mobile market` app is not installed
- 7218: huawei game services is not enabled, or user cancel
- 7204: need install the last application assist
- 7013: not login or archive is not enabled (make sure archive is true in sdkbox_config.json).

```lua
sdkbox.PluginHMS:setListener(function(args)
    -- Account
    if "onLogin" == args.event then
        local code = args.code
        local msg = args.msg
        dump(args, "onLogin:")

    -- Player Info
    else if "onPlayerInfo" == args.event then
    else if "onPlayerExtraInfo" == args.event then
    else if "onPlayerGameBegin" == args.event then
    else if "onPlayerGameEnd" == args.event then

    -- IAP
    else if "onIAPReady" == args.event then
        local code = args.code
        local msg = args.msg
    else if "onIAPProducts" == args.event then
        local code = args.code
        local msg = args.msg
    else if "onIAPPurchase" == args.event then
        local code = args.code
        local msg = args.msg
    else if "onIAPPConsume" == args.event then
        local code = args.code
        local msg = args.msg
    else if "onIAPOwnedPurchases" == args.event then
        local code = args.code
        local msg = args.msg
    else if "onIAPOwnedPurchaseRecords" == args.event then
        local code = args.code
        local msg = args.msg

    -- Achievement
    else if "onAchievementList" == args.event then
    else if "onAchievementShow" == args.event then
    else if "onAchievementVisualize" == args.event then
    else if "onAchievementGrow" == args.event then
    else if "onAchievementMakeSteps" == args.event then

    -- Event
    else if "onEventList" == args.event then

    -- Ranking
    else if "onRankingSwitchStatus" == args.event then
    else if "onRankingSetSwitchStatus" == args.event then
    else if "onRankingSubmitScore" == args.event then
    else if "onRankingShow" == args.event then
    else if "onRankingList" == args.event then
    else if "onRankingCurPlayerScore" == args.event then
    else if "onRankingPlayerCenteredScores" == args.event then
    else if "onRankingMoreScores" == args.event then
    else if "onRankingTopScores" == args.event then

    -- Archive
    else if "onArchiveLimitThumbnailSize" == args.event then
    else if "onArchiveLimitDetailsSize" == args.event then
    else if "onArchiveAdd" == args.event then
    else if "onArchiveShow" == args.event then
    else if "onArchiveSummaryList" == args.event then
    else if "onArchiveSelect" == args.event then
    else if "onArchiveThumbnail(code, errorOrJson, co" == args.event then
    else if "onArchiveUpdate" == args.event then
    else if "onArchiveLoad(code, errorOrJson, cont" == args.event then
    else if "onArchiveRemove" == args.event then

    -- Game Stats
    else if "onGamePlayerStats" == args.event then
    else if "onGameSummary" == args.event then

    -- Ad
    else if "onAdClose" == args.event then
    else if "onAdFail" == args.event then
    else if "onAdLeave" == args.event then
    else if "onAdOpen" == args.event then
    else if "onAdLoad" == args.event then
    else if "onAdClick" == args.event then
    else if "onAdImpression" == args.event then
    else if "onAdReward" == args.event then

    else
        print("unknow event ", args.event)
    end
end)
```
