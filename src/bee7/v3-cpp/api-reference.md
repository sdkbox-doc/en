## API Reference

### Methods
```cpp
static void init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( Bee7Listener * listener ) ;
```
> Set listener to listen for bee7 events

```cpp
static Bee7Listener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void showGameWall ( ) ;
```


### Listeners
```cpp
void onAvailableChange ( bool available );
```

```cpp
void onVisibleChange ( bool available );
```

```cpp
void onGameWallWillClose ( );
```

```cpp
void onGiveReward ( long bee7Points ,
                    long virtualCurrencyAmount ,
                    const std::string & appId ,
                    bool cappedReward ,
                    long campaignId ,
                    bool videoReward );
```


