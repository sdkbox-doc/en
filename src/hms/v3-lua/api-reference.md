## API Reference

### Methods
```lua
sdkbox.PluginHMS:setGDPR(enabled)
```
> Set GDPR

```lua
sdkbox.PluginHMS:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginHMS:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginHMS:login(loginType)
```
> HMS provider three way to login
loginType: 0, slient login 1, login with HuaweiID(ID Token) 2, login with HuaweID(Authorization Code)

```lua
sdkbox.PluginHMS:logout()
```
> logout HMS

```lua
sdkbox.PluginHMS:playerRequestInfo()
```
> request current player info

```lua
sdkbox.PluginHMS:playerRequestExtraInfo()
```
> request player extra info

```lua
sdkbox.PluginHMS:playerSubmitGameBegin()
```
> submit game begin event

```lua
sdkbox.PluginHMS:playerSubmitGameEnd()
```
> submit game end event

```lua
sdkbox.PluginHMS:iapRequestProducts()
```

```lua
sdkbox.PluginHMS:iapPurchase(name)
```

```lua
sdkbox.PluginHMS:iapPurchaseWithPrice(productJson)
```

```lua
sdkbox.PluginHMS:iapRequestOwnedPurchases()
```

```lua
sdkbox.PluginHMS:iapConsume(purchaseToken)
```

```lua
sdkbox.PluginHMS:iapRequestOwnedPurchaseRecords()
```

```lua
sdkbox.PluginHMS:achievementRequestList()
```

```lua
sdkbox.PluginHMS:achievementShow()
```

```lua
sdkbox.PluginHMS:achievementVisualize(name)
```

```lua
sdkbox.PluginHMS:achievementGrow(achiveName, steps)
```

```lua
sdkbox.PluginHMS:achievementMakeSteps(achiveName, steps)
```

```lua
sdkbox.PluginHMS:achievementReach(achiveName)
```

```lua
sdkbox.PluginHMS:eventGrow(eventName, amount)
```

```lua
sdkbox.PluginHMS:eventRequestList(realtime, eventNamas)
```

```lua
sdkbox.PluginHMS:rankingRequestSwitchStatus()
```
> request if player allow open score in ranking

```lua
sdkbox.PluginHMS:rankingSetSwitchStatus(status)
```
> request if player allow open score in ranking
status: 0->player allow submit score, 1->player not allow submit score

```lua
sdkbox.PluginHMS:rankingSubmitScore(rankingName, score, unit)
```
> submit score to ranking

```lua
sdkbox.PluginHMS:rankingShow(timeDimension, rankingName)
```
> use hms's ui to show ranking

```lua
sdkbox.PluginHMS:rankingRequestList(realtime, rankingName)
```
> request ranking list

```lua
sdkbox.PluginHMS:rankingRequestCurPlayerScore(rankingName, timeDimension)
```
> request current player ranking score

```lua
sdkbox.PluginHMS:rankingRequestPlayerCenteredScores(rankingName,
                                                     timeDimension,
                                                     size,
                                                     realtime)
```
> request player centered scores

```lua
sdkbox.PluginHMS:rankingRequestMoreScores(rankingName,
                                           timeDimension,
                                           offset,
                                           pageSize,
                                           pageDirection)
```
> request more scores

```lua
sdkbox.PluginHMS:rankingRequestTopScores(rankingName,
                                          timeDimension,
                                          offset,
                                          pageSize,
                                          pageDirection)
```
> submit score to ranking

```lua
sdkbox.PluginHMS:archiveRequestLimitThumbnailSize()
```
> get thumbnail max size

```lua
sdkbox.PluginHMS:archiveRequestLimitDetailsSize()
```
> get detail max size

```lua
sdkbox.PluginHMS:archiveAdd(playedTime, progress, description, supportCache,
                               bmBytes, bmBytesType,
                               dataBytes)
```
> add archive
> bmBytes: cover image data
> dataBytes: archive data

```lua
sdkbox.PluginHMS:archiveShow(title, allowAdd, allowDelete, pageSize)
```
> use hms's default ui to show archive

```lua
sdkbox.PluginHMS:archiveRequestSummaryList(realtime)
```
> request archive summay list, developer can show custome archive list with the returned data

```lua
sdkbox.PluginHMS:archiveRequestThumbnail(archiveId)
```
> request archive cover thumbnail

```lua
sdkbox.PluginHMS:archiveUpdate(archiveId,
                               playedTime, progress, description, supportCache,
                               bmBytes, bmBytesType,
                               dataBytes)
```
> update archive
> bmBytes: cover image data
> dataBytes: archive data

```lua
sdkbox.PluginHMS:archiveLoad(archiveId, conflictPolicy)
```
> load archive

```lua
sdkbox.PluginHMS:archiveRemove(archiveId)
```
> remvoe archive

```lua
sdkbox.PluginHMS:gamePlayerStatsRequest(realtime)
```
> request game player statistics

