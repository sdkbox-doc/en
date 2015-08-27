### Modify `project.properties`
An __Android Library Reference__ for __Google Play Services__ is required. The
path will be different depending upon your setup. Also, this is an additional
download that does not come as part of a standard install. To install use the
__sdk installer__ and choose __extras->google play services__. Here is an example of what this line could look like:
```
android.library.reference.1=
../android/sdk.latest/extras/google/google_play_services/libproject/
google-play-services_lib
```
__Note:__ if you already have an `android.library.reference.1` you can add
another by incrementing the number as `android.library.reference.2`, etc.
