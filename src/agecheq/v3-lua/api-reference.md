## API Reference

### Methods
```lua
sdkbox.PluginAgeCheq:init()
```
>  initialize the plugin instance.

```lua
sdkbox.PluginAgeCheq:setListener(listener)
```
> Set listener to listen for adcolony events

```lua
sdkbox.PluginAgeCheq:check(ACPin)
```
>  The AgeCheq check method is used to determine the status of a child’s relationship with a particular
 online service. It requires the developer’s unique identifier, the child’s AgeCheq PIN as set up by
 their parent, and the unique identifier of the game or application.

```lua
sdkbox.PluginAgeCheq:associateData(ACPin, Data)
```
>  The associateData method allows you to save a string of information linking it to a particular
 AgeCheqPIN for a specific game or app. You’ll want to use that data later if a parent should
 unauthorize your online service.


### Listeners
```lua
checkResponse(rtn,
               rtnmsg,
               apiversion,
               checktype,
               appauthorized,
               appblocked,
               parentverified,
               under13,
               under18,
               underdevage,
               trials)
```
>  The delegate named checkResponse is triggered once the check command executes. It contains several
 status variables that you can check against.

```lua
associateDataResponse(rtn, rtnmsg)
```
>  The delegate named associateDataResponse is triggered once the associateData command executes.