```lua
sdkbox.PluginHMS:gameSummaryRequest(realtime)
```
> request game summary

```lua
sdkbox.PluginHMS:buoyShow()
```

```lua
sdkbox.PluginHMS:buoyHide()
```

```lua
sdkbox.PluginHMS:adCache(name)
```

```lua
sdkbox.PluginHMS:adShow(name)
```

```lua
sdkbox.PluginHMS:adHide(name)
```

```lua
sdkbox.PluginHMS:adIsAvailable(name)
```

```lua
sdkbox.PluginHMS:adSetRewardData(custom_data)
```

```lua
sdkbox.PluginHMS:adSetRewardUserId(user_id)
```

```lua
sdkbox.PluginHMS:adSetAdContentClassification(adContentClassification)
```

```lua
sdkbox.PluginHMS:adSetTagForUnderAgeOfPromise(tagForUnderAgeOfPromise)
```

```lua
sdkbox.PluginHMS:adSetTagForChildProtection(tagForChildProtection)
```

```lua
sdkbox.PluginHMS:adSetNonPersonalizedAd(nonPersonalizedAd)
```


### Listeners
```lua
onLogin(code, errorOrJson)
```

```lua
onPlayerInfo(code, errorOrJson)
```

```lua
onPlayerExtraInfo(code, errorOrJson)
```

```lua
onPlayerGameBegin(code, errorOrJson)
```

```lua
onPlayerGameEnd(code, errorOrJson)
```

```lua
onIAPReady(code, errorOrJson)
```

```lua
onIAPProducts(code, errorOrJson)
```

```lua
onIAPPurchase(code, errorOrJson)
```

```lua
onIAPConsume(code, errorOrJson)
```

```lua
onIAPOwnedPurchases(code, errorOrJson)
```

```lua
onIAPOwnedPurchaseRecords(code, errorOrJson)
```

```lua
onAchievementList(code, errorOrJson)
```

```lua
onAchievementShow(code, errorOrJson)
```

```lua
onAchievementVisualize(code, errorOrJson)
```

```lua
onAchievementGrow(code, errorOrJson)
```

```lua
onAchievementMakeSteps(code, errorOrJson)
```

```lua
onEventList(code, errorOrJson)
```

```lua
onRankingSwitchStatus(code, errorOrJson)
```

```lua
onRankingSetSwitchStatus(code, errorOrJson)
```

```lua
onRankingSubmitScore(code, errorOrJson)
```
> callback for rankingSubmitScore

```lua
onRankingShow(code, errorOrJson)
```
> callback for rankingShow

```lua
onRankingList(code, errorOrJson)
```
> callback for rankingRequestList

```lua
onRankingCurPlayerScore(code, errorOrJson)
```
> callback for rankingRequestCurPlayerScore

```lua
onRankingPlayerCenteredScores(code, errorOrJson)
```
> callback for rankingRequestPlayerCenteredScores

```lua
onRankingMoreScores(code, errorOrJson)
```
> callback for rankingRequestMoreScores

```lua
onRankingTopScores(code, errorOrJson)
```
> callback for rankingRequestTopScores

```lua
onArchiveLimitThumbnailSize(code, errorOrJson)
```
> callback for archiveRequestLimitThumbnailSize

```lua
onArchiveLimitDetailsSize(code, errorOrJson)
```
> callback for archiveRequestLimitDetailsSize

```lua
onArchiveAdd(code, errorOrJson)
```
> callback for archiveAdd

```lua
onArchiveShow(code, errorOrJson)
```
> callback for archiveShow

```lua
onArchiveSummaryList(code, errorOrJson)
```
> callback for archiveRequestSummaryList

```lua
onArchiveSelect(code, errorOrJson)
```
> callback when user select archive

```lua
onArchiveThumbnail(code, errorOrJson, coverData, coverDataLen)
```
> callback for archiveRequestThumbnail

```lua
onArchiveUpdate(code, errorOrJson)
```
> callback for archiveUpdate

```lua
onArchiveLoad(code, errorOrJson, contentData, contentDataLen)
```
> callback for archiveLoad

```lua
onArchiveRemove(code, errorOrJson)
```
> callback for archiveRemove

```lua
onGamePlayerStats(code, errorOrJson)
```
> callback for gamePlayerStatsRequest

```lua
onGameSummary(code, errorOrJson)
```
> callback for gameSummaryRequest

```lua
onAdClose(code, errorOrJson)
```

```lua
onAdFail(code, errorOrJson)
```

```lua
onAdLeave(code, errorOrJson)
```

```lua
onAdOpen(code, errorOrJson)
```

```lua
onAdLoad(code, errorOrJson)
```

```lua
onAdClick(code, errorOrJson)
```

```lua
onAdImpression(code, errorOrJson)
```

```lua
onAdReward(code, errorOrJson)
```


