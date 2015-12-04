### Register Javascript Functions
You need to register all the InMobi JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginInMobiJS.hpp"
#include "PluginInMobiJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginInMobiJS);
sc->addRegisterCallback(register_all_PluginInMobiJS_helper);
```

### Initialize InMobi
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginInMobi.init();

//setting if need
sdkbox.PluginInMobi.setLogLevel(sdkbox.PluginInMobi.SBIMSDKLogLevel.kIMSDKLogLevelDebug);
sdkbox.PluginInMobi.addIdForType("test", sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
sdkbox.PluginInMobi.removeIdType(sdkbox.PluginInMobi.SBIMSDKIdType.kIMSDKIdTypeLogin);
sdkbox.PluginInMobi.setAge(18);
sdkbox.PluginInMobi.setAreaCode("area code");
sdkbox.PluginInMobi.setAgeGroup(sdkbox.PluginInMobi.SBIMSDKAgeGroup.kIMSDKAgeGroupBetween18And20);
sdkbox.PluginInMobi.setYearOfBirth(1989);
sdkbox.PluginInMobi.setEducation(sdkbox.PluginInMobi.SBIMSDKEducation.kIMSDKEducationHighSchoolOrLess);
sdkbox.PluginInMobi.setEthnicity(sdkbox.PluginInMobi.SBIMSDKEthnicity.kIMSDKEthnicityHispanic);
sdkbox.PluginInMobi.setGender(sdkbox.PluginInMobi.SBIMSDKGender.kIMSDKGenderMale);
sdkbox.PluginInMobi.setHouseholdIncome(sdkbox.PluginInMobi.SBIMSDKHouseholdIncome.kIMSDKHouseholdIncomeBelow5kUSD);
sdkbox.PluginInMobi.setIncome(4500);
sdkbox.PluginInMobi.setInterests("game");
sdkbox.PluginInMobi.setLanguage("zh-cn");
sdkbox.PluginInMobi.setLocation("cd", "sc", "usa");
sdkbox.PluginInMobi.setLocation(102, 348);
sdkbox.PluginInMobi.setNationality("nationality");
sdkbox.PluginInMobi.setPostalCode("618000");
```

### Show Interstitial
After initialization you can begin to use the InMobi functionality. Use `showInterstitial` wherever you want from your code:
```javascript
// Manually Loading Ads
sdkbox.PluginInMobi.loadInterstitial();

// show interstitial
if (sdkbox.PluginInMobi.isInterstitialReady()) {
    console.log('inmobi interstitial ad is ready');
    sdkbox.PluginInMobi.showInterstitial();
} else {
    console.log('inmobi interstitial ad is not ready');
}
```

### Catch InMobi events (optional)
This allows you to catch the `InMobi` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
var plugin = sdkbox.PluginInMobi
plugin.setListener({
    bannerDidFinishLoading: function() { console.log('bannerDidFinishLoading'); },
    bannerDidFailToLoadWithError: function(code, description) { console.log('bannerDidFailToLoadWithError code:' + code + ' desc:' + description); },
    bannerDidInteractWithParams: function(params) { console.log('bannerDidInteractWithParams'); },
    userWillLeaveApplicationFromBanner: function() { console.log('userWillLeaveApplicationFromBanner'); },
    bannerWillPresentScreen: function() { console.log('bannerWillPresentScreen'); },
    bannerDidPresentScreen: function() { console.log('bannerDidPresentScreen'); },
    bannerWillDismissScreen: function() { console.log('bannerWillDismissScreen'); },
    bannerDidDismissScreen: function() { console.log('bannerDidDismissScreen'); },
    bannerRewardActionCompletedWithRewards: function(rewards) { console.log('bannerRewardActionCompletedWithRewards'); },
    interstitialDidFinishLoading: function() { console.log('interstitialDidFinishLoading'); },
    interstitialDidFailToLoadWithError: function(code, description) { console.log('interstitialDidFailToLoadWithError code:' + code + ' desc:' + description); },
    interstitialWillPresent: function() { console.log('interstitialWillPresent'); },
    interstitialDidPresent: function() { console.log('interstitialDidPresent'); },
    interstitialDidFailToPresentWithError: function(code, description) { console.log('interstitialDidFailToPresentWithError code:' + code + ' desc:' + description); },
    interstitialWillDismiss: function() { console.log('interstitialWillDismiss'); },
    interstitialDidDismiss: function() { console.log('interstitialDidDismiss'); },
    interstitialDidInteractWithParams: function(params) { console.log('interstitialDidInteractWithParams'); },
    interstitialRewardActionCompletedWithRewards: function(rewards) { console.log('interstitialRewardActionCompletedWithRewards'); },
    userWillLeaveApplicationFromInterstitial: function() { console.log('userWillLeaveApplicationFromInterstitial'); }
})
plugin.init();
```
