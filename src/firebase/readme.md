[&#8249; Firebase Doc Home](./)

<h1>Firebase Integration Guide</h1>
<<[../../shared/-VERSION-/version.md]

##SDK Version
<<[../version]

##Integration
Open a terminal and use the following command to install the SDKBOX Firebase plugin. Make sure you setup the SDKBOX installer correctly.
```bash
$ sdkbox import firebase
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON Configuration
Firebase's configuration file can download from firebase [website](https://console.firebase.google.com)

#### iOS Plist
you can download iOS configuration file `GoogleService-Info.plist` from `iOS Project` -> `Settings`, and then drag `GoogleService-Info.plist` to your iOS project

#### Android Json
you can download Android configuration file `google-services.json` from `Android Project` -> `Settings`

__Notice__:
You must translate `google-services.json` to xml to use.

 * open console
 * entry directory `google-services.json` location at
 * run

```python
python -c """import urllib; import sys; sys.argv = ['transpy', '-i', './google-services.json', '-o', './googleservices.xml']; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/tools/generate_xml_from_google_services_json.py').read(); exec(s);"""
```

 * `googleservices.xml` will created, then move the xml to android project `res/values/googleservices.xml`

more info, take a look at [this](https://support.google.com/firebase/answer/7015592)

##### google_app_id Conflict

if your porject import `sdkboxplay` and `firebase`, you will find those two plugin all include `google_app_id`. at the time, you should change `google_app_id` in `sdkboxplay` to another word, e.g. `google_app_id_2`.

your modification should be like follow:

- ./res/values/strings.xml

 <del> <`string name="google_app_id">340534096218</string>` <del>

`<string name="google_app_id_2">340534096218</string>`

- Andmanifest.xml

<del> `<meta-data android:name="com.google.android.gms.games.APP_ID" android:value="@string/google_app_id"/>` <del>

`<meta-data android:name="com.google.android.gms.games.APP_ID" android:value="@string/google_app_id_2"/>`

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

<<[../shared/debug.md]
