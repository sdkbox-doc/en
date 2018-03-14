[&#171; SDKBOX Home](http://sdkbox.com)

<h1>Use SDKBOX with Custom Activity in Unity</h1>

if you have to create your own custom activity for your unity project, to add your java code or fix SDKBox Unity plugin lanucher activity conflict issue. please follow this steps:

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
        SDKBox.onActivityResult(requestCode, resultCode, data);
        super.onActivityResult(requestCode, resultCode, data);

        //code

    }

    //code

}
```



