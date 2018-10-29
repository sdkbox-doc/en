<<[../shared/manual_android_v3.md]

- frameworks/runtime-src/Classes/*.cpp <- $PLUGIN_MISC_BUNDLE/plugin/jsbindings/*.cpp
- frameworks/runtime-src/Classes/*.h <- $PLUGIN_MISC_BUNDLE/plugin/jsbindings/*.h
- frameworks/runtime-src/Classes/*.hpp <- $PLUGIN_MISC_BUNDLE/plugin/jsbindings/*.hpp

if you use creator 1.7+, you should copy js binding file in jsb2:

- frameworks/runtime-src/Classes/*.cpp <- $PLUGIN_MISC_BUNDLE/plugin/jsbindings/jsb2/*.cpp
- frameworks/runtime-src/Classes/*.h <- $PLUGIN_MISC_BUNDLE/plugin/jsbindings/jsb2/*.h
- frameworks/runtime-src/Classes/*.hpp <- $PLUGIN_MISC_BUNDLE/plugin/jsbindings/jsb2/*.hpp

- proj.android/app/jni/Android.mk
```diff
                   $(LOCAL_PATH)/../../../Classes/AppDelegate.cpp \
-                  $(LOCAL_PATH)/../../../Classes/HelloWorldScene.cpp
+                  $(LOCAL_PATH)/../../../Classes/HelloWorldScene.cpp \
+                  $(LOCAL_PATH)/../../../Classes/SDKBoxJSHelper.cpp \
+                  $(LOCAL_PATH)/../../../Classes/PluginMiscJS.cpp \
+                  $(LOCAL_PATH)/../../../Classes/PluginMiscJSHelper.cpp

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

- `./frameworks/runtime-src/Classes/AppDelegate.cpp`

register javascript functions

```diff
  #endif
  
  USING_NS_CC;
+ #ifdef SDKBOX_ENABLED
+ #include "PluginMiscJS.hpp"
+ #include "PluginMiscJSHelper.h"
+ #endif
  
  AppDelegate::AppDelegate(int width, int height) : Application("Cocos Game", width, height)

  ...

  jsb_register_all_modules();
+ #ifdef SDKBOX_ENABLED
+     se->addRegisterCallback(register_all_PluginMiscJS);
+     se->addRegisterCallback(register_all_PluginMiscJS_helper);
+ #endif

  #if (CC_TARGET_PLATFORM == CC_PLATFORM_ANDROID || CC_TARGET_PLATFORM == CC_PLATFORM_IOS) && PACKAGE_AS
```
