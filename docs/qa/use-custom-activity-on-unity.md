[&#171; SDKBOX Home](http://sdkbox.com)

<h1>How To Use User Customize Activity</h1>

## How to use user customize activity
---

if you already have your customize main activity, please follow this steps:

1. delete `CustomActivity.jar` (maybe location at `Assets/SDKBOX/sdkbox/Resources/CustomActivity.jar` or `Assets/Plugin/Android/libs/CustomActivity.jar`)

2. modify your self customize activity, maybe like follow:

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

sdkbox lib file location at `Assets/SDKBOX/sdkbox/Assets/Plugins/Android/sdkbox.jar`

