## Encryption
If you wish, you may encrypt the `sdkbox_config.json` to help further safeguard your config. It is very easy to encrypt and decrypt with a single command. The syntax is simple:
  ```
  $ <path_to_sdkbox>/sdkbox.py <operation> <input_file> --<key " ">
  -o <output_file>
  ```

You can specify the same input and output file to encrypt the `sdkbox_config.json` in place without creating a new output file.

Full example encrypt:
  ```
  $ ./tools/installer/sdkbox/sdkbox.py encrypt sample/adcolony/Resources/sdkbox_config.json
  --key "123" -o sample/adcolony/Resources/sdkbox_config.json
  ```

Full example decrypt:
  ```
  ./tools/installer/sdkbox/sdkbox.py decrypt sample/adcolony/Resources/sdkbox_config.json
  --key "123" -o sample/adcolony/Resources/sdkbox_config.json
  ```

## Working with the encrypted `sdkbox_config.json`
If you do encrypt your `sdkbox_config.json` it is necessary to also make a few changes to your codebase to accommodate this. Without doing this, your app will fail to work with your encrypted `sdkbox_config.json`

* Add to `AppDelegate.cpp`:
  ```cpp
  #include "Sdkbox/sdkbox.h"
  ```

* Add a new line to `AppDelegate.cpp` to specify the __key__ that was used
when encrypting the `sdkbox_config.json`. This must be done before any `init()` call to a plugin: Example:
  ```cpp
  sdkbox::Sdkbox::setXXTEAKey("123", strlen("123"));
  sdkbox::PluginAdColony::init();
  ```
