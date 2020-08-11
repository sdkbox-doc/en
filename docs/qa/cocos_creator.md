#SDKBOX for Cocos Creator

## Installation

1. Download [SDKBoxHelper Windows](https://github.com/hugohuang1111/sdkboxhelper/releases/download/v0.0.5/sdkboxhelper.exe) or [SDKBoxHelper Mac](https://github.com/hugohuang1111/sdkboxhelper/releases/download/v0.0.5/sdkboxhelper)

2. install `SDKBox Installer` by run command `sdkboxhelper`

3. install `SDKBox GUI For Creator` by run command `sdkboxhelper -t creator -p path/to/creator_project`

__Note__:

* open a new terminal and run command `sdkbox -h` to check if `SDKBox Installer` have installed. maybe need restart when you got `command not find` error.

* Cocos Creator 2.4.1- need't install `SDKBox GUI For Creator` manually. `SDKBox GUI For Creator` is built in.

### Install `SDKBox GUI For Creator` Manually

`sdkboxhelper -t creator -p path/to/creator_project` will install `SDKBox GUI For Creator` locally.

if you want to install `SDKBox GUI For Creator` global.

* Download `SDKBox GUI For Creator` [package](http://sdkbox.anysdk.com/gui/creator/sdkbox-1.4.1.zip)
* Install:
    - Global Install: unzip `SDKBox GUI For Creator` package to path `~/.CocosCreator/packages` (`C:\Users\${UserName}\.CocosCreator\packages` on windows)
    - locally Install: unzip `SDKBox GUI For Creator` package to path `${CocosCreator Project}/packages`

* Then, `SDKBox` item show in `Expand` Menu.

* packages file tree should be like follow:
```
packages
|--sdkbox
    |--app
    |--main.js
    |--package.json
```


Starting Cocos Creator 1.4 developer can install SDKBOX plugin from Extension Store

<iframe src='https://gfycat.com/ifr/ConsciousSomberGerenuk' frameborder='0' scrolling='no' width='640' height='360' allowfullscreen></iframe>

Once installed successfully, a new menu entry named "SDKBox" will be added to Cocos Creator

![](../imgs/ccc_tutorial_sdkbox_menu.png)

##Integration
Before integrating SDKBOX plugins make sure you generate the iOS/Android build for your Cocos Creator projects first

<iframe src='https://gfycat.com/ifr/EntireLinearBeetle' frameborder='0' scrolling='no' width='640' height='360' allowfullscreen></iframe>


##After Intergration

Once you finish integrate the SDK, you should be able to use it with javascript code. Here we'll use Admob SDK as an example

### Add buttons

add two button to scene, design ui like follow:
![](../imgs/ccc_tutorial_ui_design.png)

### Create JavaScript Component

create javascript commponent, name it `AdMob.js`, add three empty function to `AdMob.js`, also add admob initialize code in `onLoad` function like follow:

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

### Configuration AdMob

* configure `./build/jsb-default/res/sdkbox_config.json` with your ad id


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


