[&#8249; PhunwareMessaging Doc Home](./)

<h1>Phunware Integration Guide（Messaging）</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX [Phunware Messaging](http://maas.phunware.com/) plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import phunwaremessaging
```

##iOS Configuration

1. Go to [Apple developer portal](https://developer.apple.com) and create a push notification certificate. (See [Push notification tutorial](https://www.raywenderlich.com/123862/push-notifications-tutorial) for detailed instructions)

2. Once it's created, download the push production certificate and add it to Keychain Access. Then,
   from Keychain Access, export both the certificate and key. (Right click to view the Export option)
   as a .p12 and set a password.

3. Now, log on to the Maas Portal, navigate to the app created for your application and update the following.

    - Certificate (.p12): Click the grey ellipses button to upload the Production Push Certificate
      you created on developer.apple.com.
    - Password: The password you setup for the push certificate.
    - Environment: Use Sandbox for debug builds. Use Production environment for production apps and Production Ad-Hoc build.

##Android Configuration

1. Phunware messaging currently only supports Android-Studio
2. Create a new Android application in MAAS-portal
3. In strings.xml (under Sample/src/main/res/values), replace the appId, accessKey and signatureKey with values for this application in MAAS portal.
4. Set up [Google Cloud Messaging](https://developers.google.com/cloud-messaging/android/client)
5. Create a project on Firebase console

    -> Choose 'Add Firebase to Android app'

    -> In the Firebase console, the package name should be the same as application id in build.grade (under Sample directory) 
6. In the MAAS portal, for the newly created Android app, replace the API Key and sender id with the values for ServerKey and SenderId on the Firebase console (under CloudMessaging section)
7. The Firebase console creates a google-services.json file and downloads it to your default Downloads folder.
8. Replace the default google-service.json file (under Sample directory) the sample app with the dowloaded google-service.json from Firebase console
9. Add the google-services gradle plugin to you applications gradle file
  `apply plugin: 'com.google.gms.google-services'`

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
SDKBOX Installer will automatically inject a sample configuration to your `sdkbox_config.json`, that you have to modify it before you can use it for your own app.

Here is an example of the PhunwareMessaging configuration.
```json
{
    "ios": {
        "PhunwareMessaging":{
            "debug":true,
            "api_id":"1569",
            "access_key":"b49ea8dc7bdc4a056d51e8b72a8f3a575047a4aa",
            "signature_key":"b3f090e90cefe5b9535b0703d94a89a10f8a934b"
        }
    },
    "android": {
        "PhunwareMessaging":{
            "debug":true,
            "api_id":"1527",
            "access_key":"c11a65cb3deeca49aac6f8c0e794b7bc68e1481a",
            "signature_key":"1580b669f2edb1c810c29e52e9a754f443f6215a",
            "env":"dev"
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

##Notice

SDKBox PhunwareMessaging v3.5.1+ android Required:

1. Build SDK Version - 23
2. Compile SDK Version - 23

if you get `miss HttpClient` error when set build sdk to 23:

1. if use eclipse, copy `$ANDROID_SDK_ROOT/platforms/android-23/optional/org.apache.http.legacy.jar` to your project `libs` folder
2. if use android studio, add this to your gradle:

``` groovy
android {
    useLibrary 'org.apache.http.legacy'
}
```
