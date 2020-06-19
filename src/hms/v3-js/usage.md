### Register Javascript Functions
You need to register all the HMS JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```javascript
#include "PluginHMSJS.hpp"
#include "PluginHMSJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```javascript
sc->addRegisterCallback(register_all_PluginHMSJS);
sc->addRegisterCallback(register_all_PluginHMSJS_helper);
```

### Initialize HMS
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.HMS.init();
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```javascript
sdkbox.HMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.HMS.login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```javascript
sdkbox.HMS.login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```javascript
sdkbox.HMS.logout();
```

### Request Managed Products

```javascript
sdkbox.HMS.iapRequestProducts();
```
this method will trigger `onIAPProducts` event

### Purchase Managed Product

```javascript
sdkbox.HMS.iapPurchase("coin");
```
this method will trigger `onIAPPurchase` event

### Purchase Unmanaged Product

```javascript
let productInfo = {
  priceType: 0, // 0:consumable 1:non-consumable 2:subscription
  productName: 'product name',
  productId: 'product id',
  amount: '1.00',
  currency: 'CNY',
  country: 'CN',
  sdkChannel: '1', // sdkChannel size must be between 0 and 4
  serviceCatalog: 'X58',
  reservedInfor: '{"a": 1, "b":"s"}', // reservedInfor must be json string
  developerPayload: 'payload1'
};
sdkbox.HMS.iapPurchaseWithPrice(JSON.stringify(productInfo));
```
this method will trigger `onIAPPurchase` event

### request owned purchase

will return current user own products, include non-consumable, subscription product and consumable product which have not be consumed.

```javascript
sdkbox.HMS.iapRequestOwnedPurchases();
```
this method will trigger `onIAPOwnedPurchases` event

### consume product

```javascript
sdkbox.HMS.iapConsume(purchaseToken);
```
this method will trigger `onIAPPConsume` event

### request owned purchase record

request current user's all purchase records.
```javascript
sdkbox.HMS.iapRequestOwnedPurchaseRecords(purchaseToken);
```
this method will trigger `onIAPOwnedPurchaseRecords` event

### Player Info

#### GetPlayer Info

will trigger listener event `onPlayerInfo`
```javascript
sdkbox.HMS.playerRequestInfo();
```

#### GetPlayer ExtraInfo

Will return follow info of current player: isadult, playtime and so on
will trigger listener event `onPlayerExtraInfo`
```javascript
sdkbox.HMS.playerRequestInfo();
```

#### Submit GameBegin

submit player game begin event. if your game will sell in china, you should submit game begin event.
will trigger listener event `onPlayerGameBegin`
```javascript
sdkbox.HMS.playerSubmitGameBegin();
```

#### Submit GameEnd

submit player game begin event. if your game will sell in china, you should submit game end event.

will trigger listener event `onPlayerGameEnd`

```javascript
sdkbox.HMS.playerSubmitGameEnd();
```

### Achievement

#### Request Achievement List

request achivement list, then you can show achievement list by yourself

will trigger listener event `onAchievementList`

```javascript
sdkbox.HMS.achievementRequestList();
```

#### AchievementShow

show achivement with hms default ui

will trigger listener event `onAchievementShow`

```javascript
sdkbox.HMS.achievementShow();
```

#### achievementVisualize

will trigger listener event `onAchievementVisualize`
```javascript
sdkbox.HMS.achievementVisualize();
```

#### achievementGrow

will trigger listener event `onAchievementGrow`
```javascript
sdkbox.HMS.achievementGrow();
```

#### achievementMakeSteps

will trigger listener event `onAchievementMakeSteps`
```javascript
sdkbox.HMS.achievementMakeSteps();
```

#### achievementReach

```javascript
sdkbox.HMS.achievementReach();
```

### Event

#### eventGrow

```javascript
sdkbox.HMS.eventGrow();
```

#### eventRequestList

will trigger listener event `onEventList`
```javascript
sdkbox.HMS.eventRequestList();
```

### Ranking

#### Check ranking switch status

before invoke ranking related api, you must make sure player is allow to open score.

will trigger listener event `onRankingSwitchStatus`
```javascript
sdkbox.HMS.rankingRequestSwitchStatus();
```

will trigger listener event `onRankingSetSwitchStatus`
```javascript
sdkbox.HMS.rankingSetSwitchStatus();
```

#### submit score

will trigger listener event `onRankingSubmitScore`

```javascript
sdkbox.HMS.rankingSubmitScore(rankingName, score, score_unit);
```

#### Show ranking

show ranking by self.

will trigger listener event `onRankingList`

```javascript
const realtime = true; // true, will request data from hms server; false, will use local cache data
sdkbox.HMS.rankingRequestList(realtime, rankingName);
```

show with hms default ui

will trigger listener event `onRankingShow`

```javascript
const timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.HMS.rankingShow(timeDimension, rankingName);
```

#### get scores

current player score

will trigger listener event `onRankingCurPlayerScore`

```javascript
const timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.HMS.rankingRequestCurPlayerScore(rankingName, timeDimension);
```

request player centered score

will trigger listener event `onRankingPlayerCenteredScores`

```javascript
const timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.HMS.rankingRequestPlayerCenteredScores(rankingName, timeDimension, realtime);
```

### Archive

add archive

will trigger listener event `onArchiveAdd`

```javascript
sdkbox.HMS.archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesLen, bmBytesType,
                               dataBytes, dataBytesLen);
