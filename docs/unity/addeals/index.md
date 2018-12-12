# Unity plugin for AdDeals

This is a cross-platform Unity plugin for [AdDeals](https://www.addealsnetwork.com/)'s SDKs. It combines and supports three platforms together: Windows(UWP), iOS, and Android.

System requirements:

* Unity v5.5.4.p5 or later
* Vistual Studio 2017 or later
* Xcode 10
* Android Studio 3.2.1



## Integrate

* Downlonad the AdDeals plugin from either Unity's marketplace, or sdkbox.com. 
* Drag `Assets\AdDeals\AdDeals.prefab` onto your game scene.
* Call AdDeals SDK APIs. Please check out the sample codes in `Assets\AdDeals\Sample\Test.cs`: 
```
AdDeals.AdDealsWrapper.Init("AppID", "AppSecert");

int adType = 1; // 1:interstitial 2: reward
AdDeals.AdDealsWrapper.ShowPopupAd(adType);
```


### Windows UWP build

* Support the lastest AdDeals SDK for Windows:  [AdDealsUniversalSDKW81](https://www.nuget.org/packages/AdDealsUniversalSDKW81).
* Using .Net ScriptBackend, please export the UWP proejct in Unity with the following settings: 

    ![Unity UWP project config](./unity_project_config.png)

* Please enable `InternetClient` setting for UWP under `PlayerSetting`->`Universal Windows Platform`->`Publishing Setting`->`Capabilities`

    ![Unity UWP capabilities setting](./uwp_capabilities.png)

* For Unity 5.x: because Vistual Studio 2017 is required for UWP application to target aginest the lastest UWP SDK, please make sure to install the [Unity Patch Releases](https://unity3d.com/unity/qa/patch-releases) with UWP support.



### iOS build

* From Unity, first export to an iOS project. Next build and run it using xCode. 
* Support iOS 8+. 


### Android build

* From Unity, first export the application to a Gradle project. Next build and run it using Android Studio. __Do NOT build APK directly in Unity.__

       ![](./unity_android_export.png)

* Support Android SDK v15+.
* For Unity 5.x: please edit `YOUR_EXPORTS_PROTECT_ROOT/build.gradle` with the following configurations:
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



## API

### Methods


```
void AdDeals.AdDealsWrapper.Init(String appID, String appKey);
```
* Initialize the AdDeals SDK.

```
void AdDeals.AdDealsWrapper.SetConsent(int consent);
```
* Set privacy policy consent.

```
void AdDeals.AdDealsWrapper.IsAvailable(int adType, int uiOrientation);
```
* Check availability.
* `uiOrientation` is invalid on UWP. Set to `AdDealsWrapper.UIOrientationUnknown`. 

```
void AdDeals.AdDealsWrapper.CacheAdByType(int adType, string placement, int uiOrientation);
```
* Cache Ad.
* `placement` is invalid on UWP, set to "".
* `uiOrientation` is invalid on UWP, set to `AdDealsWrapper.UIOrientationUnknown`. 

```
void AdDeals.AdDealsWrapper.ShowPopupAd(int adType, string placement, int uiOrientation);
```
* Show Ad. 
* `placement` is invalid on UWP, set to "".
* `uiOrientation` is invalid on UWP, set to `AdDealsWrapper.UIOrientationUnknown`.


### Constants

#### UI Orientation
```
AdDealsWrapper.UIOrientationUnknown = 0;
AdDealsWrapper.UIOrientationPortrait = 1;
AdDealsWrapper.UIOrientationPortraitUpsideDown = 2;
AdDealsWrapper.UIOrientationLandscapeRight = 3;
AdDealsWrapper.UIOrientationLandscapeLeft = 4;
```

#### Ad type
```
AdDealsWrapper.AdTypeInterstitial = 1;
AdDealsWrapper.AdTypeRewardVideo = 2;
```


## Verification

Tested on the follow Unity versions:

* Unity v2018.2.16f
* Unity v2018.1.0f2
* Unity v2017.1.2f1
* Unity v2017.1.0p5
* Unity v5.5.4p5


## Sample Project

[https://github.com/sdkbox/AdDeals-Unity-Sample](https://github.com/sdkbox/AdDeals-Unity-Sample)


## Issues

* if you got follow error when import this unitypackage, it's ok, you can ignore it.

![](./unity_addeals_framework_import_error.png)


