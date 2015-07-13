### Initialize Kochava
Initialize the plugin where appropriate in your code. We recommend to do this in the `AppDelegate::applicationDidFinishLaunching()` or `AppController:didFinishLaunchingWithOptions()`. Make sure to include the appropriate headers:
```cpp
#include "PluginKochava/PluginKochava.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginKochava::init();
}
```

### Tracking Events
Kochava provides tracking __custom__, __spatial__ or __referral__ events.

* Tracking a __custom__ event:
```cpp
sdkbox::PluginKochava::trackEvent("<EVENT>", "<VALUE>");
```

* Tracking a __spatial__ event, by providing a title and position in the world:
```cpp
sdkbox::PluginKochava::spatialEvent("<TITLE>", <X>, <Y>, <Z>);
```

* Tracking a __referral__ event (also known as a deep link):
```cpp
sdkbox::PluginKochava::sendDeepLink("<URI>", "<YOUR APP>");
```
__Note:__ On Android, the 2nd parameter (__<YOUR APP>__) is not used. You just
need to pass the __<URI>__.

### Catch Kochava events (optional)
This allows you to poll and catch `Kochava` events so that you get notified when
referral or attribution data is returned from the server or secondly get notified
when a user has crossed a beacon boundary, i.e. the user is near a Starbucks or
perhaps walks into a Starbucks. The implementation here is simple using a __lambda__ function:

```cpp
auto callback = [](const std::map<std::string, std::string>* attribution)
{
  if (attribution)
  {
      typedef std::map<std::string, std::string> map_type;
      const map_type& m = * attribution;

      for (map_type::const_iterator it = m.begin(); it != m.end(); ++it)
      {
          const map_type::value_type& kv = * it;
          printf("%s -> %s", kv.first.c_str(), kv.second.c_str());
      }
  }
};

sdkbox::PluginKochava::setAttributionCallback(callback);
```
 __Note__: Asking for attribution data could take a while. You can  poll
 `getAttributionData()` until you get something back that is not **null**.
