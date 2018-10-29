### Initialize Misc
Initialize the plugin by calling `init()` where appropriate in your code. We
recommend to do this in the `app.js`. Example:
```javascript
sdkbox.PluginMisc.init();
```

### send local notification

```javascript
// will receive notification after 10 second
let nid = sdkbox.PluginMisc.localNotify("test title", "this a test notify content", 1000 * 10);
cc.log('Local Notification ID:' + nid);
```

### Implement MiscListner
* You can implement MiscListener if you want to receive local notification event.
```javascript

sdkbox.PluginMisc.setListener({
    onHandleLocalNotify :function (json) {
        cc.log(json);
    }
});

```
