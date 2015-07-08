### Modify `<YourGameName>.java`
* Modify `proj.android/src/<package identifier>/<YourGameName>.java` to add the following imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* Second, modify the class to edit the `onCreate(final Bundle savedInstanceState)` function to add a call to `SDKBox.init(this);`. Example of what this might look like for you:
```java
protected void onCreate(Bundle savedInstanceState){
  super.onCreate(savedInstanceState);
  SDKBox.init(this);
}
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
