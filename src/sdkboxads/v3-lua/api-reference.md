## API Reference

### Methods
```lua
sdkbox.PluginSdkboxAds:init ( ) ;
```
> initialize the plugin instance.

```lua
sdkbox.PluginSdkboxAds:setListener ( listener ) ;
```
> Set listener to listen for SdkboxAds events

```lua
sdkbox.PluginSdkboxAds:playAd()
```
> Each unit knows how to play an ad by default.  So this method will play a default Ad for the default AdUnit.

```lua
sdkbox.PluginSdkboxAds:playAd( ad_name, params );
```
> Play An Ad in the default AdUnit with extra hints. These hints are i.e. position on screen, transparency, etc. Each AdUnit will document what extra hints can be passed to play an Ad. Currently none of the AdUnits need this parameter.

```lua
sdkbox.PluginSdkboxAds:playAd( ad_unit, ad_name, params );
```
> Play an Ad in an specific AdUnit with extra hint parameters. If you pass values to an AdUnit that does need need, they will simply be ignored.

```lua
sdkbox.PluginSdkboxAds:placement(placement_name);
```
> 
When you want to invoke a placement, just call this method. If the placement does not exist, the call will just be ignored. A placement will take care of AdUnit’s cache control, so if the current AdUnit has no cached content, or the AdUnit fails to load an ad, the next adUnit will be used.

```lua
sdkbox.PluginSdkboxAds:cacheControl( ad_unit, cacheOpts );
```
> Some Ad units expose fine-grained cache control. For example Chartboost offers specific cache control for each location, as well as general Ads cache control. This method interfaces with the AdUnit’s cache mechanism. If no cache control is exposed for a given AdUnit, the call will silently be ignored. Each AdUnit will document what valid values to pass to the cacheOpts parameter. E.g. for Chartboost, these are valid values:
>
>  "Default": true,		// a configuration location
>  "Level Complete": true,	// a configuration location
>  "__ADS__": true		// a general placeholder chartboost specific 
   

### Listeners
```lua
onAdAction( ad_unit_id, ad_name, action_type);
```
> This method notifies back with the AdUnit identifier, the Ad name it tried to play, and an enum type of the action it is communicating about.
> The Action type is the following enum:

```lua
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

```lua
onRewardAction( ad_unit_id, ad_name, reward_amount, reward_succeed);
```