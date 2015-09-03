### Initialize Chartboost
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginChartboost/PluginChartboost.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginChartboost::init();
}
```

### Showing Ads
Display an ad where ever you want from your code:
```cpp
// To use the Chartboost predefined locations
sdkbox::PluginChartboost::show(sdkbox::CB_Location_Default);
// To use customized location
sdkbox::PluginChartboost::show("your_ad_name");
```

### Catch Chartboost events (optional)
This allows you to catch the `Chartboost` events so that you can perform operations such as providing player rewards for watching the video.

* Allow your class to extend `sdkbox::ChartboostListener`
```cpp
#include "PluginChartboost/PluginChartboost.h"
class MyClass : public sdkbox::ChartboostListener
{
public:
    void onChartboostCached(const std::string& name);
    bool onChartboostShouldDisplay(const std::string& name);
    void onChartboostDisplay(const std::string& name);
    void onChartboostDismiss(const std::string& name);
    void onChartboostClose(const std::string& name);
    void onChartboostClick(const std::string& name);
    void onChartboostReward(const std::string& name, int reward);
    void onChartboostFailedToLoad(const std::string& name, sdkbox::CB_LoadError e);
    void onChartboostFailToRecordClick(const std::string& name, sdkbox::CB_ClickError e);
    void onChartboostConfirmation();
    void onChartboostCompleteStore();
};
```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginChartboost::setListener(this);
```
