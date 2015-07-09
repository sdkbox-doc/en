## API Reference

### Methods
```cpp
static void init();
```
> initialize the plugin instance.

```cpp
static AdColonyAdStatus getStatus(const std::string& name);
```
> Check the availability of the AdColony ads by name

```cpp
static int zoneStatusForZone(const std::string& zoneID);
```
> returns the status for the specified zone. Use this to pre-load a zone.

```cpp
static void show(const std::string& name);
```
> play video ad using provided __zone name__ that was specified in `sdkbox_config.json`.

```cpp
static void setListener(AdColonyListener* listener);
```
> set a listener to listen for event changes.

```cpp
static void removeListener();
```
> remove the event listener.

```cpp
static bool isVirtualCurrencyRewardAvailableForZone(const std::string& zoneID);
```
> check if this zone offers a virtual currency reward.

```cpp
static int getVirtualCurrencyRewardsAvailableTodayForZone(
  const std::string& zoneID);
```
> is there a virtual currency reward available to the user today for passed in
zone.

```cpp
static std::string getVirtualCurrencyNameForZone(const std::string& zoneID);
```
> get virtual currency name for passed in zone.

```cpp
static int getVirtualCurrencyRewardAmountForZone(const std::string& zoneID);
```
> the amount of the virtual currency reward for passed in zone.

```cpp
static int getVideosPerReward(const std::string& currencyName);
```
> are there multiple videos to watch per reward? Get the number of them.

```cpp
static int getVideoCreditBalance(const std::string& currencyName);
```
> get video credit balance for passed in currency name.

```cpp
static void cancelAd();
```
> stop the currently showing ad.

```cpp
static bool videoAdCurrentlyRunning();
```
> is there a video currently showing?

```cpp
static void turnAllAdsOff();
```
> turn off all ads.

### Listeners
```cpp
void onAdColonyChange(const sdkbox::AdColonyAdInfo& info, bool available);
```
> called when AdColony is finished loading.

```cpp
void onAdColonyReward(const sdkbox::AdColonyAdInfo& info,
  const std::string& currencyName,
  int amount, bool success);
```
> reward was received.

```cpp
void onAdColonyStarted(const sdkbox::AdColonyAdInfo& info);
```
> showing an ad has started.

```cpp
void onAdColonyFinished(const sdkbox::AdColonyAdInfo& info);
```
> showing an ad has finished.
