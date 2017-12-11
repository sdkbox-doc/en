Copy all source and header files from `plugin/jsbindings/` to your projects `Classes` folder.

**NOTE**: `plugin/jsbindings/jsb2` for creator 1.7.

Add all `.cpp` files, that you just copied, to `Android.mk` in the __LOCAL_SRC_FILES__ section. Example
```
LOCAL_SRC_FILES := hellocpp/main.cpp \
                  ../../Classes/AppDelegate.cpp \
                  ../../Classes/HelloWorldScene.cpp \
									../../Classes/NewSourceFile.cpp
```
