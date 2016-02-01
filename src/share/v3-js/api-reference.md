## API Reference

### Methods
```javascript
sdkbox.PluginShare.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginShare.setListener(listener);
```
> Set listener to listen for share events

```javascript
sdkbox.PluginShare.getListener();
```
> Get the listener

```javascript
sdkbox.PluginShare.removeListener();
```
> Remove the listener, and can't listen to events anymore

```javascript
sdkbox.PluginShare.share(info);
```
> Share content, e.g. {text: "share string"}

### Listeners
```javascript
onShareState(response);
```
> Notifies the delegate that share completion


