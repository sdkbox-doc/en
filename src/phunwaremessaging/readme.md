[&#8249; PhunwareMessaging Doc Home](./)

<h1>PhunwareMessaging Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##Integration
Open a terminal and use the following command to install the SDKBOX [PhunwareMessaging](http://maas.phunware.com/) plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import phunwaremessaging
```

##Configure your app for push notifications (iOS)

1. Go to developer.apple.com and create a push notification certificate.(Push notification tutorial)

2. Once it's created, download the push production certificate and add it to Keychain Access. Then,
   from Keychain Access, export both the certificate and key. (Right click to view the Export option)
   as a .p12 and set a password.

3. Now, log on to the Maas Portal, navigate to the app created for your application and update the following.

    - Certificate (.p12): Click the grey ellipses button to upload the Production Push Certificate
      you created on developer.apple.com.
    - Password: The password you setup for the push certificate.
    - Environment: Use Production environment for production apps.

##Configure your app for push notifications (Android)

**NOTE**: PhunwareMessaing don't support Eclipse/Ant project

1. Set up GCM at https://developers.google.com/cloud-messaging/android/client

2. Create a project on Firebase console

    - Choose 'Add Firebase to Android app'
    - In the Firebase console, the package name should be the same as application id in build.grade
3. The Firebase console creates a google-services.json file and downloads it to your default Downloads folder.
4. Put the google-services.json file to proj.android-studio/app/ folder

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

2. if use android studio, add this to your gradle:

``` groovy
android {
    useLibrary 'org.apache.http.legacy'
}
```
