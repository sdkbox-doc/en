## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( SdkboxAdsListener * listener ) ;
```
> Set listener to listen for SdkboxAds events

```cpp
static void playAd()
```
> Each unit knows how to play an ad by default.  So this method will play a default Ad for the default AdUnit.

```cpp
static void playAd(const std::string& );
```
> Play an identified by name on the Default AdUnit

```cpp
static void playAd(const std::string&, const AdUnitParams& params );
```
> Eventually, an AdUnit may need some extra hints to play an ad, like position on screen, transparency, etc. Each AdUnit will document what extra hints can be passed to play an Ad. Currently none of the AdUnits need this parameter.

```cpp
static void playAd(
        const std::string& ad_unit, 
        const std::string& zone_place_location );
```
> Play an ad name, for a given AdUnit. AdUnits are idenfitied by name. So a valid example call would be: 
`sdkbox::SdkboxAds::playAd(“AdColony”, “video”);`.

```cpp
static void playAd(
        const std::string& ad_unit, 
        const std::string& zone_place_location, 
        const AdUnitParams& params );
```
> Again, should an AdUnit need extra parameters, use this method. If you pass values to an AdUnit that does need need, they will simply be ignored.

```cpp
static void placement(const std::string& placement);
```
> 
When you want to invoke a placement, just call this method. If the placement does not exist, the call will just be ignored. A placement will take care of AdUnit’s cache control, so if the current AdUnit has no cached content, or the AdUnit fails to load an ad, the next adUnit will be used.

```cpp
static void cacheControl( 
        const std::string& ad_unit, 
        const std::map<std::string, std::string>& cacheOpts );
```
> Some Ad units expose fine-grained cache control. For example Chartboost offers specific cache control for each location, as well as general Ads cache control. This method interfaces with the AdUnit’s cache mechanism. If no cache control is exposed for a given AdUnit, the call will silently be ignored. Each AdUnit will document what valid values to pass to the cacheOpts parameter. E.g. for Chartboost, these are valid values:
>
>  "Default": true,		// a configuration location
>  "Level Complete": true,	// a configuration location
>  "__ADS__": true		// a general placeholder chartboost specific 
   


### Listeners
```cpp
void onAdAction( 
        const std::string& ad_unit_id, 
        const std::string& zone_location_place_you_name_it, 
        sdkbox::AdActionType action_type);
```
> This method notifies back with the AdUnit identifier, the Ad name it tried to play, and an enum type of the action it is communicating about.
> The Action type is the following enum:

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
> Not all AdUnits will expose all types of events. For example, Chartboost notifies CLICKED action, but AdColony does not. Each AdUnit’s documentation will reflect what events will notify.

```cpp
void onRewardAction( 
        const std::string& ad_unit_id, 
        const std::string& zone_id, 
        float reward_amount, 
        bool reward_succeed);
```