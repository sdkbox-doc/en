### Register Javascript Functions
You need to register all the Youtube JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginYoutubeJS.hpp"
#include "PluginYoutubeJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
sc->addRegisterCallback(register_all_PluginYoutubeJS);
sc->addRegisterCallback(register_all_PluginYoutubeJS_helper);
```

### Initialize Youtube
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginYoutube.init();
```

### Play Video
Play a youtube video with a youtube video id

For example
```javascript
sdkbox.PluginYoutube.playVideo("cdgQpa1pUUE", 0, true, true);
```

### Play multiple videos
There are two methods you can use if you want to play multiple videos

You can either play a youtube playlist
```javascript
sdkbox.PluginYoutube.playPlayList("7E952A67F31C58A3", 0, 0, true, true);
```

or you can put a group of videos together and play them
```javascript
var v = ["cdgQpa1pUUE","8aCYZ3gXfy8"];

sdkbox.PluginYoutube.playVideoList(v, 0, 0, true, true);
```

### Implement YoutubeListner
* You can implement YoutubeListener if you want to receive callbacks like video finish playing.
```javascript

sdkbox.PluginYoutube.setListener({
    onPlayEnds : function() { cc.log("Video finished playing");}
})

```
