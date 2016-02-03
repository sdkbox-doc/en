[&#171; SDKBOX Home](http://sdkbox.com)

<h1>SdkboxAds Plugin</h1>

##Overview
While Sdkbox includes out-of-the-box support for many ad networks, these can be managed using Sdkbox’s mediation software called SdkboxAds. 
It includes support for playing ads and rewarded contents, as well as the definition of placements.
Before digging deeper into its internals, some concepts must be clarified.

###AdUnit
An AdUnit will be any plugin which can be mediated by SdkboxAds. AdColony, Vungle or Chartboost are examples of AdUnits.
AdUnits will be responsible for wrapping already existing plugins and exposing all of them through a common exposed interface. Yes, you will be able to manage all AdUnits with the same codebase.
Each AdUnit will expose in the configuration a set of different elements like interstitials, videos or rewards. For example, AdColony defines zones, Chartboost locations and Vungle places. All these three concepts are the same: a name to point to a given ad type.

###Placement
A Placement is a collection of pairs of AdUnit and ad name. The idea is to mediate among different AdUnits in a declarative way.
For example, a placement could be:

<pre>
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
          "name": "interstitial"
        }
      ]
    },
   …
]
</pre>

Each time this placement is invoked, it round-robin for each AdUnit it has defined. If by any circumstance, at invocation time any AdUnit has no Ads data ready to be played, the next AdUnit will be requested. If no AdUnit has ads ready, nothing will happen.
The only available placement strategy is currently “round-robin”, but expect it to have more available values anytime soon.
Certain AdUnits don’t handle the concept of a zone, location or place (e.g Fyber). For these, Sdkbox plugin will use `INTERSTITIAL`, `REWARDED`, `VIDEO` or `BANNER` to refer to the expected ad type to be played by the AdUnit.

###Default AdUnit
SdkboxAds defines a default AdUnit. It will be the first defined unit in the the plugin’s units list.

<<[../shared/guides.md]


##Sample Project

* [A demo project using cocos2d-x v3.x on github](https://github.com/sdkbox/sdkbox-SdkboxAds-sample)
