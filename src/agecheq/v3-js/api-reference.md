## API Reference

### Methods
```javascript
sdkbox.PluginAgeCheq.init();
```
>  initialize the plugin instance.

```javascript
sdkbox.PluginAgeCheq.setListener(listener);
```
> Set listener to listen for adcolony events

```javascript
sdkbox.PluginAgeCheq.check(ACPin);
```
>  The AgeCheq check method is used to determine the status of a child’s relationship with a particular
 online service. It requires the developer’s unique identifier, the child’s AgeCheq PIN as set up by
 their parent, and the unique identifier of the game or application.

<pre>
 @param ACPin This unique identifier is passed by the user to link them with the online service. This identifier may be letters, numbers, or symbols from 4-30 characters long.
</pre>

```javascript
sdkbox.PluginAgeCheq.associateData(ACPin, Data);
```
>  The associateData method allows you to save a string of information linking it to a particular
 AgeCheqPIN for a specific game or app. You’ll want to use that data later if a parent should
 unauthorize your online service.

<pre>
 @param ACPin This unique identifier is passed by the user to link them with the online service. This identifier may be letters, numbers, or symbols from 4-30 characters long.
 @param Data This field holds the data you want to store for later.
</pre>


### Listeners
```javascript
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
               trials);
```
>  The delegate named checkResponse is triggered once the check command executes. It contains several
 status variables that you can check against.

<pre>
 @param rtn If the method made a good round-trip to the server and back, this value will be “OK”.
 If the method failed for some reason, this value will read “FAIL”.
 @param rtnmsg If the method failed for some reason, this value will hold a brief explanation of
 why it happened. If the method made a good round-trip to the server and back, this value will be
 empty.
 @param apiversion The version of the AgeCheq API used to fulfill requests.
 @param checktype The values will correspond to the following types:
         0 = Normal check call
         1 = Normal check as a result of a throttled call
         2 = All data forced to “allow” as a result of a throttled call
 @param appauthorized If the game or app is authorized by an adult for use by a child under 13,
 the value will be true. If the game or app is not authorized by a parent, or if the device is not
 yet registered this value will be false.
 @param appblocked If the game or app is authorized by an adult for use by a child under 13,
 but the game is temporarily blocked by the authorizing parent the value will be true. If the game
 or app is authorized by a parent and they do not have the blocking switch on the value will be
 false.
 @param parentverified The values indicate the following statuses:
         0 = Not verified
         1 = Fully verified via payment or form
         2 = Partially verified via EmailPlus, SMS, or VOIP
         3 = All data forced to "allow" as the result of a trial call and
             the trials value will be incremented
 @param under13 This field will be true if the user identified by the AgeCheq PIN
 has a birthdate that makes them currently under the age of thirteen based on information
 provided to the AgeCheq Parent Dashboard.
 @param under18 This field will be true if the user identified by the AgeCheq PIN has
 a birthdate that makes them currently under the age of eighteen based on information provided to
 the AgeCheq Parent Dashboard.
 @param underdevage This field will be true if the user identified by the AgeCheq PIN has a
 birthdate that makes them currently under the age of set by the developer for the application
 in the Developer Dashboard. If this custom age is not set, this field will always be a false.
 @param trials If the application is set up in the AgeCheq Developer Dashboard
 (https://developer.agecheq.com) to use Application Trials, this field will return the number
 of times a check has been made but the app has not been authorized.
</pre>

```javascript
associateDataResponse(rtn, rtnmsg);
```
>  The delegate named associateDataResponse is triggered once the associateData command executes.

<pre>
 @param rtn If the method made a good round-trip to the server and back, this value will be “OK”.
 If the method failed for some reason, this value will read “FAIL”.
 @param rtnmsg If the method failed for some reason, this value will hold a brief explanation
 of why it happened. If the method made a good round-trip to the server and back, this value
 will be empty.
</pre>


