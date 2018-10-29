<<[../shared/manual_android_v3.md]

- frameworks/runtime-src/Classes/*.cpp <- $PLUGIN_MISC_BUNDLE/plugin/luabindings/*.cpp
- frameworks/runtime-src/Classes/*.h <- $PLUGIN_MISC_BUNDLE/plugin/luabindings/*.h
- frameworks/runtime-src/Classes/*.hpp <- $PLUGIN_MISC_BUNDLE/plugin/luabindings/*.hpp

- proj.android/app/jni/Android.mk
```diff
                   $(LOCAL_PATH)/../../../Classes/AppDelegate.cpp \
-                  $(LOCAL_PATH)/../../../Classes/HelloWorldScene.cpp
+                  $(LOCAL_PATH)/../../../Classes/HelloWorldScene.cpp \
+                  $(LOCAL_PATH)/../../../Classes/SDKBoxLuaHelper.cpp \
+                  $(LOCAL_PATH)/../../../Classes/PluginMiscLua.cpp \
+                  $(LOCAL_PATH)/../../../Classes/PluginMiscLuaHelper.cpp

+ LOCAL_CPPFLAGS := -DSDKBOX_ENABLED
  LOCAL_C_INCLUDES := $(LOCAL_PATH)/../../../Classes
+ LOCAL_WHOLE_STATIC_LIBRARIES := PluginMisc sdkbox

  # _COCOS_HEADER_ANDROID_BEGIN
  # _COCOS_HEADER_ANDROID_END
  include $(BUILD_SHARED_LIBRARY)

  $(call import-add-path, $(LOCAL_PATH)/../../../cocos2d)
+ $(call import-add-path, $(LOCAL_PATH))
  $(call import-module, cocos)
+ $(call import-module, ./sdkbox)
+ $(call import-module, ./PluginMisc)

  # _COCOS_LIB_IMPORT_ANDROID_BEGIN

```

- `./frameworks/runtime-src/Classes/lua_module_register.h`

register lua functions

```diff
  #endif

  #include "audioengine/lua_cocos2dx_audioengine_manual.h"
+ #ifdef SDKBOX_ENABLED
+ #include "PluginMiscLua.hpp"
+ #include "PluginMiscLuaHelper.h"
+ #endif
  #include "physics3d/lua_cocos2dx_physics3d_manual.h"

  static int lua_module_register(lua_State* L)
      ...

      register_audioengine_module(L);
+ #ifdef SDKBOX_ENABLED
+     register_all_PluginMiscLua(L);
+     register_all_PluginMiscLua_helper(L);
+ #endif
  #if CC_USE_3D_PHYSICS && CC_ENABLE_BULLET_INTEGRATION
      register_physics3d_module(L);
  #endif

```
