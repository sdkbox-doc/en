[&#171; SDKBOX Home](http://sdkbox.com)

<h1>Integration Fyber to cocos2d-x project</h1>>

### Environment

* `Coco2dx-x 3.10`
* `SDKBox Installer` 1.0.0.18 [Install](http://docs.sdkbox.com/en/installer/)

### Steps

#### create project

* create empty cocos2d-x project by run `cocos new -l cpp -p com.sdkbox.sample.fyber fyber`

#### import fyber

* import fyber by run `sdkbox import fyber -p /path/to/the/empty/cocos2d-x/project`

#### add mediation

##### ios

* download adcolony mediation at [here](http://developer.fyber.com/content/current/ios/rewarded-video/adding-networks/)
* unzip adcolony mediation `Fyber_AdColony_2.6.2-r1.zip`

![](../imgs/fyber_mediation_adcolony_ios_files.png)

* drag and drop `Fyber_AdColony_2.6.2-r1.embeddedframework` to xcode project

![](../imgs/fyber_mediation_add_adcolony.png)

* open integration guide and follow it's steps

![](../imgs/fyber_mediation_adcolony_integration_guide.png)

* read `README.pdf` in foler `Fyber_AdColony_2.6.2-r1`
* add required framework

#### android

* download android adcolony mediation at [here](http://developer.fyber.com/content/current/android/rewarded-video/adding-networks/)

* open integration guide and follow it's steps
![](../imgs/fyber_mediation_adcolony_android_guide.png)

* copy `fyber-adcolony-2.3.6-r2.jar` to `proj.android/libs`
* copy `libs/armeabi/libImmEndpointWarpJ.so` to `proj.android/libs/armeabi`
* copy `libs/armeabi-v7a/libImmEndpointWarpJ.so` to `proj.android/libs/armeabi-v7a`
![](../imgs/fyber_mediation_adcolony_android_files.png)

* add activity to manifest

```xml
<activity
    android:name="com.jirbo.adcolony.AdColonyOverlay"
    android:configChanges="keyboardHidden|orientation|screenSize"
    android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen" />
<activity
    android:name="com.jirbo.adcolony.AdColonyFullscreen"
    android:configChanges="keyboardHidden|orientation|screenSize"
    android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
<activity
    android:name="com.jirbo.adcolony.AdColonyBrowser"
    android:configChanges="keyboardHidden|orientation|screenSize"
    android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen" />
```

##### website sitting

* entery Fyber [dashboard](https://dashboard.fyber.com/)
* enable reward, institial, banner

![](../imgs/fyber_mediation_enable_reward.png)

* add Adcolony network

![](../imgs/fyber_mediation_adcolony_network.png)


#### Compile Run

* compile and run fyber on ios by run `cocos run -p ios -s /path/to/fyer/project`
* compile and run fyber on android by run `cocos run -p android -s /path/to/fyer/project`


#### Add more mediation

* other mediation integration steps is same with Adcolony
