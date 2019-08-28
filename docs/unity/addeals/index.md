# Unity plugin for AdDeals

This is a cross-platform Unity plugin for [AdDeals](https://www.addealsnetwork.com/)'s SDKs. It combines and supports three platforms together: Windows(UWP), iOS, and Android.

System requirements:

* Unity v5.5.4.p5 or later
* Vistual Studio 2017 or later
* Xcode 10 or later
* Android Studio 3.2.1 or later



## Integrate

* In order to get your AppID  & AppKey you must first create an account on http://www.addealsnetwork.com
* Then add your iOS / Android / Windows 10 apps and you will get 1 AppID / AppKey for each app version.
* <font color=#FF0000>Download</font> the AdDeals plugin from either [Unity Asset Store](http://u3d.as/1p2y), or [SDKBox repo](https://github.com/sdkbox/AdDeals-Unity-Plugin/).
* Drag `Assets\AdDeals\AdDeals.prefab` onto your game scene.
* Call AdDeals SDK APIs. Please check out the sample codes in `Assets\AdDeals\Sample\Test.cs`:
```
AdDeals.AdDealsWrapper.Init("AppID", "AppKey");

int adType = AdDealsWrapper.AdTypeInterstitial; // 1:interstitial 2: rewarded video
AdDeals.AdDealsWrapper.ShowAd(adType);
```


### Windows UWP build

* Support the lastest AdDeals SDK for Windows:  [AdDealsUniversalSDKW81](https://www.nuget.org/packages/AdDealsUniversalSDKW81).
* Using .Net ScriptBackend, please export the UWP <font color=#FF0000>project (project)</font> in Unity with the following settings:

![Unity UWP project config](./unity_project_config.png)

* Or using il2cpp ScriptBackend, please export the project in Unity 2018 or later with following settings:

![Unity UWP project config](./unity_il2cpp_project_config.png)

* Please enable `InternetClient`.

Unity 2019+ UWP capabilities path: `Project Settings` > `Player` > `Publisher settings` > `Capabilities`.

![Unity UWP capabilities setting](./uwp_capabilities_unity_2019.png)

Unity 5.5+ UWP capabilities path: `PlayerSetting`->`Universal Windows Platform`->`Publishing Setting`->`Capabilities`.

![Unity UWP capabilities setting](./uwp_capabilities.png)

* For Unity 5.x: if you want to build UWP application, please use Unity 5.5.4p5 or later. you can download [Unity Patch Releases](https://unity3d.com/unity/qa/patch-releases).


### iOS build

* From Unity, first export to an iOS project. Next build and run it using Xcode.
* Support iOS 8+.
* you must add a script phase to Xcode `AdDeals.framework`

    1. new script phase, and name it `StripAdDeals`

![Unity iOS new script phase](./unity_addeals_ios_new_script_phase.png)

    2. add follow script

```bash
    strip_invalid_archs() {
        binary="$1"
        # Get architectures for current target binary
        binary_archs="$(lipo -info "$binary" | rev | cut -d ':' -f1 | awk '{$1=$1;print}' | rev)"
        # Intersect them with the architectures we are building for
        intersected_archs="$(echo ${ARCHS[@]} ${binary_archs[@]} | tr ' ' '\n' | sort | uniq -d)"
        # If there are no archs supported by this binary then warn the user
        if [[ -z "$intersected_archs" ]]; then
            echo "warning: [CP] Vendored binary '$binary' contains architectures ($binary_archs) none of which match the current build architectures ($ARCHS)."
            STRIP_BINARY_RETVAL=0
            return
        fi
        stripped=""
        for arch in $binary_archs; do
            if ! [[ "${ARCHS}" == *"$arch"* ]]; then
                # Strip non-valid architectures in-place
                lipo -remove "$arch" -output "$binary" "$binary" || exit 1
                stripped="$stripped $arch"
            fi
        done
        if [[ "$stripped" ]]; then
            echo "Stripped $binary of architectures:$stripped"
        fi
        STRIP_BINARY_RETVAL=1
    }

    binary="${TARGET_BUILD_DIR}/${FRAMEWORKS_FOLDER_PATH}/AdDeals.framework/AdDeals"

    # Strip invalid architectures so "fat" simulator / device frameworks work on device
    if [[ "$(file "$binary")" == *"dynamically linked shared library"* ]]; then
        strip_invalid_archs "$binary"
    fi
```

and the script phase should be look like follow

![Unity iOS script phase](./unity_addeals_strip_script_phase.png)


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


* Initialize the AdDeals SDK.

```
void AdDeals.AdDealsWrapper.Init(String appID, String appKey);
```

* Set privacy policy consent.

```
void AdDeals.AdDealsWrapper.SetConsent(int consent);
```

* Check availability.

```
void AdDeals.AdDealsWrapper.IsCachedAdAvailable(int adType, int uiOrientation);
```

* `uiOrientation`: when used with adType, lets you indicating if you would prefer getting a video ad whose content is horizontal (most common case) or vertical. Be aware that you aren't giving here a restriction, just a preference. Otherwise, simply pass the AdDealsWrapper.UIOrientationUnset value.

* Cache Ad.

```
void AdDeals.AdDealsWrapper.CacheAd(int adType, string placementID, int uiOrientation);
```

* `placementID`: optional AdDeals ad placement ID generated for your app (on demand). If not wanted to be used, leave it empty (""). 
* `uiOrientation`: when used with adType, lets you indicating if you would prefer getting a video ad whose content is horizontal (most common case) or vertical. Be aware that you aren't giving here a restriction, just a preference. Otherwise, simply pass the AdDealsWrapper.UIOrientationUnset value.

* Show Ad.

```
void AdDeals.AdDealsWrapper.ShowAd(int adType, string placementID, int uiOrientation);
```

* `placementID`: optional AdDeals ad placement ID generated for your app (on demand). If not wanted to be used, leave it empty (""). 
* `uiOrientation`: when used with adType, lets you indicating if you would prefer getting a video ad whose content is horizontal (most common case) or vertical. Be aware that you aren't giving here a restriction, just a preference. Otherwise, simply pass the AdDealsWrapper.UIOrientationUnset value.

__Note__: placementID is an advanced feature and in most cases you can just leave it "". In case you want to use placementIDs you should contact addeals@ahead-solutions.com

### Callback

SDK trigers feedback events (callbacks) notifying the client app when action are performed (either by SDK or end user; typically when there is an ad being shown/clicked/closed) or when failures occur. Following is the exhaustive listing of exposed callbacks :

```
public static event AdAvailableHandler AdAvailableEvent;
public static event AdEventHandler SDKNotInitializedEvent;
public static event AdEventHandler ShowAdVideoRewardedGrantedEvent;
public static event AdEventHandler ShowAdSuccessEvent;
public static event AdEventStringHandler ShowAdFailedEvent;
public static event AdEventHandler CacheAdSuccessEvent;
public static event AdEventStringHandler CacheAdFailedEvent;
public static event AdEventHandler MinDelayBtwAdsNotReachedEvent;
public static event AdEventHandler AdClosedTap;
public static event AdEventHandler AdClickedTap;
public static event AdEventHandler AdManagerInitSDKSuccess;
public static event AdEventStringHandler AdManagerInitSDKFailed;
public static event AdEventHandler AdManagerConsentSuccess;
public static event AdEventStringHandler AdManagerConsentFailed;
public static event AdEventHandler AdManagerAppDownloadSourceDetected;
public static event AdEventHandler AdManagerAppSessionSourceDetected;
```

here is a sample to subscribe SDK init success:

* define a function
```
void AdManagerInitSDKSuccess() {
    //addeals init success
}
```

* let the upper function subscribe SDK init success event
```
AdDeals.AdDealsWrapper.AdManagerInitSDKSuccess += AdManagerInitSDKSuccess;
```

* when sdk init success, AdManagerInitSDKSuccess will be called.

### Constants

#### UI Orientation
```
AdDealsWrapper.UIOrientationUnset;
AdDealsWrapper.UIOrientationPortrait;
AdDealsWrapper.UIOrientationLandscape;
```

#### Ad type
```
AdDealsWrapper.AdTypeInterstitial;
AdDealsWrapper.AdTypeRewardedVideo;
```

#### Consent
```
public const int UserConsentNotApplicable;
public const int UserConsentRevoke;
public const int UserConsentGrant;
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


