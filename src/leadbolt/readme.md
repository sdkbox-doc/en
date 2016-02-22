[&#8249; LeadBolt Doc Home](./)

<h1>LeadBolt Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX LeadBolt plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import leadbolt
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `res/sdkbox_config.json`, that you have to modify it before you can use it for your own app

Here is an example of the LeadBolt configuration, you need to replace `<api_key>`, `<name>` item with your specific [leadbolt](http://leadbolt.com/) account information.
```json
"LeadBolt":{
    "api_key":"8uc8Kd5b6LoyJZCAsFUCY2sWmSJkXZ6c",
    "ads":{
        "ad1":{
            "name":"inapp"
        }
    }
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

<<[proguard.md]
