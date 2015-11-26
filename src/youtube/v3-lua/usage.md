### Initialize Youtube
* modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginYoutube:init()
```

### Play Video
Play a youtube video with a youtube video id

For example
```lua
sdkbox.PluginYoutube:playVideo("cdgQpa1pUUE", 0, true, true);
```

### Play multiple videos
There are two methods you can use if you want to play multiple videos

You can either play a youtube playlist
```lua
sdkbox.PluginYoutube:playVideo("cdgQpa1pUUE", 0, true, true);
```
or you can put a group of videos together and play them
```lua
v = {"cdgQpa1pUUE","8aCYZ3gXfy8"};

sdkbox.PluginYoutube.playVideoList(v, 0, 0, true, true);
```

### Implement YoutubeListner
* You can implement YoutubeListener if you want to receive callbacks like video finish playing.
```lua

sdkbox.PluginYoutube.setListener(function(name, args)
    if "onPlayEnds" == name then
      print("Video Finished")
    end
end)

```
