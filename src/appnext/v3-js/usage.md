### Register Javascript Functions
You need to register all the Appnext JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginAppnextJS.hpp"
#include "PluginAppnextJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginAppnextJS);
sc->addRegisterCallback(register_all_PluginAppnextJS_helper);
```

### Initialize Appnext
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginAppnext.init();
```

### cache ad/video

```cpp
sdkbox.PluginAppnext.cacheAd("default");
sdkbox.PluginAppnext.cacheVideo("fullscreen");
```
**NOTE** : Appnext ads needs to be cached before use, auto-caching is not available with this plugin. It might take couple of minutes to cache ads, once cached you would be able to see the ads. While caching, ads are not available.


### refresh ad/video

```
sdkbox.PluginAppnext.refreshAds();
sdkbox.PluginAppnext.refreshVideo("fullscreen");
```
**NOTE** : refresh ad or video after it is closed.


### show ad/video
```cpp
sdkbox.PluginAppnext.showAd("default");
sdkbox.PluginAppnext.showVideo("fullscreen");
```

### hide ad
```cpp
sdkbox.PluginAppnext.hideAd();
```

### check ad/video available
```cpp
sdkbox.PluginAppnext.isAdReady();
sdkbox.PluginAppnext.isVideoReady("fullscreen");


### Implement AppnextListner
* You can implement AppnextListener if you want to receive callbacks like video finish playing.
```javascript

sdkbox.PluginAppnext.setListener({
    onAdError : function(msg) { },
    onAdLoaded : function() { },
    onAdOpened : function() { }, // not support on android
    onAdClosed : function() { },
    onAdClicked : function() { },

    onVideoLoaded : function(name) { },     // not support on ios
    onVideoClicked : function(name) { },    // not support on ios
    onVideoClosed : function(name) { },     // not support on ios
    onVideoEnded : function(name) { },      // not support on ios
    onVideoError : function(name, msg) { }  // not support on ios
});

```
