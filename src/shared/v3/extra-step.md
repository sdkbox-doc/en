### Modify `Cocos2dxActivity.java`
* If you're using cocos2d-x from source, assuming you are in the `proj.android` directory, `Cocos2dxActivity.java` is located:

    ```
    ../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/
    lib/Cocos2dxActivity.java
    ```

* If you're using the prebuilt cocos2d-x libraries assuming you are in the `proj.android` directory, `Cocos2dxActivity.java` is located:

    ```
    ./src/org/cocos2dx/lib/Cocos2dxActivity.java
    ```

  __Note:__ When using Cocos2d-x from source, different versions have `Cocos2dxActivity.java` in a different location. One way to find the location is to look in `proj.android/project.properties`. Example:
```
android.library.reference.1=../../cocos2d-x/cocos/platform/android/java
```

In this case, `Cocos2dxActivity.java` should be located at:

```
../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/lib/Cocos2dxActivity.java
```

* Modify `Cocos2dxActivity.java` to add the following imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* Second, modify `Cocos2dxActivity` to edit the `onCreate(final Bundle savedInstanceState)` function to add a call to `SDKBox.init(this);`. The placement of this call is important. It must be done after the call to `onLoadNativeLibraries();`. Example:
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
