## API Reference

### Methods
```javascript
sdkbox.PluginSdkboxAds.init();
```
> Initialize the plugin instance: the plugin initializes from the sdkbox_config.json file and reads configuration of the form:
> <pre>
 <code>
   "SdkboxAds": {
       "units": [ "AdColony", "Fyber" ],
       "placements": [ {} ]
   }
 </code>
</pre>

> The "units" array references other plugins' configuration. Sdkboxads mediates between other plugins
and/or simplifies interaction with them.
The "placements" block will be of the form:
> <pre>
 <code>
    {
         "id” : "placement_id”,
         "strategy" : "round-robin", // only value by now.
         "units” : [
             <UnitDefinition>
         ]
     }
 </code>
</pre>

> and each UnitDefinition as:
> <pre>
 <code>
     {
         "Unit" : string, // result_of_AdUnit.getId(),
         "name" : string, // a zone, place, or location from AdUnit's lugin config
         "params" : json_object
     }
 </code>
</pre>

> For a sample Sdkboxads config, check the example at Sdkbox github public repository.
The "params" configuration block will allow to pass in specific information to play ads
like location, position, etc.
Check each AdUnit's documentation to find specifics on its configuration.


```javascript
sdkbox.PluginSdkboxAds.setListener(listener);
```
> Set Sdkboxads' plugin listener.
This listener will expose for each registered AdUnits, events related to Ads and Rewards.
In SdkboxAds, an Ad refers generally to VIDEO, INTERSTITIAL and BANNER.
Note that some ad units may have only Ads.

```javascript
sdkbox.PluginSdkboxAds.placement(placement);
```
> A placement is a collection of mediated AdUnits.
When you want to invoke a placement, just call this method.
If the placement does not exist, the call will just be ignored.
A placement will take care of AdUnit’s cache control, so if the current AdUnit has no
cached content, or the AdUnit fails to load an ad, the next adUnit will be used.
>
> The placement will cycle throughout all the AdUnits it references, in a round robin fashion.
In the short term, new placement strategies will be added.


```javascript
sdkbox.PluginSdkboxAds.isAvailable(placement);
```
> check if placement available

```javascript
sdkbox.PluginSdkboxAds.hide(placement);
```
> hide placement

```javascript
sdkbox.PluginSdkboxAds.hideAd(ad_unit, zone_place_location);
```


### Listeners

