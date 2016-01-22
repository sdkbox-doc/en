<h1>LiveOps - Remote Configuration</h1>

## How Remote Configuraton works? 
When it's necessary to change the configuratin of a SDKBOX plugin, you will need to revise the JSON codes in the `sdkbox_config.json`, rebuild the application, and re-submit it to app stores. To solve this issue, __Remote Configuration__ allows for on-the-fly update of its plugin’s configuration. For example, it will allow the change of the Google Analytics tracking code, switch to a new AdColony campaign or add new in-app purchase products without rebuilding and redeploying your apps to the app stores.

![chart](/imgs/remote_config.jpg)
__Note__: the application will automatically pull the new configuration and put it into effect. This means that you can update configuration information on the fly and everyone playing your game will get updated the next time the user starts the application.


## Setup remote configuration
1. Register and login to [sdkbox.com](http://sdkbox.com)
2. Create a new application for your app. Retrieve application's __token__ and __secret__. 
3. To enable this cloud service in your applications is as easy as calling a single __init()__ function and passing in your __application token__ and __application secret__ that were provided when you created the app in the previous section. TBD
```
sdkbox::init( <application token>, <application secret> );
```

!!! note
To ensure security, during normal execution the new configuration is locally saved in the applications’s private folder. Also, configurations are cyphered and its contents are not exposed, even if your application runs on a rooted/jailbroken device.


