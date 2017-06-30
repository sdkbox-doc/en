### Register Lua Functions
You need to register all the Firebase Lua functions with cocos2d-x before using them.

To do this:
* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` to include the following headers:
```cpp
#include "PluginFirebaseLua.hpp"
#include "PluginFirebaseLuaHelper.h"
```

* Modify `./frameworks/runtime-src/Classes/AppDelegate.cpp` make sure to call:
```cpp
    register_all_PluginFirebaseLua(LuaEngine::getInstance()->getLuaStack()->getLuaState());
    register_all_PluginFirebaseLua_helper(LuaEngine::getInstance()->getLuaStack()->getLuaState());
```

### Initialize Firebase
Initialize the plugin by calling `init()` where appropriate in your code.Example:
```lua
sdkbox.firebase.Analytics:init()
```

### Log event
You can log game event

```lua
local evt = {
    [sdkbox.firebase.Analytics.Param.kFIRParameterItemID] = 'id123456',
    [sdkbox.firebase.Analytics.Param.kFIRParameterItemName] = 'name123456',
    [sdkbox.firebase.Analytics.Param.kFIRParameterItemCategory] = 'category123456',
    [sdkbox.firebase.Analytics.Param.kFIRParameterPrice] = '123.4'
    }
sdkbox.firebase.Analytics:logEvent(sdkbox.firebase.Analytics.Event.kFIREventViewItem, evt)
```

