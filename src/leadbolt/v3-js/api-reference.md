## API Reference

### Methods
```javascript
sdkbox.PluginLeadBolt.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginLeadBolt.setListener(listener);
```
> Set listener to listen for leadbolt events

```javascript
sdkbox.PluginLeadBolt.startSession(apiKey);
```
> start session

```javascript
sdkbox.PluginLeadBolt.closeSession();
```
> close session

```javascript
sdkbox.PluginLeadBolt.setSyncDataPeriodInSecond(periodInSecond);
```
> sync data second, just valid on ios

```javascript
sdkbox.PluginLeadBolt.sync();
```
> sync data

```javascript
sdkbox.PluginLeadBolt.event(name);
```
> event

```javascript
sdkbox.PluginLeadBolt.event(name, floatValue);
```
> event with float value

```javascript
sdkbox.PluginLeadBolt.transaction(name, floatValue, currencyCode, ref, instant);
```
> Transaction Events

```javascript
sdkbox.PluginLeadBolt.loadModule(placement, userData);
```
> load module

```javascript
sdkbox.PluginLeadBolt.loadModuleToCache(placement, userData);
```
> load module to cache

```javascript
sdkbox.PluginLeadBolt.destroyModule();
```
> destroy module

```javascript
sdkbox.PluginLeadBolt.setCrashHandlerStatus(enable);
```
> Crash Reporting

```javascript
sdkbox.PluginLeadBolt.crashWithName(crashName, description);
```
> Crash Reporting

```javascript
sdkbox.PluginLeadBolt.fixAdOrientation(orientation);
```
> force Ad Orientation

```javascript
sdkbox.PluginLeadBolt.isAdReady(placement);
```
> is ad ready

```javascript
sdkbox.PluginLeadBolt.setAgeRange(range);
```
> setAgeRange
accepted values "13-17", "18-25", "26-35", "36-45", "46+"

```javascript
sdkbox.PluginLeadBolt.setGender(gender);
```
> setGender
accepted valued "Male", "Female"

```javascript
sdkbox.PluginLeadBolt.setFramework(f);
```
> setFramework


### Listeners
```javascript
onModuleLoaded(placement);
```
> Notifies the delegate that the module has finished loading

```javascript
onModuleClosed(placement);
```
> Notifies the delegate that the module has closed

```javascript
onModuleClicked(placement);
```
> Notifies the delegate that the module has clicked

```javascript
onModuleCached(placement);
```
> Notifies the delegate that the module has cached

```javascript
onModuleFailed(placement, error, iscached);
```
> Notifies the delegate that the module has fail

```javascript
onMediaFinished(viewCompleted);
```
> Notifies the delegate that the module has finished


