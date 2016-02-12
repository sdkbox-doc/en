## API Reference

### Methods
```cpp
static bool init ( ) ;
```
> initialize the plugin instance.

```cpp
static void setListener ( SoomlaGrowListener * lis ) ;
```
> Set listener to listen for different events (list below)

```cpp
static SoomlaGrowListener * getListener ( ) ;
```
> get Listener of soomla grow

```cpp
static void removeListener ( ) ;
```
> remove Listener in soomla grow

```cpp
static void refreshInsights ( ) ;
```
> Refreshed GROW's Insights information from the server

```cpp
static int payRank ( EGenre genre ) ;
```
> get pay rank

```cpp
static double purchaseLikelihood ( EDayQuarter dayquarter ) ;
```
> purchase likelihood time


### Listeners
```cpp
void onGrowInitialized ( );
```
> This event is triggered once the highway initialized.

```cpp
void onGrowConnected ( );
```
> This event is triggered once the highway is connected to server.

```cpp
void onGrowDisconnected ( );
```
> This event is triggered once the highway disconnect from the server.

```cpp
void onGrowInsightsInitialized ( );
```
> This event is triggered once the grow insight initialized.

```cpp
void onInsightsRefreshFailed ( );
```
> This event is triggered once the grow insight refresh failed.

```cpp
void onInsightsRefreshFinished ( );
```
> This event is triggered once the grow insight refresh finished.

```cpp
void onInsightsRefreshStarted ( );
```
> This event is triggered once the grow insight refresh started.


