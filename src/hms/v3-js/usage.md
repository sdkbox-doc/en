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
sdkbox.PluginHMS.init();
```

### Login

HMS provides three way to login.

* Signing In with HUAWEI ID(ID Token)

```javascript
sdkbox.PluginHMS.login(1);
```

* Signing In with HUAWEI ID(Authorization Code)

```javascript
sdkbox.PluginHMS.login(2);
```

* Silently Signing In With HUAWEI ID

Authorization is required only at the first sign-in to your app using a HUAWEI ID. Subsequent sign-ins using the same HUAWEI ID does not require any authorization.

```javascript
sdkbox.PluginHMS.login(0);
```

> `onLogin` will be triggered when HMS AccountKit reruns the login response.

HMS offical [documentation](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/account-guide-v4)

### Logout

```javascript
sdkbox.PluginHMS.logout();
```

### Request Managed Products

```javascript
sdkbox.PluginHMS.iapRequestProducts();
```
this method will trigger `onIAPProducts` event

### Purchase Managed Product

```javascript
sdkbox.PluginHMS.iapPurchase("coin");
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
sdkbox.PluginHMS.iapPurchaseWithPrice(JSON.stringify(productInfo));
```
this method will trigger `onIAPPurchase` event

### request owned purchase

will return current user own products, include non-consumable, subscription product and consumable product which have not be consumed.

```javascript
sdkbox.PluginHMS.iapRequestOwnedPurchases();
```
this method will trigger `onIAPOwnedPurchases` event

### consume product

```javascript
sdkbox.PluginHMS.iapConsume(purchaseToken);
```
this method will trigger `onIAPPConsume` event

### request owned purchase record

request current user's all purchase records.
```javascript
sdkbox.PluginHMS.iapRequestOwnedPurchaseRecords(purchaseToken);
```
this method will trigger `onIAPOwnedPurchaseRecords` event

### Player Info

#### GetPlayer Info

will trigger listener event `onPlayerInfo`
```javascript
sdkbox.PluginHMS.playerRequestInfo();
```

#### GetPlayer ExtraInfo

Will return follow info of current player: isadult, playtime and so on
will trigger listener event `onPlayerExtraInfo`
```javascript
sdkbox.PluginHMS.playerRequestInfo();
```

#### Submit GameBegin

submit player game begin event. if your game will sell in china, you should submit game begin event.
will trigger listener event `onPlayerGameBegin`
```javascript
sdkbox.PluginHMS.playerSubmitGameBegin();
```

#### Submit GameEnd

submit player game begin event. if your game will sell in china, you should submit game end event.

will trigger listener event `onPlayerGameEnd`

```javascript
sdkbox.PluginHMS.playerSubmitGameEnd();
```

### Achievement

#### Request Achievement List

request achivement list, then you can show achievement list by yourself

will trigger listener event `onAchievementList`

```javascript
sdkbox.PluginHMS.achievementRequestList();
```

#### AchievementShow

show achivement with hms default ui

will trigger listener event `onAchievementShow`

```javascript
sdkbox.PluginHMS.achievementShow();
```

#### achievementVisualize

will trigger listener event `onAchievementVisualize`
```javascript
sdkbox.PluginHMS.achievementVisualize();
```

#### achievementGrow

will trigger listener event `onAchievementGrow`
```javascript
sdkbox.PluginHMS.achievementGrow();
```

#### achievementMakeSteps

will trigger listener event `onAchievementMakeSteps`
```javascript
sdkbox.PluginHMS.achievementMakeSteps();
```

#### achievementReach

```javascript
sdkbox.PluginHMS.achievementReach();
```

### Event

#### eventGrow

```javascript
sdkbox.PluginHMS.eventGrow();
```

#### eventRequestList

will trigger listener event `onEventList`
```javascript
sdkbox.PluginHMS.eventRequestList();
```

### Ranking

#### Check ranking switch status

before invoke ranking related api, you must make sure player is allow to open score.

will trigger listener event `onRankingSwitchStatus`
```javascript
sdkbox.PluginHMS.rankingRequestSwitchStatus();
```

will trigger listener event `onRankingSetSwitchStatus`
```javascript
sdkbox.PluginHMS.rankingSetSwitchStatus();
```

#### submit score

will trigger listener event `onRankingSubmitScore`

```javascript
sdkbox.PluginHMS.rankingSubmitScore(rankingName, score, score_unit);
```

#### Show ranking

show ranking by self.

will trigger listener event `onRankingList`

```javascript
const realtime = true; // true, will request data from hms server; false, will use local cache data
sdkbox.PluginHMS.rankingRequestList(realtime, rankingName);
```

show with hms default ui

will trigger listener event `onRankingShow`

```javascript
const timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS.rankingShow(timeDimension, rankingName);
```

#### get scores

current player score

will trigger listener event `onRankingCurPlayerScore`

```javascript
const timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS.rankingRequestCurPlayerScore(rankingName, timeDimension);
```

request player centered score

will trigger listener event `onRankingPlayerCenteredScores`

```javascript
const timeDimension = 2; // 0-> day, 1-> week, 2-> all time
sdkbox.PluginHMS.rankingRequestPlayerCenteredScores(rankingName, timeDimension, realtime);
```

### Archive

add archive

will trigger listener event `onArchiveAdd`

```javascript
const bmBytes; // Uint8Array, cover image data
const dataBytes; // Uint8Array, archive binary data

