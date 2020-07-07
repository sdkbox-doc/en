## API Reference

### Methods
```javascript
sdkbox.PluginHMS.setGDPR(enabled);
```
> Set GDPR

```javascript
sdkbox.PluginHMS.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginHMS.setListener(listener);
```
> Set listener to listen for adcolony events

```javascript
sdkbox.PluginHMS.login(loginType);
```
> HMS provider three way to login
loginType: 0, slient login 1, login with HuaweiID(ID Token) 2, login with HuaweID(Authorization Code)

```javascript
sdkbox.PluginHMS.logout();
```
> logout HMS

```javascript
sdkbox.PluginHMS.playerRequestInfo();
```
> request current player info

```javascript
sdkbox.PluginHMS.playerRequestExtraInfo();
```
> request player extra info

```javascript
sdkbox.PluginHMS.playerSubmitGameBegin();
```
> submit game begin event

```javascript
sdkbox.PluginHMS.playerSubmitGameEnd();
```
> submit game end event

```javascript
sdkbox.PluginHMS.iapRequestProducts();
```

```javascript
sdkbox.PluginHMS.iapPurchase(name);
```

```javascript
sdkbox.PluginHMS.iapPurchaseWithPrice(productJson);
```

```javascript
sdkbox.PluginHMS.iapRequestOwnedPurchases();
```

```javascript
sdkbox.PluginHMS.iapConsume(purchaseToken);
```

```javascript
sdkbox.PluginHMS.iapRequestOwnedPurchaseRecords();
```

```javascript
sdkbox.PluginHMS.achievementRequestList();
```

```javascript
sdkbox.PluginHMS.achievementShow();
```

```javascript
sdkbox.PluginHMS.achievementVisualize(name);
```

```javascript
sdkbox.PluginHMS.achievementGrow(achiveName, steps);
```

```javascript
sdkbox.PluginHMS.achievementMakeSteps(achiveName, steps);
```

```javascript
sdkbox.PluginHMS.achievementReach(achiveName);
```

```javascript
sdkbox.PluginHMS.eventGrow(eventName, amount);
```

```javascript
sdkbox.PluginHMS.eventRequestList(realtime, eventNamas);
```

```javascript
sdkbox.PluginHMS.rankingRequestSwitchStatus();
```
> request if player allow open score in ranking

```javascript
sdkbox.PluginHMS.rankingSetSwitchStatus(status);
```
> request if player allow open score in ranking
status: 0->player allow submit score, 1->player not allow submit score

```javascript
sdkbox.PluginHMS.rankingSubmitScore(rankingName, score, unit);
```
> submit score to ranking

```javascript
sdkbox.PluginHMS.rankingShow(timeDimension, rankingName);
```
> use hms's ui to show ranking

```javascript
sdkbox.PluginHMS.rankingRequestList(realtime, rankingName);
```
> request ranking list

```javascript
sdkbox.PluginHMS.rankingRequestCurPlayerScore(rankingName, timeDimension);
```
> request current player ranking score

```javascript
sdkbox.PluginHMS.rankingRequestPlayerCenteredScores(rankingName,
                                                     timeDimension,
                                                     size,
                                                     realtime);
```
> request player centered scores

```javascript
sdkbox.PluginHMS.rankingRequestMoreScores(rankingName,
                                           timeDimension,
                                           offset,
                                           pageSize,
                                           pageDirection);
```
> request more scores

```javascript
sdkbox.PluginHMS.rankingRequestTopScores(rankingName,
                                          timeDimension,
                                          offset,
                                          pageSize,
                                          pageDirection);
```
> submit score to ranking

```javascript
sdkbox.PluginHMS.archiveRequestLimitThumbnailSize();
```
> get thumbnail max size

```javascript
sdkbox.PluginHMS.archiveRequestLimitDetailsSize();
```
> get detail max size

```javascript
sdkbox.PluginHMS.archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesType,
                               dataBytes)
```
> add archive
> bmBytes: Uint8Array, cover image data
> dataBytes: Uint8Array, archive data

```javascript
sdkbox.PluginHMS.archiveShow(title, allowAdd, allowDelete, pageSize);
```
> use hms's default ui to show archive

```javascript
sdkbox.PluginHMS.archiveRequestSummaryList(realtime);
```
> request archive summay list, developer can show custome archive list with the returned data

```javascript
sdkbox.PluginHMS.archiveRequestThumbnail(archiveId);
```
> request archive cover thumbnail

```javascript
sdkbox.PluginHMS.archiveUpdate(archiveId,
                               playedTime, progress, description, supportCache,
                               bmBytes, bmBytesType,
                               dataBytes)
```
> update archive
> bmBytes: Uint8Array, cover image data
> dataBytes: Uint8Array, archive data

```javascript
sdkbox.PluginHMS.archiveLoad(archiveId, conflictPolicy);
```
> load archive

```javascript
sdkbox.PluginHMS.archiveRemove(archiveId);
```
> remvoe archive

```javascript
sdkbox.PluginHMS.gamePlayerStatsRequest(realtime);
```
> request game player statistics

