### Initialize Share
Modify your Lua code to `init()` the plugin. This can be done anyplace, however it must be done before trying to use the plugin's features.
```lua
sdkbox.PluginShare:init()
```

### share
After initialization you can begin to use the Share functionality:
```lua
local shareInfo = {}
shareInfo.text = '#sdkbox(www.sdkbox.com) - the cure for sdk fatigue - from lua - '
shareInfo.title = "sdkbox";
shareInfo.image = "http://www.sdkbox.com/assets/images/logo.png";
shareInfo.link = "http://www.sdkbox.com";
shareInfo.platform = sdkbox.SocialPlatform.Platform_Select;
plugin:share(shareInfo)
```

all value of sdkbox.SocialPlatform
 
- Platform_Unknow
- Platform_Twitter
- Platform_Facebook
- Platform_Select
- Platform_All
 

all value of sdkbox.SocialShareState

- SocialShareStateNone
- SocialShareStateUnkonw
- SocialShareStateBegin
- SocialShareStateSuccess
- SocialShareStateFail
- SocialShareStateCancelled
- SocialShareStateSelectShow
- SocialShareStateSelected
- SocialShareStateSelectCancelled


### Catch Share events (optional)
This allows you to catch the `Share` events so that you can perform operations based upon responses. A simple example might look like this:
```lua
local plugin = sdkbox.PluginShare
plugin:setListener(function(responsed)
	local event = responsed.event

    dump(responsed, "PluginShare share listener info:")
    if responsed.response.state == sdkbox.SocialShareState.SocialShareStateSuccess then
        print('share success')
    end

end)
plugin:init()
```