sdkbox.PluginHMS.archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesType,
                               dataBytes);
```

update archive

will trigger listener event `onArchiveUpdate`

```javascript
const bmBytes; // Uint8Array, cover image data
const dataBytes; // Uint8Array, archive binary data

sdkbox.PluginHMS.archiveUpdate(archiveId,
                          playedTime, progress, description,
                          bmBytes, bmBytesType,
                          dataBytes);
```

load archive

will trigger listener event `onArchiveLoad`

```javascript
const conflictPolicy = 3;
//-1 -> hms willn't hand conflict, 
//1  -> hms will resolved conflict by played time, 
//2  -> hms will resolved conflict by progress,
//3  -> hms will resolved conflict by last update time
sdkbox.PluginHMS.archiveLoad(archiveId, conflictPolicy);
```

### BUOY

if you game sell in china, you should show buoy
```javascript
sdkbox.PluginHMS.buoyShow();
//or
sdkbox.PluginHMS.buoyHide();
```

### Advertisement

caceh ad

```javascript
sdkbox.PluginHMS.adCache(adName);
```

show ad

```javascript
if (sdkbox.PluginHMS.adIsAvailable(adName)) {
    sdkbox.PluginHMS.adShow(adName);
}
```

hide banner

```javascript
sdkbox.PluginHMS.adHide(adName);
```

ad request settings (Optional)

```javascript
/*
  * adContentClassification:
  *   "W"->Content suitable for toddlers and older audiences;
  *  "PI"->Content suitable for kids and older audiences
  *   "J"->Content suitable for teenagers and older audiences.
  *   "A"->Content suitable only for adults.
  *    ""->Unknown rating.
  */
sdkbox.PluginHMS.adSetAdContentClassification("A");

/*
  * tagForUnderAgeOfPromise:
  *  0->Do not process ad requests as directed to users under the age of consent;
  *  1->Process ad requests as directed to users under the age of consent;
  * -1->Whether to process ad requests as directed to users under the age of consent is not specified;
  */
sdkbox.PluginHMS.adSetTagForUnderAgeOfPromise(0);

/*
* tagForChildProtection:
*  0->Do not process ad requests according to the COPPA;
*  1->Process ad requests according to the COPPA;
* -1->Whether to process ad requests according to the COPPA is not specified;
*/
sdkbox.PluginHMS.adSetTagForChildProtection(0);

/*
* nonPersonalizedAd
*  0->Request both personalized and non-personalized ads (default);
*  1->Request only non-personalized ads;
*/
sdkbox.PluginHMS.adSetNonPersonalizedAd(0);
```

reward ad setting (Optional)

reward data must be URL-encoded and length must be less than 1024

```javascript
// reward ad custom data
sdkbox.PluginHMS.adSetRewardData("cdata");

// uid for reward ad
sdkbox.PluginHMS.adSetRewardUserId("uid666");
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


```Javascript
sdkbox.PluginHMS.setListener({
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

    // Ad
    onAdClose(code, errorOrJson) {
    }

    onAdFail(code, errorOrJson) {
    }

    onAdLeave(code, errorOrJson) {
    }

    onAdOpen(code, errorOrJson) {
    }

    onAdLoad(code, errorOrJson) {
    }

    onAdClick(code, errorOrJson) {
    }

    onAdImpression(code, errorOrJson) {
    }

    onAdReward(code, errorOrJson) {
    }

});
```
