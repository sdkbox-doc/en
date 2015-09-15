## API Reference

### Methods
```javascript
sdkbox.PluginSoomlaGrow.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginSoomlaGrow.setListener(listener);
```
> Set listener to listen to GROW events

```javascript
sdkbox.PluginSoomlaGrow.refreshInsight()
```
>  Refreshed Insights information from the server

```javascript
sdkbox.PluginSoomlaGrow.getUserInsightInfo()
```
>  get user insights info
>  Note: the returned value may be empty


### Listeners
```javascript
onHighWayInitialized()
```

>  This event is triggered once the highway initialized.

```javascript
onHighWayConnected()
```

>  This event is triggered once the highway is connected to server.

```javascript
onHighWayDisconnected()
```

>  This event is triggered once the highway disconnect from the server.
