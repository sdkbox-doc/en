#Release Notes
---

1.3 Release Notes
===
##Highlight
* New `update` command in sdkbox installer, which will automatically updates your SDKBOX integration to the latest version
* [SDKBOX Fyber plugin](http://cocos2d-x.org/sdkbox/fyber)
* [SDKBOX Bee7 plugin](http://cocos2d-x.org/sdkbox/bee7)
* [SDKBOX Soomla Grow plugin](http://cocos2d-x.org/sdkbox/soomlagrow)
* [SDKBOX Ratings and Review plugin](http://cocos2d-x.org/sdkbox/ratings_reviews)

##Bugfix
* [Fix facebook plugin requires login after app restart]()
* [Fix SDKBOX using absolute path for resources]()
* [Fix SDKBOX iap not handling network connection issue]()


1.2.5 Release Notes
===
##Highlight
* we created Review&Rating plugin that developer can use to prompt user to rate their app

##Bugfix
* [Fix Android-Studio integration](http://discuss.cocos2d-x.org/t/sdkbox-v0-5-6-21-android-studio-problem/23866)
* [Fix vungle isCacheAvailable function](http://stackoverflow.com/questions/31979195/failed-to-find-method-id-of-iscacheavailable-on-vungle-android-because-it-cannot)
* [Fix AdColony failed to get reward](http://discuss.cocos2d-x.org/t/adcolony-sdkbox-cant-get-reward-after-complete-view-video-ads-on-version-1-2-3-3/23600)
* [Plugins can't work together](http://discuss.cocos2d-x.org/t/error-facebook-iap-sdkbox-not-working-together/23851)

1.2.4 Release Notes
===
Fix installer failed to find ANDROID_LIB directory issue

1.2.3 Release Notes
===
##Highlight
* 1.2.3 Fixes some major bugs for the plugins, we strongly recommend updating older versions to 1.2.3

##Bugfix
Sometimes using callbacks will result in sprites show up as black, this is due to invoking cocos2d-x from a different thread
[IAP: item description can't contain newline](http://discuss.cocos2d-x.org/t/solved-google-play-iab-hasnt-been-initilized/22761/21)
[Facebook: missing api function for js/lua binding](http://discuss.cocos2d-x.org/t/sdkbox-facebook-no-api-bug/23414)
[Installer: fix COCOS_CONSOLE_ROOT invalid error](http://discuss.cocos2d-x.org/t/installation-error-for-sdkbox-iap/22898)

##AdColony
## Changelog
1. Update AdColony iOS SDK to 2.5.3
2. `register_PluginAdColonyLua_helper` -> `register_all_PluginAdColonyLua_helper`
3. `#include "PluginAdColonyLuaHelper.hpp"` -> `#include "PluginAdColonyLuaHelper.h"`
4. `#include "PluginAdColonyJSHelper.hpp"` -> `#include "PluginAdColonyJSHelper.h"`

##AgeCheq
## Changelog
1. `register_PluginAgeCheqLua_helper` -> `register_all_PluginAgeCheqLua_helper`
2. `#include "PluginAgeCheqLuaHelper.hpp"` -> `#include "PluginAgeCheqLuaHelper.h"`
3. `#include "PluginAgeCheqJSHelper.hpp"` -> `#include "PluginAgeCheqJSHelper.h"`

##Chartboost
## Changelog
1. `register_PluginChartboostJS_helper` -> `register_all_PluginChartboostJS_helper`
2. `register_PluginChartboostLua_helper` -> `register_all_PluginChartboostLua_helper`
3. Update Chartboost iOS SDK to 5.5.3
4. Update Chartboost Android SDK to 5.5.3
5. `#include "PluginChartboostLuaHelper.hpp"` -> `#include "PluginChartboostLuaHelper.h"`

##Facebook
## Changelog
1. `register_PluginFacebookJS_helper` -> `register_all_PluginFacebookJS_helper`
2. `register_PluginFacebookLua_helper` -> `register_all_PluginFacebookLua_helper`
3. Update Facebook iOS SDK to 4.5.1
4. Update Facebook Android SDK to 4.5.1
5. `#include "PluginFacebookLuaHelper.hpp"` -> `#include "PluginFacebookLuaHelper.h"`

##Flurry Analytics
## Changelog
1. `register_PluginFlurryAnalyticsJS_helper` -> `register_all_PluginFlurryAnalyticsJS_helper`
2. `register_PluginFlurryAnalyticsLua_helper` -> `register_all_PluginFlurryAnalyticsLua_helper`
3. Update Flurry iOS SDK to 6.7.0
4. Update Flurry Android SDK to 5.6.0
5. `#include "PluginFlurryAnalyticsLuaHelper.hpp"` -> `#include "PluginFlurryAnalyticsLuaHelper.h"`

##Google Analytics
## Changelog
1. `#include "PluginGoogleAnalyticsLuaHelper.hpp"` -> `#include "PluginGoogleAnalyticsLuaHelper.h"`

##IAP
## Changelog
1. `register_PluginIAPLua_helper` -> `register_all_PluginIAPLua_helper`
2. `#include "PluginIAPLuaHelper.hpp"` -> `#include "PluginIAPLuaHelper.h"`
3. `#include "PluginIAPJSHelper.hpp"` -> `#include "PluginIAPJSHelper.h"`

##Tune
1. `register_PluginTuneJS_helper` -> `register_all_PluginTuneJS_helper`
2. `register_PluginTuneLua_helper` -> `register_all_PluginTuneLua_helper`
3. Update MobileAppTracker Android SDK to 3.10.1
4. `#include "PluginTuneLuaHelper.hpp"` -> `#include "PluginTuneLuaHelper.h"`

##Vungle
## Changelog
1. `register_PluginVungleJS_helper` -> `register_all_PluginVungleJS_helper`
2. `register_PluginVungleLua_helper` -> `register_all_PluginVungleLua_helper`
3. `#include "PluginVungleLuaHelper.hpp"` -> `#include "PluginVungleLuaHelper.h"`



1.2.2 Release Notes
====
##Highlight
* Installer will automatically modify `Cocos2dxActivity.java` for you
* Facebook Plugin supports `getFriends()` function
* IAP supports `onRestoreComplete()` callback
* IAP will auto consume items if

##Bugfix

[IAP: Item already owned](http://discuss.cocos2d-x.org/t/iap-google-play-buying-product-twice/22842)
[Facebook: FB_PHOTO is not defined] (http://discuss.cocos2d-x.org/t/facebook-fb-photo-is-not-defined/23064)
[Facebook: Facebook plugin failed to work with Cocos2d-js 3.0](http://discuss.cocos2d-x.org/t/sdkbox-facebook-work-well-but-other-plugin-fails-whyy/23043)
[Chartboost: too much recursion](http://discuss.cocos2d-x.org/t/chartboost-listeners-too-much-recursion-on-android/23221/2)

1.2.1 Release Notes
====

##Highlight
[Facebook plugin](http://cocos2d-x.org/sdkbox/facebook) is here.

##Bugfix
[IAP JS crash](http://discuss.cocos2d-x.org/t/sdkbox-iap-for-cocos2d-js-crash-when-onproductrequestsuccess/22814/8)
[IAP crash on devices don't have google play](https://trello.com/c/hm1oZrNA)

##1.2.0
Release AgeCheq Plugin.
SDKBOX IAP Supports non-consumable
Chinese version of documentation relased
Bug fixes

##1.1.6
SDKBOX now supports install plugin online
SDKBOX online documentation
Upgrade Vugnle SDK to new version
 * iOS: 3.1.2
 * Android: 3.3.1

##1.1.5
Fix SDKBOX conflicts with Plugin-x

##1.1.4
Fix SDKBOX IAP plugin return invalid pricing data
