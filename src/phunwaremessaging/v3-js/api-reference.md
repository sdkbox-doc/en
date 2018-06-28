## API Reference

### Methods
```javascript
sdkbox.PluginPhunwareMessaging.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginPhunwareMessaging.setListener(listener);
```
> Set listener to listen for phunwaremessaging events

```javascript
sdkbox.PluginPhunwareMessaging.read(messageID);
```

```javascript
sdkbox.PluginPhunwareMessaging.remove(messageID);
```

```javascript
sdkbox.PluginPhunwareMessaging.deviceId();
```

```javascript
sdkbox.PluginPhunwareMessaging.serviceName();
```

```javascript
sdkbox.PluginPhunwareMessaging.version();
```

```javascript
sdkbox.PluginPhunwareMessaging.stop();
```


### Listeners
```javascript
init(success, message);
```
> Notifies the delegate that the module has finished loading

```javascript
error(message);
```

```javascript
notification(notifi);
```