```

update archive

will trigger listener event `onArchiveUpdate`

```javascript
sdkbox.HMS.archiveUpdate(archiveId,
                          playedTime, progress, description,
                          bmBytes, bmBytesLen, bmBytesType,
                          dataBytes, dataBytesLen);
```

load archive

will trigger listener event `onArchiveLoad`

```javascript
const conflictPolicy = 3;
//-1 -> hms willn't hand conflict, 
//1  -> hms will resolved conflict by played time, 
//2  -> hms will resolved conflict by progress,
//3  -> hms will resolved conflict by last update time
sdkbox.HMS.archiveLoad(archiveId, conflictPolicy);
```

### BUOY

if you game sell in china, you should show buoy
```javascript
sdkbox.HMS.buoyShow();
//or
sdkbox.HMS.buoyHide();
```

### Handling Purchase Events
This allows you to catch the `HMS` events so that you can perform operations based upon the response from your players and HMS servers.

all listener include code param, you can find code in follow url:

* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/game-return-code-v4
* https://developer.huawei.com/consumer/cn/doc/development/HMS-References/hms-error-code

here we list a specific code:

7020: havn't find data in local cache
7022: is not adult
7024: `huawei mobile market` app is not installed
7218: huawei game services is not enabled, or user cancel
7204: need install the last application assist
7013: not login or archive is not enabled (make sure archive is true in sdkbox_config.json).


```Javascript
sdkbox.HMS.setListener({
    // Account
    onLogin: function (code, msg) {
        // login event
    },

    // Player Info
    onPlayerInfo: function(code, errorOrJson) {
    },

    onPlayerExtraInfo: function(code, errorOrJson) {
    },

    onPlayerGameBegin: function(code, errorOrJson) {
    },

    onPlayerGameEnd: function(code, errorOrJson) {
    },

    // IAP
    onIAPReady: function(code, msg) {
        self.log('HMS Listener onIAPReady:' + code);
        cc.log(msg);
    },
    onIAPProducts: function(code, msg) {
        self.log('HMS Listener onIAPProducts:' + code);
        cc.log(msg);
    },
    onIAPPurchase: function(code, msg) {
        self.log('HMS Listener onIAPPurchase:' + code);
        cc.log(msg);
    },
    onIAPPConsume: function(code, msg) {
        self.log('HMS Listener onIAPPConsume:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchases: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchases:' + code);
        cc.log(msg);
    },
    onIAPOwnedPurchaseRecords: function(code, msg) {
        self.log('HMS Listener onIAPOwnedPurchaseRecords:' + code);
        cc.log(msg);
    },

    // Achievement
    onAchievementList(code, errorOrJson) {
    }

    onAchievementShow(code, errorOrJson) {
    }

    onAchievementVisualize(code, errorOrJson) {
    }

    onAchievementGrow(code, errorOrJson) {
    }

    onAchievementMakeSteps(code, errorOrJson) {
    }

    // Event
    onEventList(code, errorOrJson) {
    }

    // Ranking
    onRankingSwitchStatus(code, errorOrJson) {
    }

    onRankingSetSwitchStatus(code, errorOrJson) {
    }

    onRankingSubmitScore(code, errorOrJson) {
    }

    onRankingShow(code, errorOrJson) {
    }

    onRankingList(code, errorOrJson) {
    }

    onRankingCurPlayerScore(code, errorOrJson) {
    }

    onRankingPlayerCenteredScores(code, errorOrJson) {
    }

    onRankingMoreScores(code, errorOrJson) {
    }

    onRankingTopScores(code, errorOrJson) {
    }

    // Archive
    onArchiveLimitThumbnailSize(code, errorOrJson) {
    }

    onArchiveLimitDetailsSize(code, errorOrJson) {
    }

    onArchiveAdd(code, errorOrJson) {
    }

    onArchiveShow(code, errorOrJson) {
    }

    onArchiveSummaryList(code, errorOrJson) {
    }

    onArchiveSelect(code, errorOrJson) {
    }

    onArchiveThumbnail(code, errorOrJson, coverData:Uint8Array) {
    }

    onArchiveUpdate(code, errorOrJson) {
    }

    onArchiveLoad(code, errorOrJson, contentData:Uint8Array) {
    }

    onArchiveRemove(code, errorOrJson) {
    }

    // Game Stats
    onGamePlayerStats(code, errorOrJson) {
    }

    onGameSummary(code, errorOrJson) {
    }


});
```
