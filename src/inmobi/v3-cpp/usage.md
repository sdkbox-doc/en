### Initialize InMobi
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginInMobi/PluginInMobi.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginInMobi::init();
}
```

### Show interstitial
After initialization you can begin to use the InMobi functionality:
```cpp
// Manually Loading Ads
sdkbox::PluginInMobi::loadInterstitial();

if (sdkbox::PluginInMobi::isInterstitialReady()) {
    CCLOG("Plugin InMobi interstitial ad is ready");
    sdkbox::PluginInMobi::showInterstitial();
} else {
    CCLOG("Plugin InMobi interstitial ad is not ready");
}
```

### Set Log level
You can set log level with follow function
```cpp
sdkbox::PluginInMobi::setLogLevel(sdkbox::PluginInMobi::SBIMSDKLogLevel::kIMSDKLogLevelDebug);
```

### Set user data
You can use following functions to set user data
```cpp
sdkbox::PluginInMobi::addIdForType("test", sdkbox::PluginInMobi::SBIMSDKIdType::kIMSDKIdTypeLogin);
sdkbox::PluginInMobi::removeIdType(sdkbox::PluginInMobi::SBIMSDKIdType::kIMSDKIdTypeLogin);
sdkbox::PluginInMobi::setAge(18);
sdkbox::PluginInMobi::setAreaCode("900");
sdkbox::PluginInMobi::setAgeGroup(sdkbox::PluginInMobi::SBIMSDKAgeGroup::kIMSDKAgeGroupBetween18And20);
sdkbox::PluginInMobi::setYearOfBirth(1989);
sdkbox::PluginInMobi::setEducation(sdkbox::PluginInMobi::SBIMSDKEducation::kIMSDKEducationHighSchoolOrLess);
sdkbox::PluginInMobi::setEthnicity(sdkbox::PluginInMobi::SBIMSDKEthnicity::kIMSDKEthnicityHispanic);
sdkbox::PluginInMobi::setGender(sdkbox::PluginInMobi::SBIMSDKGender::kIMSDKGenderMale);
sdkbox::PluginInMobi::setHouseholdIncome(sdkbox::PluginInMobi::SBIMSDKHouseholdIncome::kIMSDKHouseholdIncomeBelow5kUSD);
sdkbox::PluginInMobi::setIncome(4500);
sdkbox::PluginInMobi::setInterests("game");
sdkbox::PluginInMobi::setLanguage("en-us");
sdkbox::PluginInMobi::setLocation("cd", "sc", "usa");
sdkbox::PluginInMobi::setLocation(102, 348);
sdkbox::PluginInMobi::setNationality("nationality");
sdkbox::PluginInMobi::setPostalCode("618000");
```

### Catch InMobi events (optional)
This allows you to catch the `InMobi` events so that you can perform operations based upon responses. A simple example might look like this:

* Allow your class to extend `sdkbox::InMobiListener`
```cpp
#include "PluginInMobi/PluginInMobi.h"
class MyClass : public sdkbox::InMobiListener {
public:
  	void bannerDidFinishLoading() {
        CCLOG("bannerDidFinishLoading");
    };
    void bannerDidFailToLoadWithError(sdkbox::PluginInMobi::SBIMStatusCode code, const std::string& description) {
        CCLOG("bannerDidFailToLoadWithError status:%d, desc:%s", code, description.c_str());
    };

    void bannerDidInteractWithParams(std::map<std::string, std::string> params) {
        CCLOG("bannerDidInteractWithParams");
    };

    void userWillLeaveApplicationFromBanner() {
        CCLOG("userWillLeaveApplicationFromBanner");
    };

    void bannerWillPresentScreen() {
        CCLOG("bannerWillPresentScreen");
    };

    void bannerDidPresentScreen() {
        CCLOG("bannerDidPresentScreen");
    };

    void bannerWillDismissScreen() {
        CCLOG("bannerWillDismissScreen");
    };

    void bannerDidDismissScreen() {
        CCLOG("bannerDidDismissScreen");
    };

    void bannerRewardActionCompletedWithRewards(std::map<std::string, std::string> rewards) {
        CCLOG("bannerRewardActionCompletedWithRewards");
    };

    void interstitialDidFinishLoading() {
        CCLOG("interstitialDidFinishLoading");
    };

    void interstitialDidFailToLoadWithError(sdkbox::PluginInMobi::SBIMStatusCode code, const std::string& description) {
        CCLOG("interstitialDidFailToLoadWithError status:%d, desc:%s", code, description.c_str());
    };

    void interstitialWillPresent() {
        CCLOG("interstitialWillPresent");
    };

    void interstitialDidPresent() {
        CCLOG("interstitialDidPresent");
    };

    void interstitialDidFailToPresentWithError(sdkbox::PluginInMobi::SBIMStatusCode code, const std::string& description) {
        CCLOG("interstitialDidFailToPresentWithError");
    };

    void interstitialWillDismiss() {
        CCLOG("interstitialWillDismiss");
    };

    void interstitialDidDismiss() {
        CCLOG("interstitialDidDismiss");
    };

    void interstitialDidInteractWithParams(std::map<std::string, std::string> params) {
        CCLOG("interstitialDidInteractWithParams");
    };

    void interstitialRewardActionCompletedWithRewards(std::map<std::string, std::string> rewards) {
        CCLOG("interstitialRewardActionCompletedWithRewards");
    };

    void userWillLeaveApplicationFromInterstitial() {
        CCLOG("userWillLeaveApplicationFromInterstitial");
    };
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginInMobi::setListener(this);
```
