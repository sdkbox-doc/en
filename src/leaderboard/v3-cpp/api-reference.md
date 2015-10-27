## API Reference

### Methods
```cpp
static void init ( ) ;
```
> Initialize SDKBox Leaderboard

```cpp
static void setListener ( LeaderboardListener * listener ) ;
```
> Set listener for Leaderboard

```cpp
static LeaderboardListener * getListener ( ) ;
```
> Get listener of Leaderboard

```cpp
static void removeListener ( ) ;
```
> Remove listener for Leaderboard

```cpp
static void submitScore ( const std::string & leaderboardId , int score ) ;
```

```cpp
static void getLeaderboard ( const std::string & leaderboardId ) ;
```


### Listeners
```cpp
void onComplete ( std::string leaderboard );
```

```cpp
void onFail ( );
```


