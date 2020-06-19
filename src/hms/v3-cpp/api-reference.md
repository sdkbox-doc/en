## API Reference

### Methods
```cpp
static void setGDPR ( bool enabled ) ;
```
> Set GDPR

```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( HMSListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static HMSListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void login ( int loginType ) ;
```
> HMS provider three way to login
loginType: 0, slient login 1, login with HuaweiID(ID Token) 2, login with HuaweID(Authorization Code)

```cpp
static void logout ( ) ;
```
> logout HMS

```cpp
static void playerRequestInfo ( ) ;
```
> request current player info

```cpp
static void playerRequestExtraInfo ( ) ;
```
> request player extra info

```cpp
static void playerSubmitGameBegin ( ) ;
```
> submit game begin event

```cpp
static void playerSubmitGameEnd ( ) ;
```
> submit game end event

```cpp
static void iapRequestProducts ( ) ;
```

```cpp
static void iapPurchase ( const std::string & name ) ;
```

```cpp
static void iapPurchaseWithPrice ( const std::string & productJson ) ;
```

```cpp
static void iapRequestOwnedPurchases ( ) ;
```

```cpp
static void iapConsume ( const std::string & purchaseToken ) ;
```

```cpp
static void iapRequestOwnedPurchaseRecords ( ) ;
```

```cpp
static void achievementRequestList ( ) ;
```

```cpp
static void achievementShow ( ) ;
```

```cpp
static void achievementVisualize ( const std::string & name ) ;
```

```cpp
static void achievementGrow ( const std::string & achiveName , int steps ) ;
```

```cpp
static void achievementMakeSteps ( const std::string & achiveName ,
                                   int steps ) ;
```

```cpp
static void achievementReach ( const std::string & achiveName ) ;
```

```cpp
static void eventGrow ( const std::string & eventName , int amount ) ;
```

```cpp
static void eventRequestList ( bool realtime ,
                               const std::string & eventNamas = "" ) ;
```

```cpp
static void rankingRequestSwitchStatus ( ) ;
```
> request if player allow open score in ranking

```cpp
static void rankingSetSwitchStatus ( int status ) ;
```
> request if player allow open score in ranking
status: 0->player allow submit score, 1->player not allow submit score

```cpp
static void rankingSubmitScore ( const std::string & rankingName ,
                                 long score ,
                                 const std::string unit = "" ) ;
```
> submit score to ranking

```cpp
static void rankingShow ( int timeDimension ,
                          const std::string & rankingName = "" ) ;
```
> use hms's ui to show ranking

```cpp
static void rankingRequestList ( bool realtime ,
                                 const std::string & rankingName = "" ) ;
```
> request ranking list

```cpp
static void rankingRequestCurPlayerScore ( const std::string & rankingName ,
                                           int timeDimension ) ;
```
> request current player ranking score

```cpp
static void rankingRequestPlayerCenteredScores ( const std::string & rankingName ,
                                                 int timeDimension ,
                                                 int size ,
                                                 bool realtime ) ;
```
> request player centered scores

```cpp
static void rankingRequestMoreScores ( const std::string & rankingName ,
                                       int timeDimension ,
                                       int offset ,
                                       int pageSize ,
                                       int pageDirection ) ;
```
> request more scores

```cpp
static void rankingRequestTopScores ( const std::string & rankingName ,
                                      int timeDimension ,
                                      int offset ,
                                      int pageSize ,
                                      int pageDirection ) ;
```
> submit score to ranking

```cpp
static void archiveRequestLimitThumbnailSize ( ) ;
```
> get thumbnail max size

```cpp
static void archiveRequestLimitDetailsSize ( ) ;
```
> get detail max size

```cpp
static void archiveAdd ( long playedTime ,
                         long progress ,
                         const std::string & description ,
                         bool supportCache ,
                         const unsigned char * bmBytes ,
                         int bmBytesLen ,
                         const std::string & bmBytesType ,
                         const unsigned char * dataBytes ,
                         int dataBytesLen ) ;
```
> add archive

```cpp
static void archiveShow ( const std::string & title ,
                          bool allowAdd ,
                          bool allowDelete ,
                          int pageSize ) ;
```
> use hms's default ui to show archive

```cpp
static void archiveRequestSummaryList ( bool realtime ) ;
```
> request archive summay list, developer can show custome archive list with the returned data

```cpp
static void archiveRequestThumbnail ( const std::string & archiveId ) ;
```
> request archive cover thumbnail

```cpp
static void archiveUpdate ( const std::string & archiveId ,
                            long playedTime ,
                            long progress ,
                            const std::string & description ,
                            const unsigned char * bmBytes ,
                            int bmBytesLen ,
                            const std::string & bmBytesType ,
                            const unsigned char * dataBytes ,
                            int dataBytesLen ) ;
```
> update archive

```cpp
static void archiveLoad ( const std::string & archiveId , int conflictPolicy ) ;
```
> load archive

