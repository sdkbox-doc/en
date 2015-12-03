## API Reference

### Please check Scientific Revenue Documentation

https://documentation.scientificrevenue.com/sdkbox-cocos2d-x/

contact ted@scientificrevenue.com for access.

```cpp
static ScientificRevenue* getInstance();
```
> Reference PluginInstance

```cpp
void setDebugMode ( bool flag ) ;
```
> Enable/disable debug logging

```cpp
void loadScientificRevenuePlugin();
```
> Load and initialise plugin

```cpp
const char* sessionOptions(bool newUserFlag, const char* uiLocale, bool allowLocation);
```
> Set the Pricing Session Options

```cpp
void startSession(const char* userId);
```
> Start the Pricing Session

```cpp
void stopSession();
```
> Stop the Pricing Session
