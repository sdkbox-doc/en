<<[../shared/manual_android_v3.md]

- proj.android/app/jni/Android.mk
```diff
                   $(LOCAL_PATH)/../../../Classes/AppDelegate.cpp \
                   $(LOCAL_PATH)/../../../Classes/HelloWorldScene.cpp

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
