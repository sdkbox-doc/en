## API Reference

### Please check Scientific Revenue Documentation

https://documentation.scientificrevenue.com/sdkbox-cocos2d-x/

contact ted@scientificrevenue.com for access.

```lua
sdkbox.ScientificRevenue:setDebugMode ( bool flag ) ;
```
> Enable/disable debug logging

```lua
sdkbox.ScientificRevenue:init();
```
> Load and initialise plugin

```lua
sdkbox.ScientificRevenue:sessionOptions(bool newUserFlag, const char* uiLocale, bool allowLocation);
```
> Set the Pricing Session Options

```lua
sdkbox.ScientificRevenue:startSession(const char* userId);
```
> Start the Pricing Session

```lua
sdkbox.ScientificRevenue:stopSession();
```
> Stop the Pricing Session