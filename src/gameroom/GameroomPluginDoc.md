#Gameroom Plugin Doc

## Preface
Facebook Gameroom is an entertainment platform based on **Windows(only)**, including thousands of games downloading, players community, games publishing and other more services.

Gameroom SDK is officially offered by Facebook in a bid to make developers releasing their games to Gameroom convenient. **But Now the SDK is in Beta.**

As SDKBOX should offer more plugins to serve more users, our team will pack the Gameroom SDK as a SDKBOX Plugin, uniforming its APIs and optimizing it on Cocos2d-X and other engines.

## SDKBOX Gameroom Plugin Design
A serial of plugins in SDKBOX have similar architecture:

First, Initialize SDKBOX and set callback listeners via SDKBOX Plugins APIs; Secondary, calling SDKBOX APIs to execute the original SDK function directly; And then the results and events of the execution will be handled by callback Listeners set in first step.

This illumination shows the process clearly(from [http://docs.sdkbox.com/en/](http://docs.sdkbox.com/en/)):

![SDKBOX Plugin](http://docs.sdkbox.com/en/imgs/sdkbox_sequence.jpg)

The original SDKs usually create **another thread** to callback Listeners, in the light of that, SDKBOX don’t need to care about how to implement callback APIs, just encapsulate the APIs and offer them to users. it is more different from Facebook Gameroom SDK.

According to Facebook Gameroom SDK docs, though it doesn’t demonstrate directly, the SDK can’t handle the result and events in an individual thread but in game loop.

For example, with Facebook Gameroom SDK, the implementation of IAP could be like this:

![](iap sequence diagram.png)

As SDKBOX can’t make any impacts to Game Engines, ex., Cocos2d-X, in other words, any internal game loop can’t be affected by SDKBOX plugins. it is a big headache in encapsulation of Gameroom SDK. SDKBOX Gameroom Plugin should **create a new thread** to handle Gameroom Messages(callbacks).

The SDKBOX Gameroom Plugin should work as below:

![SDKBOX Gameroom Plugin IAP Sequence Diagrams.png](images/image1.png)

## Finished Functions

Now, SDKBOX Gameroom Plugin has these functions:

*   user login
*   *feed shared (function test normally but the returned value is always 0)*
*   IAP
    *   IAP with product ID
    *   IAP with a URL link
    *   *purchase premium version or license (function test failed in Gameroom SDK)*
*   *App Events (crash in Gameroom SDK when no user login)*
*   App Request
    *    send requests to fixed person
    *    send requests to chosen person via a Facebook dialog

>   The functions in *italic* have some problem(Facebook Gameroom SDK is still in Beta version), which needs help from Facebook.

## Integration

## Integration with Cocos Project

### Using SDKBOX Installer (recommend)

With SDKBOX installer, you can install SDKBOX Gameroom Plugin in **Windows** easily.

1.  Get SDKBOX Installer

    ``` shell
python -c "import urllib; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/install/install.py').read(); exec s"
    ```
Access [SDKBOX official website](http://www.sdkbox.com) for more information.

2.  Import Gameroom Plugin
    ```shell
    sdkbox import gameroom
    ```
Or, if the gameroom plugin is in local, you can also import it like this:
    ```shell
sdkbox import -b c:\the_path_to_gameroom_plugin\sdkbox-gameroom_v0.01
    ```

### Manual Integration

If you want to install Gameroom Plugin manually, you would modify more configurations step by step. It’s a little perplex, we don’t recommend you to do this.

1.  Find the Visual Studio Solution file(.sln) and open it. For Cpp project created by “cocos”, you can find the solution file in "./proj.win32" sub-directory; As for JS project, you can find it in "./framework/runtime_src/proj.win32". We name the "proj.win32" **project-dir** for depict conveniently.

2.  Unzip the Gameromm Plugin package to get a dir including the plugin files. It’s called **plugin-dir**.

3.  Copy header files.
    a.  For cpp project, copy “win32/include/*.h” in **plugin-dir** to “include” in your **project-dir**.

    b.  If your project is in JS, copy “win32/include/*.h” in **plugin-dir** to “include/plugingameroom” in your **project-dir**.

4.  Copy library files “win32/libs/*.lib” in **plugin-dir** to “libs” in your **project-dir**.

5.  Deploy Facebook Gameroom SDK files.
    a.  Copy header files “sdk/fbg/*.h” in **plugin-dir** to “include/fbg“ in your **project-dir**.

    b.  Copy library files “sdk/libs/*.lib” in **plugin-dir** to “libs” in your **project-dir**.

6.  **OPTIONAL: ** For JS project, you should add some js-binding source. Copy them in “jsbindings” in **plugin-dir** to the dir “/Classes” in **project-dir**, which is located in the upper of your **project-dir**.

7.  Modify the configuration of Visual Studio. Follow the steps as below:
    a.  Add an include directory for the compiler, click: project(on top bar) -> properties -> Configuration Properties -> VC++ Directories -> Include Directories (click and edit, add a new entry).

    And then add `$(solutiondir)include`.

    b.  Add a library directory for *.lib files, click: project(on top bar) -> properties -> Configuration Properties -> VC++ Directories -> Library Directories (click and edit, add a new entry).

    And then add “$(solutiondir)libs”.

    c.  Link the *.lib files, click: project(on top bar) -> properties -> Configuration Properties -> Linker -> Input -> Additional Dependencies (click and edit, add a new entry).

    And then add “GameroomPlugin32.lib” and “LibFBGPlatform32.lib”.

    For “debug” version, Please add “GameroomPlugin32.debug.lib”.

8.  Patch the “AppDelegate.cpp”. The following steps can be also fulfilled with “patch” tool.

    For Cpp project, please use “AppDelegate.cpp3.15.patch” in plugin-dir. Open the “AppDelegate.cpp” in project-dir/Classes.

    a.  Before “USING_NS_CC”, add the sdkbox header files:

    ```cpp
    #ifdef SDKBOX_ENABLED
    #include “PluginGameroom.h”
    #endif
    ```

    b.  In the ctor and dtor of “AppDelegate”. Add redirect the STDOUT to a file since Facebook SDK don’t offer any logging APIs.

    ```cpp
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

    c.  At beginning of the function “applicationDidFinishLaunching”, initialize the SDKBOX Gameroom Plugin:

    ```cpp
    #ifdef SDKBOX_ENABLED
    sdkbox::PluginGameroom::init(“your_app_id”);
    #endif
    ```

    d.  And after the judgement statement “if (!glview)”, add these codes:

    ```cpp
    #if (CC_TARGET_PLATFORM == CC_PLATFORM_WIN32) || (CC_TARGET_PLATFORM == CC_PLATFORM_MAC) || (CC_TARGET_PLATFORM == CC_PLATFORM_LINUX)
        const wchar_t title[]{ L"Facebook Gameroom" };
        auto parentWin = FindWindow(NULL, title);

        // set dpi for app.
        auto res_dpi = SetProcessDPIAware();

        RECT rect;
        GetWindowRect(parentWin, &rect);
        glview = GLViewImpl::createWithRect("my_ccs-cpp", Rect(0, 0, rect.right - rect.left - 20, rect.bottom - rect.top - 100), 1.0f, true);
        director->setOpenGLView(glview);
        auto currentWin = Director::getInstance()->getOpenGLView()->getWin32Window();
        SetParent(currentWin, parentWin);
    #else
        glview = GLViewImpl::create("my_ccs-cpp");
        director->setOpenGLView(glview);
    #endif
    ```

    Another patch file “AppDelegate.js3.15.patch” is for JS project.

    a.  Open the “AppDelegate.cpp” in project-dir/Classes.

    b.  Before “USING_NS_CC”, add the sdkbox header files:

    ```cpp
    #ifdef SDKBOX_ENABLED
    #include “PluginGameroomJS.hpp”
    #include “PluginGameroomJSHelper.h
    #endif
    ```

    c.  In the ctor and dtor of “AppDelegate”. Add redirect the STDOUT to a file since Facebook SDK don’t offer any logging APIs.

    ```cpp
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

    d.  And after the judgement statement “if (!glview)”, add these codes:


    ```cpp
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

    e.  And register js-binding functions after statement “sc->addRegisterCallback(register_all_cocos2dx_3d_extension);”

    ```cpp
    #ifdef SDKBOX_ENABLED
        sc->addRegisterCallback(register_all_PluginGameroomJS);
        sc->addRegisterCallback(register_all_PluginGameroomJS_helper);
    #endif

    ```

## <span class="c10">Integration with Cocos Creator</span>

<span class="c4">TBD</span>

<span class="c4"></span>

# <span class="c2">SDKBOX Gameroom Plugin APIs</span>

## <span class="c10">Initialization / Destroy API</span>

### <span>static void sdkbox::PluginGameroom::init() </span>

<span class="c4">-- initialize Gameroom SDK and create a thread to handle Gameroom messages(callbacks).</span>

## <span class="c10">Facebook Gameroom Messages APIs</span>

### <span class="c11">
static FBGAccessTokenHandle sdkbox::PluginGameroom::handleAccessTokenMessage(FBGMessageObj obj);</span>

### <span class="c11">static FBGFeedSharedHandle sdkbox::PluginGameroom::handleFeedSharedMessage(FBGMessageObj obj);</span>

<span class="c4"></span>

### <span class="c11">static FBGPurchaseHandle sdkbox::PluginGameroom::handlePurchaseMessage(FBGMessageObj obj);</span>

<span class="c4">…</span>

<span class="c4"></span>

## <span class="c10">Access Token Handling APIs</span>

### <span class="c11">bool sdkbox::PluginGameroom::accessTokenIsValid(const FBGAccessTokenHandle obj);</span>

### <span class="c11">FBGFacebookID sdkbox::PluginGameroom::accessTokenGetUserID(const FBGAccessTokenHandle obj);</span>

### <span class="c11">size_t sdkbox::PluginGameroom::accessToken_GetTokenString(const FBGAccessTokenHandle obj, char* buffer, size_t bufferIn);</span>

<span class="c4"></span>

### <span class="c11">uint64_t accessTokenGetExpirationTimestamp(const FBGAccessTokenHandle obj);</span>

### <span class="c11">size_t &nbsp;accessTokenGetPermissions(const FBGAccessTokenHandle obj, fbgLoginScope* buffer, size_t bufferIn);</span>

<span class="c4"></span>

<span class="c4"></span>

## <span class="c10">IAP APIs</span>

### <span class="c11">static size_t sdkbox::PluginGameroom::purchaseGetPaymentID(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj,</span>

<span class="c4">&nbsp; char* buffer,</span>

<span class="c4">&nbsp; size_t bufferIn</span>

<span class="c4">);</span>

<span class="c4"></span>

### <span class="c11">static uint32_t sdkbox::PluginGameroom::purchaseGetAmount(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj</span>

<span class="c4">);</span>

<span class="c4"></span>

<span class="c4"></span>

### <span class="c11">static size_t sdkbox::PluginGameroom::purchaseGetCurrency(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj,</span>

<span class="c4">&nbsp; char* buffer,</span>

<span class="c4">&nbsp; size_t bufferIn</span>

<span class="c4">);</span>

<span class="c4"></span>

### <span class="c11">static uint64_t sdkbox::PluginGameroom::purchaseGetPurchaseTime(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj</span>

<span class="c4">);</span>

<span class="c4"></span>

### <span class="c11">static size_t sdkbox::PluginGameroom::purchaseGetProductId(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj,</span>

<span class="c4">&nbsp; char* buffer,</span>

<span class="c4">&nbsp; size_t bufferIn</span>

<span class="c4">);</span>

<span class="c4"></span>

<span class="c4"></span>

### <span class="c11">static size_t sdkbox::PluginGameroom::purchaseGetPurchaseToken(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj,</span>

<span class="c4">&nbsp; char* buffer,</span>

<span class="c4">&nbsp; size_t bufferIn</span>

<span class="c4">);</span>

<span class="c4"></span>

### <span class="c11">static uint32_t sdkbox::PluginGameroom::purchaseGetQuantity(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj</span>

<span class="c4">);</span>

### <span class="c11">static size_t sdkbox::PluginGameroom::purchaseGetRequestId(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj,</span>

<span class="c4">&nbsp; char* buffer,</span>

<span class="c4">&nbsp; size_t bufferIn</span>

<span class="c4">);</span>

### <span class="c11">static size_t sdkbox::PluginGameroom::purchaseGetStatus(</span>

<span class="c4">&nbsp; const FBGPurchaseHandle obj,</span>

<span class="c4">&nbsp; char* buffer,</span>

<span class="c4">&nbsp; size_t bufferIn</span>

<span class="c4">);</span>

<span class="c4"></span>

## <span class="c10">Trialware Purchase APIs</span>

<span class="c4">TBD</span>

<span class="c4"></span>

## <span class="c10">Share Feed APIs</span>

<span class="c4">TBD</span>

## <span class="c10">App Events APIs</span>

<span class="c4">TBD</span>

<span class="c4"></span>

## <span class="c10">Listeners</span>

### <span class="c11">void onMessages(FBGMessageObj obj)</span>
