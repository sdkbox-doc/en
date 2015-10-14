### Initialize AgeCheq
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginAgeCheq:init()
```

### Using AgeCheq
After initialization you can begin to use the AgeCheq functionality. Use `check` wherever you want from your code:
```lua
sdkbox.PluginAgeCheq:check("agecheqPin")
```

### Catch AgeCheq events (optional)
This allows you to catch the `AgeCheq` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
sdkbox.PluginAgeCheq:init()
sdkbox.PluginAgeCheq:setListener(function(data)
	    if "checkResponse" == data.event then
	        dump(data)
	    elseif "associateDataResponse" == data.event then
	        dump(data)
	    end
	end)
sdkbox.PluginAgeCheq:check("agecheqPin")
```