```javascript
sdkbox.PluginHMS.gameSummaryRequest(realtime);
```
> request game summary

```javascript
sdkbox.PluginHMS.buoyShow();
```

```javascript
sdkbox.PluginHMS.buoyHide();
```

```javascript
sdkbox.PluginHMS.adCache(name);
```

```javascript
sdkbox.PluginHMS.adShow(name);
```

```javascript
sdkbox.PluginHMS.adHide(name);
```

```javascript
sdkbox.PluginHMS.adIsAvailable(name);
```

```javascript
sdkbox.PluginHMS.adSetRewardData(custom_data);
```

```javascript
sdkbox.PluginHMS.adSetRewardUserId(user_id);
```

```javascript
sdkbox.PluginHMS.adSetAdContentClassification(adContentClassification);
```

```javascript
sdkbox.PluginHMS.adSetTagForUnderAgeOfPromise(tagForUnderAgeOfPromise);
```

```javascript
sdkbox.PluginHMS.adSetTagForChildProtection(tagForChildProtection);
```

```javascript
sdkbox.PluginHMS.adSetNonPersonalizedAd(nonPersonalizedAd);
```


### Listeners
```javascript
onLogin(code, errorOrJson);
```

```javascript
onPlayerInfo(code, errorOrJson);
```

```javascript
onPlayerExtraInfo(code, errorOrJson);
```

```javascript
onPlayerGameBegin(code, errorOrJson);
```

```javascript
onPlayerGameEnd(code, errorOrJson);
```

```javascript
onIAPReady(code, errorOrJson);
```

```javascript
onIAPProducts(code, errorOrJson);
```

```javascript
onIAPPurchase(code, errorOrJson);
```

```javascript
onIAPConsume(code, errorOrJson);
```

```javascript
onIAPOwnedPurchases(code, errorOrJson);
```

```javascript
onIAPOwnedPurchaseRecords(code, errorOrJson);
```

```javascript
onAchievementList(code, errorOrJson);
```

```javascript
onAchievementShow(code, errorOrJson);
```

```javascript
onAchievementVisualize(code, errorOrJson);
```

```javascript
onAchievementGrow(code, errorOrJson);
```

```javascript
onAchievementMakeSteps(code, errorOrJson);
```

```javascript
onEventList(code, errorOrJson);
```

```javascript
onRankingSwitchStatus(code, errorOrJson);
```

```javascript
onRankingSetSwitchStatus(code, errorOrJson);
```

```javascript
onRankingSubmitScore(code, errorOrJson);
```
> callback for rankingSubmitScore

```javascript
onRankingShow(code, errorOrJson);
```
> callback for rankingShow

```javascript
onRankingList(code, errorOrJson);
```
> callback for rankingRequestList

```javascript
onRankingCurPlayerScore(code, errorOrJson);
```
> callback for rankingRequestCurPlayerScore

```javascript
onRankingPlayerCenteredScores(code, errorOrJson);
```
> callback for rankingRequestPlayerCenteredScores

```javascript
onRankingMoreScores(code, errorOrJson);
```
> callback for rankingRequestMoreScores

```javascript
onRankingTopScores(code, errorOrJson);
```
> callback for rankingRequestTopScores

```javascript
onArchiveLimitThumbnailSize(code, errorOrJson);
```
> callback for archiveRequestLimitThumbnailSize

```javascript
onArchiveLimitDetailsSize(code, errorOrJson);
```
> callback for archiveRequestLimitDetailsSize

```javascript
onArchiveAdd(code, errorOrJson);
```
> callback for archiveAdd

```javascript
onArchiveShow(code, errorOrJson);
```
> callback for archiveShow

```javascript
onArchiveSummaryList(code, errorOrJson);
```
> callback for archiveRequestSummaryList

```javascript
onArchiveSelect(code, errorOrJson);
```
> callback when user select archive

```javascript
onArchiveThumbnail(code, errorOrJson, coverData, coverDataLen);
```
> callback for archiveRequestThumbnail

```javascript
onArchiveUpdate(code, errorOrJson);
```
> callback for archiveUpdate

```javascript
onArchiveLoad(code, errorOrJson, contentData, contentDataLen);
```
> callback for archiveLoad

```javascript
onArchiveRemove(code, errorOrJson);
```
> callback for archiveRemove

```javascript
onGamePlayerStats(code, errorOrJson);
```
> callback for gamePlayerStatsRequest

```javascript
onGameSummary(code, errorOrJson);
```
> callback for gameSummaryRequest

```javascript
onAdClose(code, errorOrJson);
```

```javascript
onAdFail(code, errorOrJson);
```

```javascript
onAdLeave(code, errorOrJson);
```

```javascript
onAdOpen(code, errorOrJson);
```

```javascript
onAdLoad(code, errorOrJson);
```

```javascript
onAdClick(code, errorOrJson);
```

```javascript
onAdImpression(code, errorOrJson);
```

```javascript
onAdReward(code, errorOrJson);
```


