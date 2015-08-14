## API Reference

### Methods
```javascript
sdkbox.PluginSoomlaGrow.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginSoomlaGrow.setListener(listener);
```
> Set listener to listen for soomlagrow events

```javascript
sdkbox.PluginSoomlaGrow.refreshInsight()
```
>  Refreshed SoomlaInsights information from the server

```javascript
sdkbox.PluginSoomlaGrow.getUserInsightInfo()
```
>  get user insight info
>  Note: the return may be empty


### Listeners
```javascript
onHighWayInitialized()
```

>  The delegate named onHighWayInitialized is triggerred once the highway initialized.

```javascript
onHighWayConnected()
```

>  The delegate named onHighWayConnected is triggerred once the highway connected to server success.

```javascript
onHighWayDisconnected()
```

>  The delegate named onHighWayDisconnected is triggerred once the highway disconnect to server.

