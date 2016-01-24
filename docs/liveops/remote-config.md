<h1>LiveOps - Remote Configuration</h1>

## How Remote Configuraton works? 
When it's necessary to change the configuratin of a SDKBOX plugin, you will need to revise the JSON codes in the `sdkbox_config.json`, rebuild the application, and re-submit it to app stores. To solve this issue, __Remote Configuration__ allows for on-the-fly update of its plugin’s configuration. For example, it will allow the change of the Google Analytics tracking code, switch to a new AdColony campaign or add new in-app purchase products without rebuilding and redeploying your apps to the app stores.

![chart](/imgs/remote_config.jpg)

!!! note
    * The application will automatically pull the new configuration and put it into effect. This means that you can update configuration information on the fly and everyone playing your game will get updated the next time the user starts the application.
    * To ensure security, during normal execution the new configuration is locally saved in the applications’s private folder. Also, configurations are cyphered and its contents are not exposed, even if your application runs on a rooted/jailbroken device.

## About Configuration Set and Versioning
* A `Configuration Set` includes multiple versions of config which are marked with different names. Each version has a state: 
    * __Live__: only one in a set, will be sent to the app be default
    * __Debug__: only one in a set, will be sent if app is in the debug mode
    * __Draft__: multiple, they are not accessable from any applications.  
* Each `Configuration Set` has a unique pair of __token__ and __secret__. They are used to securely communicate between to the app and SDKBOX LiveOps. They can not be changed. They need to be set in the app. See the "Setup Remote Config in App" below for detail. 
* An app will use the specific token to get either the `Live` or `Debug` version of config in a set, follow the sequence diagram above. 
* Each configuration set is defined for a certain platform. However each platform can have multiple sets. If the application will be published to both Apple appstore and Google Play store, you should create at least two configuration sets for both of them. For example: 
![chart](/imgs/config_versions.jpg)

## Import Existing App Configs 
* When you integrate SDKBOX, a local `sdkbox_config.json` will be added in your app. It contains all the settings of SDK plugins. 
* For moving the local configs to clout, we provice a convinient feature to import them automatically. At your application's page, click on "Import Config" button and upload your local `sdkbox_config.json`. All you current configurations will be loaded into a few new configuration sets, one for each platform. 
* After importing, you should make the remote config as the __master__ version moving forward. 


## Setup App using Remote Config 
* To enable the cloud service in your applications is as easy as calling a single __sdkbox::init()__ function and passing in your __token__ and __secret__ that are provided by the `Configuration Set`. 
```
sdkbox::init( <application token>, <application secret> );
```
* We provide a helper function to make this easy. From your application's page, click on "Export". Then select the one `Configuraton Set` for each platform you will deploy to. Next, you will get two parts of data:  
    * Code snippets for initlizing SDKBOX with the config token/scret for each platform. You can copy and paste them to your app delegate.
    * A new version of `sdkbox_config.json` includes the latest configurations saved in the cloud. __Whenever an app is submitted to the app store, please update the local version of `sdkbox_config.json` in the app, in case if remote config is not available. For example when there is no network, a local config will always be used.__ 



