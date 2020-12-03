[&#171; SDKBOX Home](http://sdkbox.com)

<h1>SDKBOX for Cocos Creator</h1>

## How to integrate SDKBox Plugin to Cocos Creator project
---

### Environment

Before you start, make sure you have both CocosCreator and SDKBox Installer

* `CocosCreator` [Install](http://www.cocos.com/creator)
* `SDKBox Installer` [Install](http://docs.sdkbox.com/en/installer/)

### Create new Cocos Creator Project

Create Project `SDKBoxTutorial` like follow:
![](../imgs/ccc_tutorial_create_project.png)

### Add buttons

add two button to scene, design ui like follow:
![](../imgs/ccc_tutorial_ui_design.png)

### Create JavaScript Component

create javascript commponent, name it `AdMob.js`, i will integrate `AdMob` the this project. add three empty function to `AdMob.js`, also add admob initialize code in `onLoad` function like follow:

```js
cc.Class({

    ...

    onLoad: function () {
        //Add this line to onLoad
        this.admobInit();
    },

    ...

    admobInit: function() {
        //finish it after import admob, let it empty for now
    },

    cacheInterstitial: function() {
        //finish it after import admob, let it empty for now
    },

    showInterstitial: function() {
        //finish it after import admob, let it empty for now
    },

    ...

});
```

### Attach AdMob.js to Canvas

![](../imgs/ccc_tutorial_canvas_script.png)

### associate button click event to AdMob.js

![](../imgs/ccc_tutorial_btn_cache_script.png)
![](../imgs/ccc_tutorial_btn_show_script.png)

### Run In Simulator

check if every thing is ok.


### Build Project

open build window
Menu->Project->Build or (Command + Shift + B)

Build iOS

![](../imgs/ccc_tutorial_build_win.png)

Build Android

![](../imgs/ccc_tutorial_build_android.png)

Build->Compile

Make sure everything is okey
![](../imgs/ccc_tutorial_console_compile_result.png)


### Import AdMob to CocosCreate project

* open console
* entry CocosCreate project by run `cd SDKBoxTutorial`
* import admob by run `sdkbox import admob -p ./build/jsb-default/`

![](../imgs/ccc_tutorial_import_admob_result.png)

### Configuration AdMob

* configure `./build/jsb-default/res/sdkbox_config.json` with your ad id

`Important`: Make sure backup `sdkbox_config.json`, `./build/jsb-default/res` will be removed every time after Build Project in Cocos Creator build windows

### Finish AdMob.js empty function

```js
cc.Class({

    ...

    admobInit: function() {
        if(cc.sys.isMobile) {
            var self = this
            sdkbox.PluginAdMob.setListener({
                adViewDidReceiveAd: function(name) {
                    self.showInfo('adViewDidReceiveAd name=' + name);
                },
                adViewDidFailToReceiveAdWithError: function(name, msg) {
                    self.showInfo('adViewDidFailToReceiveAdWithError name=' + name + ' msg=' + msg);
                },
                adViewWillPresentScreen: function(name) {
                    self.showInfo('adViewWillPresentScreen name=' + name);
                },
                adViewDidDismissScreen: function(name) {
                    self.showInfo('adViewDidDismissScreen name=' + name);
                },
                adViewWillDismissScreen: function(name) {
                    self.showInfo('adViewWillDismissScreen=' + name);
                },
                adViewWillLeaveApplication: function(name) {
                    self.showInfo('adViewWillLeaveApplication=' + name);
                }
            });
            sdkbox.PluginAdMob.init();
        }
    },

    cacheInterstitial: function() {
        if(cc.sys.isMobile) {
            sdkbox.PluginAdMob.cache('gameover');
        }
    },

    showInterstitial: function() {
        if(cc.sys.isMobile) {
            sdkbox.PluginAdMob.show('gameover');
        }
    },

    ...

});
```

### Build Cocos Creator Again

Menu->Project->Build or (Command + Shift + B)

Build->Compile

make sure AdMob.js will sync to `./build/jsb-default` project

### Build & Run

* open `./build/jsb-default/frameworks/runtime-src/proj.ios_mac/SDKBoxTutorial.xcodeproj` with Xcode
* run `cocos run -p android ` at `./build/jsb-default` to build android

![](../imgs/ccc_tutorial_admob_intistial_show.png)

### Test AD

Admob provide some test ad IDs.

AdMob iOS Test Ad: https://developers.google.com/admob/ios/test-ads

Android iOS Test Ad: https://developers.google.com/admob/android/test-ads


### IMPORTANT

Make sure backup `sdkbox_config.json`, `./build/jsb-default/res` will be removed every time after Build Project in Cocos Creator build windows
