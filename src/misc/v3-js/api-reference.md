## API Reference

### Methods
```javascript
sdkbox.PluginMisc.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginMisc.setListener(listener);
```
> Set listener to listen for misc events

```javascript
sdkbox.PluginMisc.localNotify(title, content, delaymillisecond);
```
> send a local notification
@return notification id


### Listeners
```javascript
onHandleLocalNotify (payloadJson);
```