```cpp
static void archiveRemove ( const std::string & archiveId ) ;
```
> remvoe archive

```cpp
static void gamePlayerStatsRequest ( bool realtime ) ;
```
> request game player statistics

```cpp
static void gameSummaryRequest ( bool realtime ) ;
```
> request game summary

```cpp
static void buoyShow ( ) ;
```

```cpp
static void buoyHide ( ) ;
```


### Listeners
```cpp
void onLogin ( int code , const std::string & errorOrJson );
```

```cpp
void onPlayerInfo ( int code , const std::string & errorOrJson ) {
```

```cpp
void onPlayerExtraInfo ( int code , const std::string & errorOrJson ) {
```

```cpp
void onPlayerGameBegin ( int code , const std::string & errorOrJson ) {
```

```cpp
void onPlayerGameEnd ( int code , const std::string & errorOrJson ) {
```

```cpp
void onIAPReady ( int code , const std::string & errorOrJson ) {
```

```cpp
void onIAPProducts ( int code , const std::string & errorOrJson ) {
```

```cpp
void onIAPPurchase ( int code , const std::string & errorOrJson ) {
```

```cpp
void onIAPPConsume ( int code , const std::string & errorOrJson ) {
```

```cpp
void onIAPOwnedPurchases ( int code , const std::string & errorOrJson ) {
```

```cpp
void onIAPOwnedPurchaseRecords ( int code , const std::string & errorOrJson ) {
```

```cpp
void onAchievementList ( int code , const std::string & errorOrJson ) {
```

```cpp
void onAchievementShow ( int code , const std::string & errorOrJson ) {
```

```cpp
void onAchievementVisualize ( int code , const std::string & errorOrJson ) {
```

```cpp
void onAchievementGrow ( int code , const std::string & errorOrJson ) {
```

```cpp
void onAchievementMakeSteps ( int code , const std::string & errorOrJson ) {
```

```cpp
void onAchievementReach ( int code , const std::string & errorOrJson ) {
```

```cpp
void onEventList ( int code , const std::string & errorOrJson ) {
```

```cpp
void onRankingSwitchStatus ( int code , const std::string & errorOrJson ) {
```

```cpp
void onRankingSetSwitchStatus ( int code , const std::string & errorOrJson ) {
```

```cpp
void onRankingSubmitScore ( int code , const std::string & errorOrJson ) {
```
> callback for rankingSubmitScore

```cpp
void onRankingShow ( int code , const std::string & errorOrJson ) {
```
> callback for rankingShow

```cpp
void onRankingList ( int code , const std::string & errorOrJson ) {
```
> callback for rankingRequestList

```cpp
void onRankingCurPlayerScore ( int code , const std::string & errorOrJson ) {
```
> callback for rankingRequestCurPlayerScore

```cpp
void onRankingPlayerCenteredScores ( int code ,
                                     const std::string & errorOrJson ) {
```
> callback for rankingRequestPlayerCenteredScores

```cpp
void onRankingMoreScores ( int code , const std::string & errorOrJson ) {
```
> callback for rankingRequestMoreScores

```cpp
void onRankingTopScores ( int code , const std::string & errorOrJson ) {
```
> callback for rankingRequestTopScores

```cpp
void onArchiveLimitThumbnailSize ( int code ,
                                   const std::string & errorOrJson ) {
```
> callback for archiveRequestLimitThumbnailSize

```cpp
void onArchiveLimitDetailsSize ( int code , const std::string & errorOrJson ) {
```
> callback for archiveRequestLimitDetailsSize

```cpp
void onArchiveAdd ( int code , const std::string & errorOrJson ) {
```
> callback for archiveAdd

```cpp
void onArchiveShow ( int code , const std::string & errorOrJson ) {
```
> callback for archiveShow

```cpp
void onArchiveSummaryList ( int code , const std::string & errorOrJson ) {
```
> callback for archiveRequestSummaryList

```cpp
void onArchiveSelect ( int code , const std::string & errorOrJson ) {
```
> callback when user select archive

```cpp
void onArchiveThumbnail ( int code ,
                          const std::string & errorOrJson ,
                          unsigned char * coverData ,
                          unsigned int coverDataLen ) {
```
> callback for archiveRequestThumbnail

```cpp
void onArchiveUpdate ( int code , const std::string & errorOrJson ) {
```
> callback for archiveUpdate

```cpp
void onArchiveLoad ( int code ,
                     const std::string & errorOrJson ,
                     unsigned char * contentData ,
                     unsigned int contentDataLen ) {
```
> callback for archiveLoad

```cpp
void onArchiveRemove ( int code , const std::string & errorOrJson ) {
```
> callback for archiveRemove

```cpp
void onGamePlayerStats ( int code , const std::string & errorOrJson ) {
```
> callback for gamePlayerStatsRequest

```cpp
void onGameSummary ( int code , const std::string & errorOrJson ) {
```
> callback for gameSummaryRequest


