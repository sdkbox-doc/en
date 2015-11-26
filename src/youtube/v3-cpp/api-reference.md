## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( YoutubeListener * listener ) ;
```
> set provided listener.

```cpp
static YoutubeListener * getListener ( ) ;
```
> get provided listener.

```cpp
static void removeListener ( ) ;
```
> remove listeners.

```cpp
static void playVideo ( const std::string & video_id ,
                        int startMillis ,
                        bool autoplay ,
                        bool lightbox ) ;
```
> Play youtube video with video id
you can find video id as the last part of the youtube video's url

```cpp
static void playPlayList ( const std::string & playlist_id ,
                           int playListStartIndex ,
                           int startMillis ,
                           bool autoplay ,
                           bool lightbox ) ;
```
> Play a youtube playlist

```cpp
static void playVideoList ( const std::vector <std::string> & video_ids ,
                            int playListStartIndex ,
                            int startMillis ,
                            bool autoplay ,
                            bool lightbox ) ;
```
> Play a group of youtube videos

```cpp
static void close ( ) ;
```
> Close youtube player


### Listeners
```cpp
void onPlayEnds ( bool played_ok );
```


