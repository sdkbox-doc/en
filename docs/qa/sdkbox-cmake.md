
# NOTE: plz keep PluginXXX before sdkbox

```
# PluginFacebook
# sdkbox
```

# CPP

  Plz add bellow code to the bottom of __PROJECT_ROOT__/CMakeLists.txt and replace PluginFacebook with your Plugin name

```cmake
# PluginFacebook
if(ANDROID)
    add_definitions(-DSDKBOX_ENABLED)
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/proj.android/app/jni/PluginFacebook/)
    target_link_libraries(${APP_NAME} ext_PluginFacebook)
endif()

# sdkbox
if(ANDROID)
    add_definitions(-DSDKBOX_ENABLED)
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/proj.android/app/jni/sdkbox/)
    target_link_libraries(${APP_NAME} ext_sdkbox)
endif()
```


# JS

  1. Plz add bellow code to the bottom of __PROJECT_ROOT__/CMakeLists.txt and replace PluginFacebook with your plugin name

```cmake
# PluginFacebook
if(ANDROID)
    add_definitions(-DSDKBOX_ENABLED)
    add_subdirectory(${RUNTIME_SRC_ROOT}/proj.android/app/jni/PluginFacebook/)
    target_link_libraries(${APP_NAME} ext_PluginFacebook)
endif()
# sdkbox
if(ANDROID)
    add_definitions(-DSDKBOX_ENABLED)
    add_subdirectory(${RUNTIME_SRC_ROOT}/proj.android/app/jni/sdkbox/)
    target_link_libraries(${APP_NAME} ext_sdkbox)
endif()
```

  2. Plz add bellow code before `set(APP_SRC ${GAME_HEADER} ${GAME_SOURCE})`, and replace `PluginFacebook` with your plugin name

```cmake
# PluginFacebook-JS
if(ANDROID)
    list(APPEND GAME_SOURCE ${RUNTIME_SRC_ROOT}/Classes/PluginFacebookJS.cpp)
    list(APPEND GAME_SOURCE ${RUNTIME_SRC_ROOT}/Classes/PluginFacebookJSHelper.cpp)
endif()
# sdkbox-JS
if(ANDROID)
    list(APPEND GAME_SOURCE ${RUNTIME_SRC_ROOT}/Classes/SDKBoxJSHelper.cpp)
endif()
```

# Lua

  1. Plz add bellow code to the bottom of __PROJECT_ROOT__/CMakeLists.txt and replace PluginFacebook with your plugin name

```cmake
# PluginFacebook
if(ANDROID)
   add_definitions(-DSDKBOX_ENABLED)
   add_subdirectory(${RUNTIME_SRC_ROOT}/proj.android/app/jni/PluginFacebook/)
   target_link_libraries(${APP_NAME} ext_PluginFacebook)
endif()
# sdkbox
if(ANDROID)
   add_definitions(-DSDKBOX_ENABLED)
   add_subdirectory(${RUNTIME_SRC_ROOT}/proj.android/app/jni/sdkbox/)
   target_link_libraries(${APP_NAME} ext_sdkbox)
endif()
```

  2. Plz add bellow code before `set(APP_SRC ${GAME_HEADER} ${GAME_SOURCE})`, and replace `PluginFacebook` with your plugin name

```cmake
# PluginFacebook-Lua
if(ANDROID)
   list(APPEND GAME_SOURCE ${RUNTIME_SRC_ROOT}/Classes/PluginFacebookLua.cpp)
   list(APPEND GAME_SOURCE ${RUNTIME_SRC_ROOT}/Classes/PluginFacebookLuaHelper.cpp)
endif()
# sdkbox-Lua
if(ANDROID)
   list(APPEND GAME_SOURCE ${RUNTIME_SRC_ROOT}/Classes/SDKBoxLuaHelper.cpp)
endif()
```


# IOS

## IAP example

```
if(IOS)
add_definitions(-DSDKBOX_ENABLED)
message(${CMAKE_CURRENT_SOURCE_DIR}/proj.ios_mac)
find_host_library(F_IAP
    NAMES PluginIAP
    PATHS ${CMAKE_CURRENT_SOURCE_DIR}/proj.ios_mac
    )
message(STATUS "F_IAP: ${F_IAP}") # print find libs result
target_link_libraries(${APP_NAME} ${F_IAP} "-framework SystemConfiguration" "-framework StoreKit")
endif()

if(IOS)
find_host_library(F_SDKBOX
    NAMES sdkbox
    PATHS ${CMAKE_CURRENT_SOURCE_DIR}/proj.ios_mac
    )
message(STATUS "F_SDKBOX: ${F_SDKBOX}") # print find libs result

target_link_libraries(${APP_NAME} ${F_SDKBOX})
endif()
```
