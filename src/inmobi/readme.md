[&#8249; InMobi Doc Home](./)

<h1>InMobi Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##SDK Version
<<[../version]

##Integration
Open a terminal and use the following command to install the SDKBOX InMobi plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import inmobi
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the InMobi configuration, you need to replace `<account_id>` item with your specific [__InMobi__](http://www.inmobi.com/) account information.
```json
"InMobi":{
	"interstitial_placement_id": "1449919424310", 		//interstitial id
    "account_id": "922cc696d9fa475097651b5cad78567d",
    "banner_h": 50, 									//banner height
    "banner_placement_id": "1447081423897" 				//remove if needn't
}
```

<!--<<[sdkbox-config-encrypt.md]-->

##Usage
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[../../shared/manual_integration_google_play_step.md]

<<[proguard.md]
