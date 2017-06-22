![](SDKBOX_logo.png)

<h1>In App Purchase Documentation.</h1>

For more information, visit our website @ [www.sdkbox.com](http://cocos2d-x.org/sdkbox)

##Setting up App Store accounts

The first step of implementing In app purchase will be setting up App Store Accounts.

This guide does not cover creating the account itself, or creating apps in the iTunes or GooglePlay stores. For instructions on how to do that, please visit [iTunes](http://itunesconnect.apple.com/) and [GooglePlay](https://play.google.com/apps/publish) website.

> For GooglePlay, you must specify the public key in the IAP configuration inspector panel. You can get it from the Google Play Console "Services & APIs" section

##Importing SDKBOX IAP

To begin using SDKBOX IAP, import the ```sdkbox_iap``` unity package into your project. This will add a directory under Assets called `SDKBOX`.

![](iap_dox1.png)

This directory contains everything you will need in order to make In-App-Purchases. We also provide a sample scene with everything setup, you can use it as a reference

![](sample_scene.png)


To begin, find the IAP prefab in the IAP directory.

![](iap_dox2.png)

Create an instance of the IAP prefab in the scene where you want to make in app purchases, such as your store scene.

Select the IAP game object in the hierarchy and in your inspector pane you can configure the object for In-App-Purchases.

<h2>Adding Products</h2>

Products are added on either iTunes connect for Apple, or Google Play Portal for Google. Follow directions <insert links> on how to setup products for Apple and Google platforms.

Each product will have a name, and there are two types of products. Consumable and Non-consumable. Google only supports the latter, but SDKBOX allows you to have Consumable products on Google as well as Apple, and they behave the same way.

In the ```Products``` field for each platform, you can specify how many products you have, and you can enter the name of each product, and whether or not it is consumable.

> Note: you can use same name across ios and android to keep your code cross-platform

![](iap_dox4.jpg)

##Specifying a key (Android)

![](iap_dox3.jpg)

On Android, need a license key from the ```Services & APIs``` section of the Google Play Developer Console. Copy and paste this key into the Android Key field.

##Making Purchases

Making a purchase is as simple as invoking the ```purchase``` method on the IAP game object. There are several ways to do this, we will do it by adding a button.

From the menu, choose **Game Object** -> **UI** -> **Button**. This will create a UI canvas (if you didn't have one already) and add a button.

![](iap_dox5.jpg)

Name your button in the hierarchy what you like, and change the text to "Purchase" or something similar.

Now in the inspector pane, find the ```On Click()``` event and from the object drop down, select the IAP game object. Then from the method drop down, select the ```IAP.purchase``` method.

This method takes a string argument that is the name of the product being purchased. You can enter that name under the method name in the space provided.

![](iap_dox6.jpg)

##Handling Callbacks

There are several events that provide feedback about what is happening when you initialize, make purchases, or restore previously purchased items.

The following is a list of the callbacks and the parameters they provide.

* ```onInitialized (bool status)``` Called after the IAP system initializes. It will pass a boolean value that indicates whether or not the initialization was successful or not. A value of ```true``` indicates success.

* ```onProductRequestSuccess (Product[] products)``` Called after initialization, and having requested the products from the store using the keys specified for each platform. If the request was successful, then this callback is invoked and passed the array of available products.

* ```onProductRequestFailure (string error)``` Called after initialization, and if a product request fails. The string will contain an error message.

* ```onSuccess (Product product)``` Called after a successful purchase. The product is supplied as an argument. See ```Product``` for more details.

* ```onFailure (Product product, string error)``` Called after a failed purchase attempt. The product is supplied as an argument, and a string is passed containing an error message.

* ```onCanceled (Product product)``` Called if a In-App-Purchase is canceled. The product is supplied as an argument.

* ```onRestored (Product product)``` Called for each product restored from the store. If no products have been purchased, then you will only get the following completed call.

* ```onRestoreComplete ()``` Called after all products have been restored. If none were restored, you will still receive this callback.

##Handling IAP Events

Similar to the button On Click() event, you can subscribe to SDKBOX IAP events to get feedback about the IAP process, and to receive products from the IAP store.

In the ```Callbacks``` section of the IAP script inspector pane, you can click ```+``` to add a subscriber, and specify the object, and method that you would like to have invoked.

![](iap_dox7.jpg)

##Product Class

```
	public struct Product
	{
		public enum Type {CONSUMABLE, NON_CONSUMABLE};

		// The name specified in sdkbox_config.json
		public string name;

		// The product id of an In App Purchase
		public string id;

		// Type of iap item
		public Type type;

		// The title of the IAP item
		public string title;

		// The description of the IAP item
		public string description;

		// Price value in float
		public float priceValue;

		// Localized price
		public string price;

		// price currency code
		public string currencyCode;
	}
```

The product class contains all the information about a product retrieved from the server, as well as the consumable state set in the editor.

You should not create your own products, but rather allow SDKBOX IAP to create them for you.

##Additional Android Instructions

### Override Unity Activity

In order for In-App-Purchase to work, we have to be able to forward certain activity methods to the billing code. To do this on Unity we have to replace the Unity main activity. If you do not have your own custom activity, and also have not provided your own AndroidManifest.xml, then the package will automatically copy the activity and manifest to the correct location. If there is already a manifest present, then it will notify you with a dialog to read this section and perform the following steps.

1. Copy the file *CustomActivity.jar* from **Assets/SDKBOX/Assets/Resources** to **Assets/Plugins/Android**
2. Modify your AndroidManifest.xml as following:
![](chart-8.png)

### Adding Vendor Billing Permission

In order for In-App-Purchase to work on Android, it needs the following permission to be added.

```
<uses-permission android:name="com.android.vending.BILLING" />
```

If you have not specified your own AndroidManifest.xml then when you import the package, one will be copied that already has this permission set.

If you do have your own already, then you will need to add this permission to it.

The AndroidManifest.xml is merged with the main manifest that Unity creates when building the APK.

### FAQ
1. Found plugins with same names and architectures
Sometimes Unity failed to recognize Android library correctly, when that happens you'll encounter this error message.
![](error_1_arch.png)

To fix this issue, select the *.so files based on the error message, then check the Inspector, make sure the "Platform Settings" are correct.
Anything under "x86" folder, should be set to "x86". Anything under "armeabi-v7a" folder should be set to "ARMv7"
![](error_1_solve.png)
