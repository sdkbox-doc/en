## API Reference

### Methods
```javascript
sdkbox.PluginShare.init(jsonConfig);
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginShare.setListener(listener);
```
> Set listener to listen for share events

```javascript
sdkbox.PluginShare.setSharePanelTitle(s);
```
> set custome share platform choose panel title, default is "Share to"

```javascript
sdkbox.PluginShare.setSharePanelCancel(s);
```
> set custome share platform choose panel cancel button, default is "Cancel"


### Listeners
```javascript
onShareState(response);
```
> Notifies the delegate that share completion


