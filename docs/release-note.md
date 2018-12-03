# Release Notes

# 2.4.3.0 (?)

## Add
## Upgrade
## Bugfix

1. Review [android.view.WindowManager$BadTokenException crash](https://discuss.cocos2d-x.org/t/unsatisfiedlinkerror-on-released-game/44190/17?u=yinjimmy)


# 2.4.2.0 (20181129)

## Add
1.  Misc Plugin
    1. LocalNotify， [docs here](http://docs.sdkbox.com/en/plugins/misc/v3-cpp/)
2.  Review:
    1. `rateInAppstore` api:

        >use SKStoreReviewController to review, this is default behavior
        >
        >disable will use SKStoreProductViewController to review
        >if use SKStoreReviewController, `onDeclineToRate`, `onRate`,
        >`onRemindLater` will not trigger

3. Share:
    1. `logoutTwitter` api for [this](https://discuss.cocos2d-x.org/t/need-help-twitter-share-why-onsharestate-socialsharestatecancelled-called-right-after-socialsharestatebegin/43754)

## Upgrade
1.  AdMob: iOS 7.35.1 SDK
2.  Documentation:
    1. IAP
    2. SDKBoxPlay
    3. [encrypt and decrypt sdkbox_config.json](http://docs.sdkbox.com/en/qa/crypt-sdkbox-config/)

## Bugfix
1.  AdMob:
    1. fix [`adViewDidDismissScreen` is called twice](https://discuss.cocos2d-x.org/t/admob-android-bug/44621)
2.  IAP-Amazone:
    1.  fix add
        ```
        <receiver android:name="com.amazon.device.iap.ResponseReceiver">
           <intent-filter>
               <action android:name="com.amazon.inapp.purchasing.NOTIFY"  android:permission="com.amazon.inapp.purchasing.Permission.NOTIFY" />
           </intent-filter>
        </receiver>
        ```
        to AndroidManifest.xml again when update plugin.
    2.  fix `enableUserSideVerification`, `isAutoConsume`, `setAutoConsume`,
       `consumeProduct` crash
3.  Review:
    1. Amazon, try market first, then webview
4.  SDKBox-core:
    1. fix android armeabi/armeabi-v7a arch. In pre-release, armeabi folder
       contains armeabi-v7a files, armeabi-v7a folder contains armeabi, maybe fix [UnsatisfiedLinkError on Released Game](https://discuss.cocos2d-x.org/t/unsatisfiedlinkerror-on-released-game/44190)
5.  Facebook:
    1. fix [share callback for iOS](https://developers.facebook.com/docs/ios/troubleshooting#faq_1045833585509347). Follow Facebook's development
      documentation and no longer use postId to determine if sharing is successful.
6.  Appodeal:
    1. fix installer `'android:theme=@@android:style/Theme.Translucent.NoTitleBar.Fullscreen'])`
       should be `'android:theme=@android:style/Theme.Translucent.NoTitleBar.Fullscreen'])`

# 2.4.1.1 Release Notes (20180920)

## Add

1. Android case sensitive folder, `#include "PluginIAP/PluginIAP.h" warning with folder pluginiap/Plugin.h path.`
2. SDKBoxAds: use `cache` instead of `cacheControl`:
    ```
    static void cache(const std::string& ad_unit, const std::string& ad_name);
    static void cacheControl( const std::string& ad_unit, const std::map<std::string, std::string>& cacheOpts );
    ```
3. support creator >= 2.0

## Upgrade

## Bugfix

1.  Amazon:
    1. fix `receipt` and `receiptCipheredPayload`, now `receipt` is json string and  `receiptCipheredPayload` is empty string.
2.  Appodeal:
    1. fix package installer for cocos2d-x 3.17
3.  IAP:
    1. fix [crash issue](https://discuss.cocos2d-x.org/t/sdkbox-iap-problem/43513)
4.  SDKBoxAds:
    1. fix AdMob send load event to SDKBoxAds
5.  Facebook:
    1. fix package installer for cocos2d-x 3.17 and cocos creator 2.0
6.  Google Play Services (GPS):
    1. fix failed on jsb-link creator 2.0, [1](https://discuss.cocos2d-x.org/t/cocos-creator-v2-0-released/43287/48?u=yinjimmy), [2](https://discuss.cocos2d-x.org/t/unable-to-compile-cocoscreator-2-project-android-with-sdkbox-admob/43417)
7.  Fyber:
    1. update [doc](https://discuss.cocos2d-x.org/t/solved-sdkbox-fyber-plugin-issue/43361)
8.  IAP:
    1. android "item already owned"
    2. [android price value](https://discuss.cocos2d-x.org/t/iap-v2-4-0-3-price-value-problem/43319?u=yinjimmy)
9.  Chartboost:
    1. fix cache ad which's not in sdkbox_config.json

## Remove

1. cocos2d-x v2 support

# 2.4.0.3 Release Notes (20180806)

## Add

1. auto add proguard code
2. use gradle when cocos2d-x >= 3.17
3. add `sdkbox::getConfig` and `sdkbox::setConfig`  for [this](http://www.sdkbox.com/answers/question/how-to-get-content-sdkbox_config-is-using/)
4. store sdkbox-gui standalone with [repo](https://github.com/sdkbox/misc), fix [issue1](https://discuss.cocos2d-x.org/t/sdkbox-network-failure-fatal-error/42885/3?u=yinjimmy) [issue2](https://discuss.cocos2d-x.org/t/sdkbox-network-failure-fatal-error/42885/17?u=yinjimmy)
5. unity: add [`setserverid` api](http://www.sdkbox.com/answers/question/unityads-how-to-set-serverid/)

## Upgrade

1. GPG: update android c++ lib to v3.0.1
2. Appodeal: [update to iOS 2.4.4.2-Beta](https://discuss.cocos2d-x.org/t/app-store-rejected-app-because-of-old-yandex-sdk-in-appodeal-plugin/43072)
3. Facebook: [Android 4.34.0](https://discuss.cocos2d-x.org/t/android-facebook-2-4-0-2-dialog-share-error/43003)

## Bugfix

1. IAP:
    1. send init event on Android
    2. fixed [JNI crash](https://discuss.cocos2d-x.org/t/sdkbox-iap-jni-error/37570/15?u=yinjimmy)
    3. fix [purchase subscription on Android](http://www.sdkbox.com/answers/question/error-when-purchasing-recurrent-subscription-android/)

2. Google Play Services (GPS):
    1. fix [multidex](https://discuss.cocos2d-x.org/t/sdkbox-issue-with-gps-services-multidex/42644)

3. SDKBoxPlay:
    1. fix [login error](https://discuss.cocos2d-x.org/t/sdkbox-login-error/42978)
    2. export [`saveGameDataBinary` api to javascript/Lua](https://discuss.cocos2d-x.org/t/sdkboxplay-savegamedatabinary-is-not-a-function/43045)

4. Facebook:
    1. fix [dialog share error](https://discuss.cocos2d-x.org/t/android-facebook-2-4-0-2-dialog-share-error/43003)

5. sdkbox installer:
    1. fix [`update` command generate folder n/a with cocos2d-x 3.17](https://discuss.cocos2d-x.org/t/command-sdkbox-update-generates-folder-n-a-for-cocos2dx-v3-17/42965)

6. GPG:
    1. fix [gpg.d.ts](https://discuss.cocos2d-x.org/t/question-about-gpg-d-ts/42886)


# 2.4.0.2 Release Notes (20180626)

## Add

1. GDPR api:
    1. Chartboost `restrictDataCollection`
    2. UnityAds `setGDPR`
    3. AdColony `setGDPR`
    4. Firebase `resetAnalyticsData` and `setAnalyticsCollectionEnabled`
    5. AdMob `setGDPR`

## Upgrade

1. AdMob: update iOS SDK to 7.31.0

## Bugfix

1. fix installer for cocos2d-lua/Js 3.17
2. remove all std::stringstream


# 2.4.0.1 Release Notes (20180522)

## Upgrade
1. Chartboost SDK to 7.2.0, [issue](https://discuss.cocos2d-x.org/t/sdkbox-2-4-0-0-release-with-gdpr-support/42557/2?u=yinjimmy)

## Bugfix
1. Unity share
2. SDKBoxPlay save games, [issue](https://discuss.cocos2d-x.org/t/loadallgamedata-callback/41750/28?u=yinjimmy)
3. Fix installer for cocos2d-x 3.17, [issue](https://discuss.cocos2d-x.org/t/sdkbox-plugins-failing-import-in-cocos2d-x-3-17-projects/42542)
4. Fix patch for cocos2d-lua >= 3.10
5. AdMob patch creator 1.9 failed, [issue](https://discuss.cocos2d-x.org/t/admob-error-in-cocos-creator-1-9-1/42592)


# 2.4.0.0 Release Notes (20180508)

It's ready for [https://www.eugdpr.org/](https://www.eugdpr.org/)

## Add

1. Ethereum pay (for cocos creator)

## Upgrade

1. AdMob: iOS SDK to 7.30.0
2. Appnext: iOS SDK to 1.9.0
3. Facebook: iOS SDK to 4.32.0
4. UnityAds: iOS SDK to 2.2.0, Android 2.2.1
5. Tune: iOS SDK to 5.1.0, Android 4.9.0
6. Firebase: iOS SDK to 4.13.0
7. Chartboost: iOS SDK to 7.1.2, Android 7.1.0
8. Twitter: iOS SDK to 3.3.0, Android SDK to 3.3.0
9. Apteligent: iOS SDK to 5.7.3, Android SDK to 5.8.10
10. Google Play Service: 12.0.1

# 2.3.17.9 Release Notes (20180410)

## Bugfix

1. Tapcore: fix [intigration](http://discuss.cocos2d-x.org/t/tapcore-intigration-error/42148)

# 2.3.17.8 Release Notes (20180403)

## Add

1. Firebase: add WAKE_LOCK permission
2. Firebase: add SystemConfiguration.framework
3. SDKBoxPlay: add new event onLoadGameData(nullptr, "") as load finish event
4. SDKBoxPlay: add `fetchNames` api

## Bugfix

1. Firebase: fix patch
2. Unity: fix pause and resume event
3. YouTuBe: fix patch for creator jsb2 (from 1.8 version)
4. SDKBoxPlay: fix crash when nothing store in cloud on Android
5. SDKBoxAds: fix `AppDelegate.cpp` patch
6. sdkbox installer: fix jsb-link projec for cocos creator (from 1.8 version)
7. IAP won't consume and it will throw error "item already own" on Android

## Upgrade

1. Facebook: upgrade iOS SDK to 4.31.0

# 2.3.17.7 Release Notes (20180206)

## Highlights

1. Support [Tapcore](http://tapcore.com/?refid=Y3DgX)
2. Upgrade AdColony iOS SDK to 3.3.0 and Android SDK to 3.3.0
3. Upgrade Firebase iOS SDK to 4.8.0
4. Upgrade UnityAds iOS SDK to 2.1.2 and Android SDK to 2.1.2
5. Facebook support [set web login](http://discuss.cocos2d-x.org/t/how-to-set-the-facebook-loginbehavior-fbsdkloginbehaviorweb/40952) with `PluginFacebook::setLoginBehavior(sdkbox::FBSDKLoginBehaviorBrowser);` api
6. We recommend Plugin SDKBoxAds to show ads, and other plugin AdMob, UnityAds etc as its mediation.
   So when you import Plugin AdMob or UnityAds, SDKBoxAds will be import too.

## Bugfix
1. Fix [`requestAllAds` for AdColony Android](http://discuss.cocos2d-x.org/t/adcolony-force-reload-ads-if-internet-gets-enabled/39957)
2. Fix Plugin Facebook callback for creator 1.7+, [issue1](http://discuss.cocos2d-x.org/t/solved-crash-sdkbox-pluginfacebook-after-login-successful-creatorv1-7-android/40849/18), [issue2](http://discuss.cocos2d-x.org/t/solved-crash-sdkbox-pluginfacebook-after-login-successful-creatorv1-7-android/40849), [issue3](http://discuss.cocos2d-x.org/t/solved-facebook-login-logout-game-crash/40912)
3. Fix [SDKBoxPlay apiclient is null](https://github.com/sdkbox/issues/issues/42)
4. Fix [SDKBox crash when call cc.game.restart](https://github.com/sdkbox/sdkbox-core/issues/2664)
5. Fix Appodeal `FailToPresent` event
6. Fix Unity user agreement window

# 2.3.17.6 Release Notes (20171218)

## Highlights

1. Fix [IAP payload is empty when restore on](iOS http://www.sdkbox.com/answers/question/iap-restore-receiptcipheredpayload-is-empty-ios/)
2. Appodeal upgrade Android SDK to 2.1.7
3. Fix [review no callback when click Android *BACK* button or click outside of review UI](http://discuss.cocos2d-x.org/t/sdkbox-review-ratings-android-callbacks/40429)

# 2.3.17.5 Release Notes (20171208)

## Highlights

1. Support Cocos Creator 1.7
2. AdColony supports load all ads again with `requestAllAds` api
3. Appodeal upgrade iOS SDK to 2.1.7



# 2.3.17.3 Release Notes (20171124)
## Highlights

* AdMob upgrade to GoogleMobileAdsSdkiOS-7.26.0, support iPhone X
* iOS suport Promotion IAP
* Installer support 3.16 and Cocos Creator 1.6.2

## Bugfix
* Fix receiptCipheredPayload always null on unity
* Fix IAP price encoding
* Fix IAP clean [iOS system clipboard](http://discuss.cocos2d-x.org/t/sdkbox-iap-remove-clipboard/37087)
* Fix SDKBoxPlay fetch auth code


# 2.3.17 Release Notes (20170926)

## Highlights

* Support Facebook GameRoom
* Unity Review support Amazon Store
* SDKBoxPlay support save binary data
* Upgrade Amazon IAP SDK
* [IAP support finish transaction functionality](https://github.com/sdkbox/issues/issues/21#issuecomment-318951394)
* UnityAds Plugin support SDKBoxAds
* [Chartboost Unreal Plugin support 4.12 - 4.16](https://www.unrealengine.com/marketplace/chartboost-plugin)

## Bugfix

* [Add receipt data when restore products](http://discuss.cocos2d-x.org/t/sdkbox-2-3-11-release-new-push-notification/35658/28)
* SDKBox UI stuck with 404 [issue1](http://forum.cocos.com/t/cocoscreator-macos-sdkbox/49752), [issue2](http://www.sdkbox.com/answers/question/while-trying-to-open-sdkbox-plugin-extension-sdkbox-launch-plugin-try-to-update-itself-and-received-404-error-whats-wrong/)
* [SDKBoxPlay JS submit core crash](http://www.sdkbox.com/answers/question/sdkboxplay-crash-2-3-16-1/)
* [YouTube crash sometimes with nullpointerexception](http://discuss.cocos2d-x.org/t/sdkbox-youtube-crashes-sometimes-with-nullpointerexception-cocos2djs/39091)


2.3.16 Release Notes (20170811)
===

## Highlights

* Support UnityAds
* Support Facebook app event
* Support creator 1.6

## Bugfix

* Fix NDK r14b c++_static
* Fix FlurryAnalytics track wrong app version on iOS
* Fix Firebase does not work on Android 7


2.3.15 Release Notes
===
## Highlights
* Support NDK r14b c++_static
* Support Firebase Analytics module
* Review support amazon platform
* IAP add user ID and purchase token for the purcase calblack [issue](http://www.sdkbox.com/answers/question/amazon-userid-for-receipt-verification/)
* SDKBOX Play disable cloud save as default
* Google Play Services upgrade to 11.0.0
* gpg cpp sdk upgrade to 2.3

## Bugfix
* Fix IAP receipt and receiptCipheredPayload not working for non-consumable on android [issue](http://discuss.cocos2d-x.org/t/sdkbox-2-3-11-release-new-push-notification/35658/15?u=nite)
* Fix IAP crash in IabHelper.getPurchases [issue](https://github.com/sdkbox/issues/issues/11)
* Fix SDKBOX Play fail to connect to Google Play Services [issue](http://discuss.cocos2d-x.org/t/solved-sdboxplay-error-i-sdkboxplay-error-connecting-to-play-services-reason-sign-in-required-4/37639) [issue](http://discuss.cocos2d-x.org/t/solved-sdkboxplay-not-working-after-update/37590)
* Fix SDKBOX Play local reference table overflow [issue](http://discuss.cocos2d-x.org/t/sdkbox-play-error-local-reference-table-overflow/30118)
* Fix SDKBOX Play `removeListener` doesn't work on Android [issue](https://github.com/sdkbox/issues/issues/16)
* Fix fail to patch Cocos2dxActivity.java 3.15.1

2.3.14 Release Notes
===
## Highlights
* SDKBOX Play supports cloud save function for iCloud and Google Play
* SDKBOX Play supports reset function for Achievement and Leaderboard
* SDKBOX Play leaderboard support float point scores
* InMobi supports rewarded ADs
* Support customized build path for CocosCreator project

## Bugfix
* Fix a crash issue with SDKBOX [issue](http://discuss.cocos2d-x.org/t/sdkbox-crash-after-update/36293)
* Fix a crash issue with social share
* Fix google analytics not tracking app version correctly on iOS [issue](http://discuss.cocos2d-x.org/t/google-analytics-using-sdkbox-ios-dosent-tracking-app-version/36152)
* Add new parameters for Facebook gifting [issue](http://discuss.cocos2d-x.org/t/sdkbox-2-3-12-release-admob-reward-video/35867/20?u=nite)
* Fix InMobi onAdAction callback not been triggered [issue](http://discuss.cocos2d-x.org/t/problem-with-sdkboxadslistener-and-inmobi/36347?u=nite)
* Fix crash in IAP [issue](https://github.com/sdkbox/issues/issues/11)
* Fix IAP onCanceled returns empty in a special case [issue](https://github.com/sdkbox/issues/issues/10)
* Fix double value support for SDKBOX Play [issue](https://github.com/sdkbox/issues/issues/9)
* Fix OneSignal setTag crash [issue](http://discuss.cocos2d-x.org/t/pluginonesignal-gettags-bug/36432)

2.3.13 Release Notes
===
## Highlights
* Upgrade Facebook SDK
* Upgrade GPG Framework
* Facebook supports sending/receiving gift

## Bugfix
* load achievement will include achievement names

2.3.12 Release Notes
===
## Highlights
* AdMob reward video support
* Upgrade Appodeal SDK
* Upgrade AdColony SDK
* Upgrade InMobi SDK
* Upgrade Phunware SDK
* Upgrade Chartboost SDK
* SDKBOX Play supports long and float point score

## Bugfix
* Fix build issue for Tune SDK
* Fix SDKBOX Play unlocking achievement callback been called twice [issue](https://github.com/sdkbox/issues/issues/5)
* Fix Appodeal can't play skippable videos [issue](http://sdkbox.com/answers/question/sdkbox-appodeal-skippable-video-is-not-initialized/?show_answer=684#answer_684/%23comment-225)
* Fix AdColony setCustomID [issue](http://sdkbox.com/answers/question/adcolony-customid-callback-url-error)
* Fix Facebook plugin have different text for iOS and Android [issue](http://discuss.cocos2d-x.org/t/facebook-invitefriendswithinviteids-wrong-action-type-on-ios/34599/2)
* Facebook will no longer logout when the app is offline [issue](sdkbox.com/answers/question/bug-android-sdkbox-facebook-auto-logout-when-start-game-without-internet)


Please report any issues to the [issue tracker](https://github.com/sdkbox/issues/issues)

2.3.11 Release Notes
===
## Highlights
* New Advertising Service [Phunware Ads](http://www.sdkbox.com/plugins/phunwareads)
* New PushNotification Service [Phunware Messaging](http://www.sdkbox.com/plugins/phunware_messaging)
* Cocos Creator Plugin will be in the Cocos Creator plugin store
* [Issue tracking for SDKBOX](https://github.com/sdkbox/issues/issues)

## Bugfix
* Fix a bug for AppNext Android
* Fix a bug with SDKBOX Ads weight more than 100, ads won't play

2.3.10 Release Notes
===
## Highlights
* SDKBOX for Cocos Creator Plugin
* Phunware Ads plugin
* Update SDK for Appnext
* [Issue tracking for SDKBOX](https://github.com/sdkbox/issues/issues)

## Bugfix
* Fix Installer error when trying to update multiple plugins
* Fix SDKBOX Ads error when the weights of different ad units is more than 100
* Fix [Facebook request have different text between iOS and Android](http://discuss.cocos2d-x.org/t/facebook-invitefriendswithinviteids-wrong-action-type-on-ios/34599/2)
* Fix [Facebook logout user when offline](http://www.sdkbox.com/answers/question/bug-android-sdkbox-facebook-auto-logout-when-start-game-without-internet/)
* Fix [AdColony getCustomID not working](http://www.sdkbox.com/answers/question/sdkbox-pluginadcolony-setcustomid-check-for-errors/)
* Fix [SDKBOX Play Documentation issues](https://github.com/sdkbox/issues/issues/2)

2.3.9 Release Notes
===
## Highlights
* Add "Designed for families" flag for AdMob
* Upgrade InMobi SDK
* SDKBOX LiveOps supports ATS


2.3.8 Release Notes
===
## Highlights
* IAP plugin will report order id by default
* AdColony SDK update
* Apteligent SDK update
* Appodeal SDK update

## Bugfix
* Fix [Installer time out issue](http://discuss.cocos2d-x.org/t/sdkbox-download-server-connection-problems/33892)
* Fix the cookie issue with sdkbox.com
* Fix [Sdkbox Ads crash](http://www.sdkbox.com/answers/question/app-crash-using-sdkbox-and-admob-plugin-on-iphone7/)
* Fix [pre/post popup for adcolony](http://discuss.cocos2d-x.org/t/sdkbox-adcolony-and-chartboost-bugs/33702)
* Add [native share to js/lua](http://discuss.cocos2d-x.org/t/sdkbox-2-3-7-released-native-share-is-here/33695/9?u=nite)
* Fix [OneSignal missing arm64 for iOS](http://discuss.cocos2d-x.org/t/pluginonesignal-ios-missing-arm64/33811)


2.3.7 Release Notes
===
## Highlights
* [Native share](http://docs.sdkbox.com/en/plugins/share/v3-cpp/#native-share)
* SDKBOX Ads supports adjust ads with weight on LiveOps
* Test and verified SDKBOX with NDK 12
* Remove soomla, vungle plugins
* Merge achievement leaderboard plugin with SDKBOX Play

## Bugfix
* Fix [tune plugin crash](http://discuss.cocos2d-x.org/t/tune-plugin-crash-js/32114/4)
* Fix [Facebook share cancel callback](http://discuss.cocos2d-x.org/t/facebook-plugin-share-issues/33136/3)
* Fix [One signal bug](http://www.sdkbox.com/answers/question/onesignal-notifications_when_activefalse-not-working/)
* Fix [SDKBoxAds shows invalid placement name](http://www.sdkbox.com/answers/question/app-crash-using-sdkbox-and-admob-plugin-on-iphone7/)
* Fix installer caching issue when updating


2.3.6 Release Notes
===
## Highlights
* Support Google Analytics exceptions
* Update SDK for InMobi
* add google access token data to SDKBOX play android

## Bugfix

2.3.5 Release Notes
===
## Highlights
* AdColony 3.0 update (Note: AdColony)

## Bugfix
* Trim ARM x64 build to reduce size

2.3.4 Release Notes
===
## Highlights
* Make sure IAP receipts are always available
* Add `hide()` function to hide banner for SDKBoxAds

## Bugfix
* [Facebook] Fix get user info callback when user login
* [GPG] Fix turn based multiplayer sample for JS
* [LiveOps] Fix a issue happens when user have more than 28 achievements
* [Appodeal] Fix installer for cheetah mobile error


2.3.2 Release Notes
===
## Highlight
* Google Play Game Services plugin enable you to implement a huge array of services with ease in your game.
 * Authorization
 * Achievements
 * Leaderboards
 * Turn-based multiplayer
 * Real-time multiplayer
 * Events and Quests
 * Saved Games
 * Nearby Connections (Android only)
 * Player Statistics
* Add Hide banner functionality to SDKBoxAds
* Upgrade SDK for Appodeal
* Upgrade SDK for Fyber
* Upgrade SDK for AdMob
* Upgrade SDK for Flurry
* Upgrade SDK for Kochava
* Upgrade SDK for AdColony
* Upgrade SDK for AppNext

## Bugfix
* Fix Crashing issue for OneSignal

2.3.1 Release Notes
===
## Highlight
* Add achievement notification control to LiveOps
* Support latest cocos2d-x and Cocos Creator

## Bugfix
* Fix a crashing issue with SDKBoxAds
* Fix setListener on android
* Restore products no longer returns consumables
* Fix SDKBoxplay crash if logged out from google play settings menu
* Fix a crash when finish playing certain InMobi videos
* Support latest cocos2d-x and Cocos Creator
* Fix Facebook callback not triggering when using Facebook share dialog
* Fix a SDKBoxplay crash on iOS when listener was not set
* Fix Appodeal crash when skip videos


2.3.0 Release Notes
===
## Highlight
* SDKBOX installer supports projects created with Cocos Creator 1.2
* SDKBOX play now supports enable/disable achievement popup from GameCenter & Google Play
* Add isAvailable function to SDKBOX Ads to check ads availability
* Fix google security warning for SDKBOX IAP
* SDKBOX IAP Supports restore subscription for Google Play

## Bugfix
* Fix a crash issue for AdMob
* Fix SDKBOX installer issue with windows path that contains spaces
* Fix Appodeal create duplicate records issue during update process
* Fix Chartboost video went black when press home button on android

2.2.5 Release Notes
===
## Highlight
* SDKBOX supports loading encrypted configuration locally
* SDKBOX partially supports cocos creator project, user will still need to copy sdkbox_config.json manually

## Bugfix
* Fix Chartboost crashing issue
* Fix SDKBoxplay JS binding crash issue
* Fix SDKBoxplay onMyScore callback

2.2.4 Release Notes
===
## Highlight
* Share plugin support email
* add new APIs to SDKBoxplay to retrieve player score
* Update Facebook SDK to the latest version
* Update Appodeal to the latest version
* Update Bee7 to the latest version
* Make sure SDKBOX is compliant with google play and iTune store's privacy policy

## Bugfix
* Fix SDKBoxplay keep asking user to login
* Fix SDKBoxplay crash when there is more than 76 achievements
* Fix review plugin crash

2.2.3 Release Notes
===
## Highlight
* AdMob plugin now auto caches ads
* InMobi plugin now can hide banners
* Upgraded google play services to the latest version
* SDKBOX supports loading encrypted configuration locally

## Bugfix
* Fix multiple issue regarding SDKBOX play login
* various documentation fixes

2.2.2 Release Notes
===
## Highlight
* AdMob will automatically cache ads
* New user id related functions in SDKBOX play
* Youtube plugin supports customize close button
* Vungle SDK has been updated
* Appodeal SDK has been updated
* Share plugin supports composing dialog

## Bugfix
* Fix a crashing issue with Facebook
* Fix installer issue with cocos2d-x 3.11

2.2.1 Release Notes
===
## Highlight
* OneSignal plugin for push notification
* update AppNext SDK
* update Vungle android SDK
* update InMobi SDK
* add new AD displaying strategy
* Add Text messaging support for share plugin
* Apteligent plugin now will install a uploading script for your debug symbol files
* Share plugin now supports share dialog

## Bugfix
* Fix installer only updates one plugin
* Fix installer will downgrade android API level
* Fix SDKBOX ads js crash issue
* Fix Facebook crash issue when no Facebook id
* Fix Facebook android sample

2.2 Release Notes
===
## Highlight
* SDKBOX play plugin offers cross platform solution for Leaderboard and achievements
* Apteligent plugin offers crash reporting
* Optimize sample projects makes them take less space
* Facebook plugin supports setting App ID with config file

## Bugfix
* Fix IAP crashing issue when user side verification was set.

2.1.3 Release Notes
===
## Highlight
* Developer can enable/disable a plugin using sdkbox.com
* Share plugin now supports share to Facebook as well
* Facebook Plugin now supports set Facebook App id through config and code
* Updated Appodeal SDK

## Bugfix
* Add JS callback function for Kochava plugin


2.1.2 Release Notes
===
## Highlight
* Update Appodeal SDK
* Update Fyber SDK


## Bugfix
* Fix js binding for cocos2d-x v2
* Fix Appodeal callback for iOS
* Fix Playphone been initialized multiple times

2.1.1 Release Notes
===
## Highlight
* Amazon plugin
* Upgrade Adcolony Android SDK to 2.3.2
* Upgrade Appodeal iOS SDK to 0.9.0
* Upgrade Appodeal Android SDK to 1.14.18

## Bug
* fix SDKBOX update process will stuck in windows shell
* fix a crash with Facebook api call

2.1.0 Release Notes
===
## Highlight
* LeadBolt plugin

## Bug
* SDKBOX update command will not overwrite sdkbox_config.json
* Fix tune plugin not sending correct measure event
* Fix InMobi can't preload ads


2.0.0 Release Notes
===
## Highlight
* SDKBOX LiveOps feature which user can update their SDKBOX config files
* AdMob plugin
* Share plugin with twitter support
* Update Adcolony, Vungle and Appodeal
* provide a lite version of google play service to avoid android's api limitations, check it out [here](https://github.com/darkdukey/Google-Play-Service-Lite)

## Bugfix
* Fix IAP crash when google play service are not initialized correctly
* Fix installer will change Android.mk format bug
* Fix compatibility issue with Reachability project
* Fix InMobi banner settings
* Fix conflicts between Tune and other plugins


1.5.2 Release Notes
===
## Highlight
* Include Google Play Services SDK for needed plugins. No need to install it manually anymore.
* Support the coming Cocos 3.10 release

## Bugfix
*

1.5.1 Release Notes
===
## Highlight
* InMobi plugin
* Update Tune plugin
* Update Appodeal plugin
* Installer will not auto detects projects using c++static library and install correct binary
* Add SDKBOX_ENABLED flag to support projects in other platforms (win, osx, linux)

## Bugfix
* Fix a crash when user attempt purchase in offline mode for IAP plugin.
* Fix generate n/a directory for windows
* Fix a bug that will result android platform have incorrect APP_PLATFORM, and failed to build.


1.5 Release Notes
===
## Highlight
* ScientificRevenue Plugin
* Youtube Plugin
* SDKBOX Installer now support switching different android app stores with `sdkbox set store`
* SDKBOX Installer now supports dependencies between plugins
* Created automatic installation script for installer
* c++static lib support
* Add SDKBOX_ENABLED flag to support projects in other platforms (win, osx, linux)


## Bugfix
* Installer download update to the wrong folder
* remove dependency to ANDROID_SDK_ROOT, installer will find android SDK automatically
* remove dependency to COCOS_CONSOLE_ROOT


1.4.1 Release Notes
===
## Highlight
* Automatic installation script help you setup SDKBOX in a flash
* Update Vungle android SDK to 3.3.3
* Update Appodeal to support rewarded video
* Update tune SDK

## Bugfix
* Fix Facebook invite app link documentation
* Installer will no longer modify osx projects
* Fix Chartboost isAvailable functions
* Fix proguard settings

1.4 Release Notes
===
## Highlight
* [SDKBOX Playphone plugin](http://cocos2d-x.org/sdkbox/playphone)
* [SDKBOX Valuepotion plugin](http://cocos2d-x.org/sdkbox/valuepotion)
* [SDKBOX Appodeal plugin](http://cocos2d-x.org/sdkbox/appodeal)


1.3 Release Notes
===
## Highlight
* New `update` command in sdkbox installer, which will automatically update your SDKBOX integration to the latest version
* [SDKBOX Fyber plugin](http://cocos2d-x.org/sdkbox/fyber)
* [SDKBOX Bee7 plugin](http://cocos2d-x.org/sdkbox/bee7)
* [SDKBOX SOOMLA Grow plugin](http://cocos2d-x.org/sdkbox/soomlagrow)
* [SDKBOX Ratings and Review plugin](http://cocos2d-x.org/sdkbox/ratings_reviews)

## Bugfix
* [Fix Facebook plugin requires login after app restart]()
* [Fix SDKBOX using absolute path for resources]()
* [Fix SDKBOX iap not handling network connection issue]()


1.2.5 Release Notes
===
## Highlight
* we created Review&Rating plugin that developer can use to prompt user to rate their app

## Bugfix
* [Fix Android-Studio integration](http://discuss.cocos2d-x.org/t/sdkbox-v0-5-6-21-android-studio-problem/23866)
* [Fix Vungle isCacheAvailable function](http://stackoverflow.com/questions/31979195/failed-to-find-method-id-of-iscacheavailable-on-vungle-android-because-it-cannot)
* [Fix AdColony failed to get reward](http://discuss.cocos2d-x.org/t/adcolony-sdkbox-cant-get-reward-after-complete-view-video-ads-on-version-1-2-3-3/23600)
* [Plugins can't work together](http://discuss.cocos2d-x.org/t/error-facebook-iap-sdkbox-not-working-together/23851)

1.2.4 Release Notes
===
Fix installer failed to find ANDROID_LIB directory issue

1.2.3 Release Notes
===
## Highlight
* 1.2.3 Fixes some major bugs for the plugins, we strongly recommend updating older versions to 1.2.3

## Bugfix
Sometimes using callbacks will result in sprites show up as black, this is due to invoking cocos2d-x from a different thread
[IAP: item description can't contain newline](http://discuss.cocos2d-x.org/t/solved-google-play-iab-hasnt-been-initilized/22761/21)
[Facebook: missing api function for js/lua binding](http://discuss.cocos2d-x.org/t/sdkbox-facebook-no-api-bug/23414)
[Installer: fix COCOS_CONSOLE_ROOT invalid error](http://discuss.cocos2d-x.org/t/installation-error-for-sdkbox-iap/22898)

## AdColony
#### Changelog
1. Update AdColony iOS SDK to 2.5.3
2. `register_PluginAdColonyLua_helper` -> `register_all_PluginAdColonyLua_helper`
3. `#include "PluginAdColonyLuaHelper.hpp"` -> `#include "PluginAdColonyLuaHelper.h"`
4. `#include "PluginAdColonyJSHelper.hpp"` -> `#include "PluginAdColonyJSHelper.h"`

## AgeCheq
#### Changelog
1. `register_PluginAgeCheqLua_helper` -> `register_all_PluginAgeCheqLua_helper`
2. `#include "PluginAgeCheqLuaHelper.hpp"` -> `#include "PluginAgeCheqLuaHelper.h"`
3. `#include "PluginAgeCheqJSHelper.hpp"` -> `#include "PluginAgeCheqJSHelper.h"`

## Chartboost
#### Changelog
1. `register_PluginChartboostJS_helper` -> `register_all_PluginChartboostJS_helper`
2. `register_PluginChartboostLua_helper` -> `register_all_PluginChartboostLua_helper`
3. Update Chartboost iOS SDK to 5.5.3
4. Update Chartboost Android SDK to 5.5.3
5. `#include "PluginChartboostLuaHelper.hpp"` -> `#include "PluginChartboostLuaHelper.h"`

## Facebook
#### Changelog
1. `register_PluginFacebookJS_helper` -> `register_all_PluginFacebookJS_helper`
2. `register_PluginFacebookLua_helper` -> `register_all_PluginFacebookLua_helper`
3. Update Facebook iOS SDK to 4.5.1
4. Update Facebook Android SDK to 4.5.1
5. `#include "PluginFacebookLuaHelper.hpp"` -> `#include "PluginFacebookLuaHelper.h"`

## Flurry Analytics
#### Changelog
1. `register_PluginFlurryAnalyticsJS_helper` -> `register_all_PluginFlurryAnalyticsJS_helper`
2. `register_PluginFlurryAnalyticsLua_helper` -> `register_all_PluginFlurryAnalyticsLua_helper`
3. Update Flurry iOS SDK to 6.7.0
4. Update Flurry Android SDK to 5.6.0
5. `#include "PluginFlurryAnalyticsLuaHelper.hpp"` -> `#include "PluginFlurryAnalyticsLuaHelper.h"`

## Google Analytics
#### Changelog
1. `#include "PluginGoogleAnalyticsLuaHelper.hpp"` -> `#include "PluginGoogleAnalyticsLuaHelper.h"`

## IAP
#### Changelog
1. `register_PluginIAPLua_helper` -> `register_all_PluginIAPLua_helper`
2. `#include "PluginIAPLuaHelper.hpp"` -> `#include "PluginIAPLuaHelper.h"`
3. `#include "PluginIAPJSHelper.hpp"` -> `#include "PluginIAPJSHelper.h"`

## Tune
#### Changelog
1. `register_PluginTuneJS_helper` -> `register_all_PluginTuneJS_helper`
2. `register_PluginTuneLua_helper` -> `register_all_PluginTuneLua_helper`
3. Update MobileAppTracker Android SDK to 3.10.1
4. `#include "PluginTuneLuaHelper.hpp"` -> `#include "PluginTuneLuaHelper.h"`

## Vungle
#### Changelog
1. `register_PluginVungleJS_helper` -> `register_all_PluginVungleJS_helper`
2. `register_PluginVungleLua_helper` -> `register_all_PluginVungleLua_helper`
3. `#include "PluginVungleLuaHelper.hpp"` -> `#include "PluginVungleLuaHelper.h"`



1.2.2 Release Notes
====
## Highlight
* Installer will automatically modify `Cocos2dxActivity.java` for you
* Facebook Plugin supports `getFriends()` function
* IAP supports `onRestoreComplete()` callback
* IAP will auto consume items if

## Bugfix

[IAP: Item already owned](http://discuss.cocos2d-x.org/t/iap-google-play-buying-product-twice/22842)
[Facebook: FB_PHOTO is not defined] (http://discuss.cocos2d-x.org/t/facebook-fb-photo-is-not-defined/23064)
[Facebook: Facebook plugin failed to work with Cocos2d-js 3.0](http://discuss.cocos2d-x.org/t/sdkbox-facebook-work-well-but-other-plugin-fails-whyy/23043)
[Chartboost: too much recursion](http://discuss.cocos2d-x.org/t/chartboost-listeners-too-much-recursion-on-android/23221/2)

1.2.1 Release Notes
====

## Highlight
[Facebook plugin](http://cocos2d-x.org/sdkbox/facebook) is here.

## Bugfix
[IAP JS crash](http://discuss.cocos2d-x.org/t/sdkbox-iap-for-cocos2d-js-crash-when-onproductrequestsuccess/22814/8)
[IAP crash on devices don't have google play](https://trello.com/c/hm1oZrNA)

1.2.0 Release Notes
===

Release AgeCheq Plugin.
SDKBOX IAP Supports non-consumable
Chinese version of documentation released
Bug fixes

1.1.6 Release Notes
===

SDKBOX now supports install plugin online
SDKBOX online documentation
Upgrade Vugnle SDK to new version
 * iOS: 3.1.2
 * Android: 3.3.1

1.1.5 Release Notes
===

Fix SDKBOX conflicts with Plugin-x

1.1.4 Release Notes
===

Fix SDKBOX IAP plugin return invalid pricing data
