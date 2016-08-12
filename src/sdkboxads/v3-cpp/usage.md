### Initialize SdkboxAds
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:

```cpp
#include "PluginSdkboxAds/PluginSdkboxAds.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSdkboxAds::init();
}
```

### Using SdkboxAds


#### Configuration
SdkboxAds is an ad mediation service. This means it will manage at runtime a set of predefined AdUnits.
The configuration spans in two different parts: AdUnits, and Placements. Each AdUnit will reference to an Sdkbox plugin
that can be managed as an AdUnit.
The configuration could be:
<pre>
    "SdkboxAds": {
        "units": [
            "AdColony",
            "Fyber",
            "Chartboost",
            "Vungle"
        ]
    }
</pre>

Placements are references to specific ads in a given AdUnit. A whole SdkboxAds config file could be:

<pre>
    "SdkboxAds": {
        "units": [
                "AdColony",
                "Fyber",
                "Chartboost",
                "Vungle"
            ],
        "placements": [
            {
                "id" : "placement-1",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "AdColony",
                      "name": "video"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Default"
                    }
                ]
            },
            {
                "id" : "placement-2",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "Vungle",
                      "name": "reward"
                    },
                    {
                      "unit": "AdColony",
                      "name": "v4vc"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Next Level"
                    }
                ]
            }
        ] 
    }
</pre>

#### Usage

A call to `sdkbox::SdkboxAds::init()` will suffice to instantiate and manage all referenced AdUnits in the configuration
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
