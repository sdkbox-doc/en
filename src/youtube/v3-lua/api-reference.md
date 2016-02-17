## API Reference

### Methods
```lua
sdkbox.PluginYoutube:init()
```
> initialize the plugin instance.

```lua
sdkbox.PluginYoutube:setListener(listener)
```
> set provided listener.

```lua
sdkbox.PluginYoutube:getListener()
```
> get provided listener.

```lua
sdkbox.PluginYoutube:removeListener()
```
> remove listeners.

```lua
sdkbox.PluginYoutube:playVideo(video_id, startMillis, autoplay, lightbox)
```
> Play youtube video with video id
you can find video id as the last part of the youtube video's url

```lua
sdkbox.PluginYoutube:playPlayList(playlist_id,
                                   playListStartIndex,
                                   startMillis,
                                   autoplay,
                                   lightbox)
```
> Play a youtube playlist

```lua
sdkbox.PluginYoutube:playVideoList(video_ids,
                                    playListStartIndex,
                                    startMillis,
                                    autoplay,
                                    lightbox)
```
> Play a group of youtube videos

```lua
sdkbox.PluginYoutube:close()
```
> Close youtube player


### Listeners
```lua
onPlayEnds(played_ok)
```


