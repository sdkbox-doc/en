# Encrypt and decrypt sdkbox_config.json

## Precondition
- plugin's version >= 2.4.1.1
- sdkbox command >= 1.0.2.2

## Solution of SDKBox

### 1. encrypt sdkbox_config.json

```bash
# encrypt
sdkbox encrypt -i sdkbox_config.json -o sdkbox_config.json --key your_key

# decrypt
sdkbox decrypt -i sdkbox_config.json -o sdkbox_config.json --key your_key
```

### 2. set decrypt key

```c++
// AppDelegate.cpp
#include <sdkbox/Sdkbox.h>


sdkbox::init("", "your_key"); // the first argument must set "",
                              // if you don't need remote config
sdkbox::IAP::init();
sdkbox::PluginAdMob::init();
```

## Solution of yours

```c++
// AppDelegate.cpp
#include <sdkbox/Sdkbox.h>

std::string content = __decrypt__("your_encrypt_content");
sdkbox::setConfig(content); // the content of 'sdkbox_config.json'
sdkbox::IAP::init();
sdkbox::PluginAdMob::init();
```

## Use Cocos Creator's Solution


Steps:

* modify `AppDelegate.cpp` like follow:

```cpp
...
#include "SDKBoxJSHelper.h"
...

bool AppDelegate::applicationDidFinishLaunching()
{
    ...

    jsb_register_all_modules();
    se->addRegisterCallback(register_all_SDKBoxJS_helper);

    ...

    return true;
}

```

* move and rename `jsb-link/res/sdkbox_config.json` to `assets/SDKBox/sdkbox_config.js`.
* add `module.exports =` to `assets/SDKBox/sdkbox_config.js` at first line

```js
module.exports =
{
    "android": {
        "iap": {
            ...
        }
        ...
    },
    "ios": {
        "iap": {
            ...
        }
        ...
    }
}

```

* require sdkbox_config.js, and send json string to sdkbox

```js
const sdkbox_config = require('../SDKBox/sdkbox_config')
...
sdkbox.setConfig(JSON.stringify(sdkbox_config)); // make sure call this before sdkbox pluign init
...
sdkbox.PluginXXX.init();
...
```

