### Register Javascript Functions
You need to register all the SOOMLA Grow JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginSoomlaGrowJS.hpp"
#include "PluginSoomlaGrowJSHelper.hpp"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginSoomlaGrowJS);
sc->addRegisterCallback(register_all_PluginSoomlaGrowJS_helper);
```

### Initialize SoomlaGrow
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginSoomlaGrow.init();
```

### Using GROW's Insights module
After initialization you can begin to use the Insights functionality. Use `refreshInsight`, 'getUserInsightInfo' wherever you want from your code:
```javascript
sdkbox.PluginSoomlaGrow.payRank(sdkbox.PluginSoomlaGrow.EGenre.Word)
sdkbox.PluginSoomlaGrow.purchaseLikelihood(sdkbox.PluginSoomlaGrow.EDayQuarter._12am_6am)

sdkbox.PluginSoomlaGrow.refreshInsight()
sdkbox.PluginSoomlaGrow.getUserInsightInfo()
```

all value of `sdkbox.PluginSoomlaGrow.EGenre`

-   Action
-   Adventure
-   Arcade
-   Board
-   Card
-   Casino
-   Casual
-   Educational
-   Family
-   Music
-   Puzzle
-   Racing
-   Role_Playing
-   Simulation
-   Sports
-   Strategy
-   Trivia
-   Word


all value of `sdkbox.PluginSoomlaGrow.EDayQuarter`

-   _12am_6am
-   _6am_12pm
-   _12pm_6pm
-   _6pm_12am


### Catch SoomlaGrow events (optional)
This allows you to catch the `SOOMLA Grow` events so that you can perform operations based upon responses. A simple example might look like this:
```javascript
sdkbox.PluginSoomlaGrow.setListener({
            onGrowInitialized: function() { cc.log("onGrowInitialized") },
            onGrowConnected: function() { cc.log("onGrowConnected") },
            onGrowDisconnected: function() { cc.log("onGrowDisconnected") },
            onGrowInsightsInitialized: function() { cc.log("onGrowInsightsInitialized") },
            onInsightsRefreshFailed: function() { cc.log("onInsightsRefreshFailed") },
            onInsightsRefreshFinished: function() { cc.log("onInsightsRefreshFinished") },
            onInsightsRefreshStarted: function() { cc.log("onInsightsRefreshStarted") }
            })
sdkbox.PluginSoomlaGrow.init()
```
