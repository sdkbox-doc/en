<h1>FAQ</h1>

## Android App Over 64K Methods
If you see this build error for your android app
```
Unable to execute dex: method ID not in [0, 0xffff]: 65536
```
That means your app has hit the android API limit


If you're using gradle/Android Studio, you can enable patch according to [google's guide](https://developer.android.com/studio/build/multidex.html)


However if you're using cocos cosnole, Ant or eclipse you have to find a way to reduce the number of APIs in your app.