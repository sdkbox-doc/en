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
>start session

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

```javascript
sdkbox.PluginLeadBolt.event(name, floatValue);
```

```javascript
sdkbox.PluginLeadBolt.transaction(name, floatValue, currencyCode);
```

```javascript
sdkbox.PluginLeadBolt.transaction(name, floatValue, currencyCode, instant);
```

```javascript
sdkbox.PluginLeadBolt.transaction(name, floatValue, currencyCode, ref);
```

```javascript
sdkbox.PluginLeadBolt.transaction(name, floatValue, currencyCode, ref, instant);
```

```javascript
sdkbox.PluginLeadBolt.loadModule(placement);
```

```javascript
sdkbox.PluginLeadBolt.loadModule(placement, userData);
```

```javascript
sdkbox.PluginLeadBolt.loadModuleToCache(placement);
```

```javascript
sdkbox.PluginLeadBolt.loadModuleToCache(placement, userData);
```

```javascript
sdkbox.PluginLeadBolt.destroyModule();
```

```javascript
sdkbox.PluginLeadBolt.setCrashHandlerStatus(enable);
```

```javascript
sdkbox.PluginLeadBolt.crashWithName(crashName, description);
```

```javascript
sdkbox.PluginLeadBolt.fixAdOrientation(orientation);
```

```javascript
sdkbox.PluginLeadBolt.isAdReady(placement);
```

```javascript
sdkbox.PluginLeadBolt.setAgeRange(range);
```

```javascript
sdkbox.PluginLeadBolt.setGender(gender);
```

```javascript
sdkbox.PluginLeadBolt.setFramework(f);
```


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


