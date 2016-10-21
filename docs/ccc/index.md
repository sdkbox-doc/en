[&#171; SDKBOX Home](http://sdkbox.com)

<h1>SDKBOX for Cocos Creator</h1>

## How to integrate SDKBox Plugin to Cocos Creator project
---

### Environment

* `CocosCreator` Ver.1.2.2 [Install](http://www.cocos.com/creator)
* `SDKBox Installer` 1.0.0.18 [Install](http://docs.sdkbox.com/en/installer/)

### Create new Cocos Creator Project

Create Project `SDKBoxTutorial` like follow:
![](../imgs/ccc_tutorial_create_project.png)

### Add buttons

add two button to scene, design ui like follow:
![](../imgs/ccc_tutorial_ui_design.png)

### Create JavaScript Component

create javascript commponent, name it `AdMob.js`, i will integrate `AdMob` the this project. add three empty function to `AdMob.js`. like follow:

```js
cc.Class({

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
![](../imgs/ccc_tutorial_build_win.png)

Build->Compile
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
        let self = this
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

        // just for test
        let plugin = sdkbox.PluginAdMob
        if ("undefined" != typeof(plugin.deviceid) && plugin.deviceid.length > 0) {
            this.showInfo('deviceid=' + plugin.deviceid);
            // plugin.setTestDevices(plugin.deviceid);
        }
    },

    cacheInterstitial: function() {
        sdkbox.PluginAdMob.cache('gameover');
    },

    showInterstitial: function() {
        sdkbox.PluginAdMob.show('gameover');
    },

    ...

});
```

### Build Cocos Creator Again

Menu->Project->Build or (Command + Shift + B)
Build->Compile
make sure AdMob.js will sync to `./build/jsb-default` project

### Build with Xcode

* open `./build/jsb-default/frameworks/runtime-src/proj.ios_mac/SDKBoxTutorial.xcodeproj` with Xcode
* Build && Run

![](../imgs/ccc_tutorial_admob_intistial_show.png)

### IMPORTANT

Make sure backup `sdkbox_config.json`, `./build/jsb-default/res` will be removed every time after Build Project in Cocos Creator build windows
