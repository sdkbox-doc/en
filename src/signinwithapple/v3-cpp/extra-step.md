### Modify __AppActivity.java__

#### Plugin >= 2.4.0.3

1. Find the __AppActivity.java__
```bash
find . -name "AppActivity.java"
```

2. Replace `extends Cocos2dxActivity` with `extends com.sdkbox.plugin.SDKBoxActivity`


Example of the directory where the __AppActivity.java__ file is located:

```
cpp
  - proj.android/src/org/cocos2dx/cpp/AppActivity.java
  - proj.android-studio/app/src/org/cocos2dx/cpp/AppActivity.java
  - proj.android/app/src/org/cocos2dx/cpp/AppActivity.java ( from cocos2d-x 3.17)

lua
  - frameworks/runtime-src/proj.android/src/org/cocos2dx/lua/AppActivity.java
  - frameworks/runtime-src/proj.android-studio/app/src/org/cocos2dx/lua/AppActivity.java
  - frameworks/runtime-src/proj.android/app/src/org/cocos2dx/lua/AppActivity.java (from cocos2d-x 3.17)

js
  - frameworks/runtime-src/proj.android/src/org/cocos2dx/javascript/AppActivity.java
  - frameworks/runtime-src/proj.android/app/src/org/cocos2dx/javascript/AppActivity.java ( from cocos2d-x 3.17)
```


#### Plugin < 2.4.0.3

* If you're using cocos2d-x from source, assuming you are in the __proj.android__ directory, __Cocos2dxActivity.java__ is located:

    ```
    ../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/
    lib/Cocos2dxActivity.java
    ```

* If you're using the prebuilt cocos2d-x libraries assuming you are in the `proj.android` directory, __Cocos2dxActivity.java__ is located:

    ```
    ./src/org/cocos2dx/lib/Cocos2dxActivity.java
    ```

  __Note:__ When using Cocos2d-x from source, different versions have __Cocos2dxActivity.java__ in a different location. One way to find the location is to look in __proj.android/project.properties__. Example:
  ```
  android.library.reference.1=../../cocos2d-x/cocos/platform/android/java
  ```

In this case, __Cocos2dxActivity.java__ should be located at:

```
../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/lib/Cocos2dxActivity.java
```

* Modify __Cocos2dxActivity.java__ to add the following imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* Second, modify __Cocos2dxActivity.java__ to edit the `onCreate(final Bundle savedInstanceState)` function to add a call to `SDKBox.init(this);`. The placement of this call is important. It must be done after the call to `onLoadNativeLibraries();`. Example:
```java
onLoadNativeLibraries();
SDKBox.init(this);
```

* Last, we need to insert the proper __overrides__ code. There are a few rules here.
    * If the method listed has not been defined, __add it__.

    * If the method listed has been defined, add the calls to `SDKBox` in the __same__ existing function.
```java
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
          if(!SDKBox.onActivityResult(requestCode, resultCode, data)) {
            super.onActivityResult(requestCode, resultCode, data);
          }
    }
    @Override
    protected void onStart() {
          super.onStart();
          SDKBox.onStart();
    }
    @Override
    protected void onStop() {
          super.onStop();
          SDKBox.onStop();
    }
    @Override
    protected void onResume() {
          super.onResume();
          SDKBox.onResume();
    }
    @Override
    protected void onPause() {
          super.onPause();
          SDKBox.onPause();
    }
    @Override
    public void onBackPressed() {
          if(!SDKBox.onBackPressed()) {
            super.onBackPressed();
          }
    }
```
