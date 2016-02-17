## API Reference

### Methods
```javascript
sdkbox.PluginYoutube.init();
```
> initialize the plugin instance.

```javascript
sdkbox.PluginYoutube.setListener(listener);
```
> set provided listener.

```javascript
sdkbox.PluginYoutube.getListener();
```
> get provided listener.

```javascript
sdkbox.PluginYoutube.removeListener();
```
> remove listeners.

```javascript
sdkbox.PluginYoutube.playVideo(video_id, startMillis, autoplay, lightbox);
```
> Play youtube video with video id
you can find video id as the last part of the youtube video's url

```javascript
sdkbox.PluginYoutube.playPlayList(playlist_id,
                                   playListStartIndex,
                                   startMillis,
                                   autoplay,
                                   lightbox);
```
> Play a youtube playlist

```javascript
sdkbox.PluginYoutube.playVideoList(video_ids,
                                    playListStartIndex,
                                    startMillis,
                                    autoplay,
                                    lightbox);
```
> Play a group of youtube videos

```javascript
sdkbox.PluginYoutube.close();
```
> Close youtube player


### Listeners
```javascript
onPlayEnds(played_ok);
```


