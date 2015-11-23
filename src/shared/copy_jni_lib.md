#### Copy jni libs
Copy and overwrite all the folders from `plugin/android/jni`
to your `<project_root>/jni/` directory.

> Note: sdkbox link with `gnustl` by default, if your project link with `c++static` please replace the files in `<project_root>/jni/<plugin_name>/libs` with files in `<project_root>/jni/<plugin_name>/libs_c++_static` folder