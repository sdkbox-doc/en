### Manual Integration

If you want to install Gameroom Plugin manually, you would modify more configurations step by step. It's a little perplex, we don't recommend you to do this.

1.  Find the Visual Studio Solution file(.sln) and open it. As for JS project, you can find it in "./framework/runtime\_src/proj.win32". We name the "proj.win32" **project-dir** for depict conveniently.

2.  Unzip the Gameromm Plugin package to get a dir including the plugin files. It's called **plugin-dir**.

3.  Copy header files. For JS project, copy `win32/include/*.h` in **plugin-dir** to `include/plugingameroom` in your **project-dir**.

4.  Copy library files `win32/libs/*.lib` in **plugin-dir** to `libs` in your **project-dir**.

5.  Deploy Facebook Gameroom SDK files.

    a.  Copy header files `sdk/fbg/*.h` in **plugin-dir** to `include/fbg` in your **project-dir**.

    b.  Copy library files `sdk/libs/*.lib` in **plugin-dir** to `libs` in your **project-dir**.

6.  For JS project, you should add some js-binding source. Copy them in `jsbindings` in **plugin-dir** to the dir `/Classes`, which is located in the upper of your **project-dir**.

7.  Modify the configuration of Visual Studio. Follow the steps as below:

    a.  Add an include directory for the compiler, click: project(on top bar) -> properties -> Configuration Properties -> VC++ Directories -> Include Directories (click and edit, add a new entry).

    And then add `$(solutiondir)include`.

    b.  Add a library directory for *.lib files, click: project(on top bar) -> properties -> Configuration Properties -> VC++ Directories -> Library Directories (click and edit, add a new entry).

    And then add `$(solutiondir)libs`.

    c.  Link the *.lib files, click: project(on top bar) -> properties -> Configuration Properties -> Linker -> Input -> Additional Dependencies (click and edit, add a new entry).

    And then add `GameroomPlugin32.lib` and `LibFBGPlatform32.lib`.

    **For `debug` version, Please add `GameroomPlugin32.debug.lib`**.

8.  Patch the `AppDelegate.cpp`. Open the `AppDelegate.cpp` in **project-dir**/Classes.

9.  **The following steps can also be fulfilled with `patch` tool**. The file `AppDelegate.js3.15.patch` in **plugin-dir** is for JS project.

```
patch AppDelegate.cpp ./plugin-dir/path/AppDelegate.js3.15.patch
```

-   Before `USING_NS_CC`, add the sdkbox header files:

```
#ifdef SDKBOX_ENABLED
#include "PluginGameroomJS.hpp"
#include "PluginGameroomJSHelper.h"
#endif
```

-   In the ctor and dtor of `AppDelegate`. Add redirect the STDOUT to a file since Facebook SDK don't offer any logging APIs.

```
AppDelegate::AppDelegate()
{
    freopen("fbg.log", "w", stdout);
}

AppDelegate::~AppDelegate()
{
    ...
    fclose(stdout);
}
```

-   And after the judgement statement `if (!glview)`, add these codes:

```
#if(CC_TARGET_PLATFORM == CC_PLATFORM_WP8) || (CC_TARGET_PLATFORM == CC_PLATFORM_WINRT)
    glview = cocos2d::GLViewImpl::create("cocos_gameroom_sample_js");
    director->setOpenGLView(glview);
#else
    const wchar_t title[]{ L"Facebook Gameroom" };
    auto parentWin = FindWindow(NULL, title);

    // set dpi for app
    auto res_dpi = SetProcessDPIAware();

    RECT rect;
    GetWindowRect(parentWin, &rect);
    glview = GLViewImpl::createWithRect("cocos_gameroom_sample_js", Rect(0, 0, rect.right - rect.left - 20, rect.bottom - rect.top - 100), 1.0f, true);
    director->setOpenGLView(glview);
    auto currentWin = Director::getInstance()->getOpenGLView()->getWin32Window();
    SetParent(currentWin, parentWin);
#endif
```

-   And register js-binding functions after statement `sc->addRegisterCallback(register_all_cocos2dx_3d_extension);`

```
#ifdef SDKBOX_ENABLED
    sc->addRegisterCallback(register_all_PluginGameroomJS);
    sc->addRegisterCallback(register_all_PluginGameroomJS_helper);
#endif
```

