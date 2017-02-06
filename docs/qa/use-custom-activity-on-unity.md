[&#171; SDKBOX Home](http://sdkbox.com)

<h1>How To Use SDKBOX with Custom Activity in Unity</h1>

if you have to create your own custom activity for your unity project,  please follow this steps:

1. delete `CustomActivity.jar` (maybe location at `Assets/SDKBOX/sdkbox/Resources/CustomActivity.jar` or `Assets/Plugin/Android/libs/CustomActivity.jar`)
2. make sure `sdkbox.jar` is at this location `Assets/SDKBOX/sdkbox/Assets/Plugins/Android/sdkbox.jar`
3. modify your custom activity, maybe like follow:

```java
import com.sdkbox.plugin.SDKBox;

public class UserMainActivity extends UnityPlayerActivity
{

    //code

    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        if (!SDKBox.onActivityResult(requestCode, resultCode, data))
            super.onActivityResult(requestCode, resultCode, data);
    }

    //code

}
```



