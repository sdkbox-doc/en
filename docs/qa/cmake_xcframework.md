<h1>FAQ</h1>

## CMake XCFramework

As we all know, CocosCreator 3+ uses CMake to generate and build iOS/Android projects.

CMake does not support link xcframework. Therefore, we take xcframework as the framework and link to the `ios-i386_x86_64-simulator` framework in xcframework by default.


When you want to run on another architecture, you can manually switch to another architecture.

take a look at file `$CreatorProjectRoot/native/engine/ios/CMakeLists.txt`

Library ${LIB_NAME} is linked to ios simulator i386/x86_64
```CMake

LinkXCFramework("${CMAKE_CURRENT_LIST_DIR}/Firebase/FirebaseAnalytics/FirebaseCore.xcframework" ios-i386_x86_64-simulator ${LIB_NAME})

```

The library is now linked to the ios device armv7/arm64
```CMake

LinkXCFramework("${CMAKE_CURRENT_LIST_DIR}/Firebase/FirebaseAnalytics/FirebaseCore.xcframework" ios-armv7_arm64 ${LIB_NAME})

```

### Another Way

You can link xcframwork directly in the generated xcode project.
However, it should be noted that every generation operation in Creator may overwrite the xcode project.


[CMake XCFramework Issue](https://gitlab.kitware.com/cmake/cmake/-/issues/21752)

