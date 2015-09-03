Copy all source and header files from `plugin/luabindings/` to your projects `Classes` folder.

Add all `.cpp` files, that you just copied, to `Android.mk` in the __LOCAL_SRC_FILES__ section. Example
```
LOCAL_SRC_FILES := hellocpp/main.cpp \
                ../../Classes/AppDelegate.cpp \
                ../../Classes/HelloWorldScene.cpp \
								../../Classes/NewSourceFile.cpp
```
