# AdDeals For Unity

this is a AdDeals Unity plugin. now this plugin support Unity 5.5.4p5+.

Note: if you are use Unity 5.x, please upgrade use Unity 5.x patch version.

## Integrate

* drag `Assets/AdDeals/AdDeals.prefab` to your game scene
* Invoke AdDeals SDK API. take a look at sample code file `Assets/AdDeals/Sample/Test.cs`

```csharp
AdDeals.AdDealsWrapper.Init("AppID", "AppSecert");

int adType = 1; // 1:interstitial 2: reward
AdDeals.AdDealsWrapper.ShowPopupAd(adType);
```


### iOS

min support iOS: 8


### Android

min support android sdk: 15

this plugin is not support build APK directly in Unity.

please export Gradle Project, and build&run with Android Studio.

![](./unity_android_export.png)

#### For Unity 5.x

if you use Unity 5.x, please check `YOUR_EXPORTS_PROTECT_ROOT/build.gradle`, make it look like follow:

```gradle
    ...
    android {
        ...
        defaultConfig {
            minSdkVersion 15
            targetSdkVersion 28
            versionCode 1
            versionName '0.1'
            ...
        }
        ...
    }
    ...
```




### Windows UWP

* the plugin is base on [AdDealsUniversalSDKW81](https://www.nuget.org/packages/AdDealsUniversalSDKW81).

* we support Windows UWP with C# Project with .Net ScriptBackend. please make sure your export UWP proejct setting like follow.

    ![Unity UWP project config](./unity_project_config.png)

* enable InternetClient on UWP, you can find it with follow path `PlayerSetting`->`Universal Windows Platform`->`Publishing Setting`->`Capabilities`

    ![Unity UWP capabilities setting](./uwp_capabilities.png)

* UWP application target aginest the lastest UWP SDK must use `Vistual Studio 2017`, so if you use Unity 5.x, please make sure use [Unity patch version](https://unity3d.com/unity/qa/patch-releases).


## API

// Init AdDeals

* void AdDeals.AdDealsWrapper.Init(String appID, String appKey);

// set privacy policy consent

* void AdDeals.AdDealsWrapper.SetConsent(int consent);

// check is ad available
// params uiOrientation is invalid on UWP, send 0

* void AdDeals.AdDealsWrapper.IsAvailable(int adType, int uiOrientation);

// cache ad
// params placement is invalid on UWP, send ""
// params uiOrientation is invalid on UWP, send 0

* void AdDeals.AdDealsWrapper.CacheAdByType(int adType, string placement, int uiOrientation);

// show ad
// params placement is invalid on UWP, send ""
// params uiOrientation is invalid on UWP, send 0

* void AdDeals.AdDealsWrapper.ShowPopupAd(int adType, string placement, int uiOrientation);



## Versions

* Version 0.0.4

Release Date: 2018.12.10

fix xcode project issue on unity 5.5


* Version 0.0.3

Release Date: 2018.12.10

support iOS & Android


* Version 0.0.2

Release Date: 2018.11.30

support Unity 5.5.4+ patch release version


* Version 0.0.1

Release Date: 2018.11.23

first version, support Unity 2017+ with UWP

## Tested Unity Version

Haved Tested With Follow Unity Version:

* Unity 2018.2.16f
* Unity 2018.1.0f2
* Unity 2017.1.2f1
* Unity 2017.1.0p5
* Unity 5.5.4p5
