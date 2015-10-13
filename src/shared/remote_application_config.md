### Remote Application Configuration
SDKBOX allows developers to create a __Remote Application Configuration__ for each application they are developing.

Registering the applications’ allows for on-the-fly update of its plugin’s configuration. For example, it will allow the change of the Google Analytics tracking code, switch to a new AdColony campaign or add new in-app purchase products without rebuilding and redeploying your apps to the app stores.

To enable this cloud service in your applications is as easy as calling a single __init()__ function and passing in your __application token__ and __application secret__ that were provided when you created the app in the previous section.
```
sdkbox::init( <application token>, <application secret> );
```
  __Note__: each application will have it’s own __application token__ and each configuration for each game will have it’s own __application secret__. The __application secret__ is the actual encryption key used to decipher the remote configuration.

When the developer updates a __Remote Application Configuration__ the application will automatically pull the new configuration and put it into effect. This means that you can update configuration information on the fly and everyone playing your game will get updated the next time the user starts the application!

To ensure security, during normal execution the new configuration is locally saved in the applications’s private folder, and the next time it restarts it is applied. Also, configurations are cyphered and its contents are not exposed, even if your application runs on a rooted/jailbroken device.
