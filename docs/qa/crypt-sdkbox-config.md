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


