### Initialize SdkboxAds
Initialize the plugin in your code. We recommend to do it in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginSdkboxAds/PluginSdkboxAds.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSdkboxAds::init();
}
```

### Using SdkboxAds


#### Configuration
SdkboxAds is an ad mediation service. It manages a set of predefined AdUnits at runtime.
The configuration includes two parts: AdUnits, and Placements. 

- Each AdUnit entry references to a Sdkbox plugin that can be managed as an AdUnit.
- A Placement is a collection of pairs of AdUnit and ad name ordered by a strategy. 

Please read the (<a href="./../">SdkboxAds Configuration Overview</a>) for more details. 


#### Usage

A call to `sdkbox::SdkboxAds::init()` will load and instantiate all referenced AdUnits in the configuration
file.

To request a default Ad for the default AdUnit and have a fast integration test:
```cpp
sdkbox::PluginSdkboxAds::playAd()
```

To request Ads in the Default AdUnit:
```cpp
sdkbox::PluginSdkboxAds::playAd( const std::string& zone_place_location );
sdkbox::PluginSdkboxAds::playAd( const std::string& zone_place_location, const AdUnitParams& params );

// AdUnitParams is a typedef for std::map<std::string,std::string>
```
> Note: the params are defined per AdUnit, and should be checked in each AdUnit's documentation.

To request Ads for an specific AdUnit:
```cpp
sdkbox::PluginSdkboxAds::playAd( 
        const std::string& ad_unit_name, 
        const std::string& zone_place_location );
        
sdkbox::PluginSdkboxAds::playAd( 
        const std::string& ad_unit_name, 
        const std::string& zone_place_location, 
        const AdUnitParams& params );
```

To request ads for a placement defined in the sdkbox_config.json file:
```cpp
sdkbox::PluginSdkboxAds::placement( const str::string& placement );
```

To have fine grained cache control (for AdUnits that expose it):
```cpp
sdkbox::PluginSdkboxAds::cacheControl( 
        const std::string& ad_unit, 
        const std::map<std::string, std::string>& cacheOpts );
```
> Cache options are AdUnit specific and must be checked in each AdUnit's documentation.

### SdkboxAds events
This allows you to catch `SdkboxAds`' events.

* Allow your class to extend `sdkbox::SdkboxAdsListener` and override the functions listed:
```cpp
#include "PluginSdkboxAds/PluginSdkboxAds.h"
class MyClass : public sdkbox::SdkboxAdsListener
{
private:
    void onAdAction( 
            const std::string& ad_unit_id, 
            const std::string& zone_location_place_you_name_it, 
            sdkbox::AdActionType action_type);
            
    void onRewardAction( 
            const std::string& ad_unit_id, 
            const std::string& zone_id, 
            float reward_amount, 
            bool reward_succeed);

};
```
> `sdkbox::AdActionType` is an enum with these values:

```cpp
    enum AdActionType {

        LOADED=0,           	// content loaded
        LOAD_FAILED,        	// content failed to load

        CLICKED,            	// clicked on content

        REWARD_STARTED,	 	// reward started
        REWARD_ENDED,       	// reward achieved
        REWARD_CANCELED,    	// reward aborted

        AD_STARTED,         	// start showing.
        AD_CANCELED,        	// start showing.
        AD_ENDED,           	// content shown

        ADACTIONTYPE_UNKNOWN	// mostly on error situations.

    };

```

* Create a __listener__ that handles callbacks:
```cpp
sdkbox::PluginSdkboxAds::setListener( new MyClass() );
```
