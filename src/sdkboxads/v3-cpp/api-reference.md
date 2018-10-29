## API Reference

### Methods

```cpp
static void init ( ) ;
```

> The plugin initializes from the sdkbox_config.json file and reads configuration.
> <pre>
 <code>
   "SdkboxAds": {
       "units": [ "AdColony", "AdMob" ],
       "placements": [ {} ]
   }
 </code>
</pre>

> The "placements" block will be of the form:
> <pre>
 <code>
    {
         "id": string, // placement's id
         "strategy" : "round-robin", // only value by now.
         "units": [
             <UnitDefinition>
         ]
     }
 </code>
</pre>

> Each UnitDefinition as:
> <pre>
 <code>
     {
         "Unit": string, // result_of_AdUnit.getId(),
         "name": string, // a zone, place, or location name from AdUnit's plugin config,
         "params": json_object
     }
 </code>
</pre>

> For a sample Sdkboxads config, check the example at Sdkbox github public repository.
The "params" configuration block will allow to pass in specific information to play ads
like location, position, etc. Check each AdUnit's documentation to find specifics on its configuration.


```cpp
static void setListener ( sdkbox::PluginSdkboxAdsListener * listener ) ;
```
> Set Sdkboxads' plugin listener.
This listener will expose for each registered AdUnits, events related to Ads and Rewards.
In SdkboxAds, an Ad refers generally to VIDEO, INTERSTITIAL and BANNER.
Note that some ad units may have only Ads.

```cpp
static PluginSdkboxAdsListener * getListener ( ) ;
```
> Retrieve plugin's listener.

```cpp
static void playAd ( const std::string & ad_unit ,
                     const std::string & zone_place_location ,
                     const AdUnitParams & params ) ;
```
> Play an Ad identified by its zone/location/place with optional parameters.
AdUnits like Fyber which don't have zones, will use common placeholders like "INTERSTITIAL" or "REWARDED".
Some AdUnits may require extra information to play an Ad, and should use the params for that purpose.
You should refer to the documentation of each specific AdUnit about what parameters will accept.
>
> The ad will be played for a specific AdUnit based on its identifier. The identifiers are the
values in the "units" node of the sdkbox_config.json file.
For example: "AdColony" or "Fyber".

```cpp
static void playAd ( const std::string & ad_unit ,
                     const std::string & zone_place_location ) ;
```

```cpp
static void playAd ( const std::string & , const AdUnitParams & params ) ;
```
> Like the 3 parameter playAd method, this one plays an Ad for the default AdUnit.
Currently the default AdUnit is the first defined one in the sdkbox_config.json file.

```cpp
static void playAd ( const std::string & ) ;
```

```cpp
static void playAd ( ) ;
```
> Play a default Ad with the default AdUnit.
Each AdUnit knows how to play an Ad by default.
For example, AdColony will play the first video zone, or the first Reward if there's no one.

```cpp
static void placement ( const std::string & placement ) ;
```
> A placement is a collection of mediated AdUnits.
When you want to invoke a placement, just call this method.
If the placement does not exist, the call will just be ignored.
A placement will take care of AdUnit's cache control, so if the current AdUnit has no
cached content, or the AdUnit fails to load an ad, the next adUnit will be used.
>
> The placement will cycle throughout all the AdUnits it references, in a round robin fashion.
In the short term, new placement strategies will be added.


```cpp
static void cacheControl ( const std::string & ad_unit ,
                           const std::map <std::string ,
                           std::string> & cacheOpts ) ;
```
> Manage cache control policies.
Not all AdUnits expose cache control while some others expose fine-grained cache control.
For example Chartboost offers specific cache control for each location, as well as
general Ads cache control.
>
> This method interfaces with the AdUnit's cache mechanism. If no cache control is exposed
for a given AdUnit, the call will silently be ignored.
Each AdUnit will document what valid values to pass to the cacheOpts parameter.
E.g. for Chartboost, these are valid values:
cacheOpts for Chartboost:
     element : bool
         Element corresponds to an identifiable CBLocation (ChartBoost)
     e.g:
><pre>
 <code>
     {
         "Default": true, // a configuration location
         "Level Complete": true, // a configuration location
         "ADS": true // a general placeholder chartboost specific
     }
 </code>
</pre>

```cpp
static bool isAvailable ( const std::string & placement ) ;
```
> check if placement available

```cpp
static void hide ( const std::string & placement ) ;
```
> hide placement

```cpp
static void hideAd ( const std::string & ad_unit ,
                     const std::string & zone_place_location ) ;
```



