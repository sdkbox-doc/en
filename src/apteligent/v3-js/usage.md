### Register Javascript Functions
You need to register all the Apteligent JS functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```javascript
#include "PluginApteligentJS.hpp"
#include "PluginApteligentJSHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```javascript
sc->addRegisterCallback(register_all_PluginApteligentJS);
sc->addRegisterCallback(register_all_PluginApteligentJS_helper);
```

### Logging Breadcrumbs

```javascript
// leave a breadcrumb
sdkbox.PluginApteligent.addFilter("www.gmail.com");

// perform all breadcrumb writes on a background thread
sdkbox.PluginApteligent.setAsyncBreadcrumbMode(true);
```


### Logging User Metadata

```
// Adding a Username
sdkbox.PluginApteligent.setUsername("MrsCritter");

// Adding Arbitrary User Metadata
sdkbox.PluginApteligent.setValueforKey("5", "Game Level");
```


### Logging Userflows
```javascript
// Beginning a Userflow
sdkbox.PluginApteligent.beginUserflow("login");

// Ending a Userflow
sdkbox.PluginApteligent.endUserflow("login");

// Failing a Userflow
sdkbox.PluginApteligent.failUserflow("login");

// Cancelling a Userflow
sdkbox.PluginApteligent.cancelUserflow("login");
```

### Modifying the Value of a Userflow
```javascript
int valueInCents = sdkbox.PluginApteligent.valueForUserflow("my_userflow");
valueInCents += 5;
sdkbox.PluginApteligent.setValueforUserflow(valueInCents, "my_userflow");

```

### Logging Network Requests
```javascript
sdkbox.PluginApteligent.logNetworkRequest("GET", "http://www.abc123def456.com", 2.0, 1000, 100, 200);
```


### Filtering Captured Data
```javascript
sdkbox.PluginApteligent.addFilter("www.gmail.com");
```

### Configuring Location
```javascript
// Beijing, China
sdkbox.PluginApteligent.updateLocation(39.9042, 116.4074);
```

### Other Tasks
```javascript
// Allowing Users to Opt Out of Crittercism
sdkbox.PluginApteligent.setOptOutStatus(true);

// Changing the verbosity of Crittercism’s Logs
// sdkbox.PluginApteligent.LoggingLevel.Silent  : Turns off all Crittercism log messages
// sdkbox.PluginApteligent.LoggingLevel.Error   : Only print errors. An error is an unexpected event that will result not capturing important data
// sdkbox.PluginApteligent.LoggingLevel.Warning : (Default) Only print warnings. Currently warning messages are printed when calling Crittercism methods before initializing Crittercism.
// sdkbox.PluginApteligent.LoggingLevel.Info    : The most verbose level of logging
sdkbox.PluginApteligent.setLoggingLevel(sdkbox.PluginApteligent.LoggingLevel.Info);

// Send App Load Data
// You must set `"delay_sending_appload":true` in `sdkbox_config.json` first
sdkbox.PluginApteligent.sendAppLoadData();
```


### Implement ApteligentListner
* You can implement ApteligentListener if you want to receive callbacks like video finish playing.
```javascript

sdkbox.PluginApteligent.setListener({
    onCrashOnLastLoad : function() { } // not support on android
});

```
