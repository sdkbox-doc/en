### Initialize Youtube
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers. Example:
```cpp
#include "PluginYoutube/PluginYoutube.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginYoutube::init();
}
```

### Play Video
Play a youtube video with a youtube video id

For example
```cpp
sdkbox::PluginYoutube::playVideo("cdgQpa1pUUE", 0, true, true);
```
Will play the following youtube video 
https://www.youtube.com/watch?v=cdgQpa1pUUE

### Play multiple videos
There are two methods you can use if you want to play multiple videos

You can either play a youtube playlist
```cpp
sdkbox::PluginYoutube::playPlayList("7E952A67F31C58A3", 0, 0, true, true);
```

or you can put a group of videos together and play them
```cpp
std::vector<std::string> v;
v.push_back( "cdgQpa1pUUE" );
v.push_back( "8aCYZ3gXfy8" );
v.push_back( "cdgQpa1pUUE" );

sdkbox::PluginYoutube::playVideoList(v, 0, 0, true, true);
```

### Implement YoutubeListner
* You can implement YoutubeListener if you want to receive callbacks like video finish playing.
```cpp
#include "PluginYoutube/PluginYoutube.h"
class MyClass : public sdkbox::YoutubeListener
{
private:
  void onPlayEnds( bool played_ok );
}
```
