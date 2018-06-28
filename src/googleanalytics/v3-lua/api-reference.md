## API Reference

### Methods
```lua
sdkbox.PluginGoogleAnalytics:init(jsonconfig)
```
> initialize the plugin instance.

```lua
sdkbox.PluginGoogleAnalytics:startSession()
```
> The analytics session is being explicitly started at plugin initialization time.

```lua
sdkbox.PluginGoogleAnalytics:stopSession()
```
> You normally will never stop a session manually.

```lua
sdkbox.PluginGoogleAnalytics:dispatchHits()
```
> Manually request dispatch of hits. By default, data is dispatched from the
Google Analytics SDK for Android every 5 minutes.

```lua
sdkbox.PluginGoogleAnalytics:dispatchPeriodically(seconds)
```
> Change the dispatch info time period to the desired amount of seconds.

```lua
sdkbox.PluginGoogleAnalytics:stopPeriodicalDispatch()
```
> Stop periodically sending info. Then manually the <code>dispatchPeridically</code>
or <code>dispatchHits</code> should be called.

```lua
sdkbox.PluginGoogleAnalytics:setUser(userID)
```
> Set user ID for this tracking session

```lua
sdkbox.PluginGoogleAnalytics:setDimension(index, value)
```
> Set value to custom dimension

```lua
sdkbox.PluginGoogleAnalytics:setMetric(index, value)
```
> Set value to custom metric

```lua
sdkbox.PluginGoogleAnalytics:logScreen(title)
```
> Log screen info. title is the title of a screen. Screens are logical units
inside your app you'd like to identify at analytics panel.

```lua
sdkbox.PluginGoogleAnalytics:logEvent(eventCategory,
                                       eventAction,
                                       eventLabel,
                                       value)
```
> GoogleAnalytics::logEvent("Achievement", "Unlocked", "Slay 10 dragons", 5);

```lua
sdkbox.PluginGoogleAnalytics:logException(exceptionDescription, isFatal)
```
> Log an exception. It is a basic support for in-app events.

```lua
sdkbox.PluginGoogleAnalytics:logTiming(timingCategory,
                                        timingInterval,
                                        timingName,
                                        timingLabel)
```
> Measure a time inside the application.

```lua
sdkbox.PluginGoogleAnalytics:logSocial(socialNetwork,
                                        socialAction,
                                        socialTarget)
```
> Log a social event.

```lua
sdkbox.PluginGoogleAnalytics:logECommerce(info)
```
> Log ecommerce event

<pre>
            // 1. track purchase
            std::map<std::string, std::string> info;
            // transaction info
            info["action"] = "purchase";
            info["transaction"] = "T12345";
            info["affiliation"] = "Google Store - Online";
            info["transactionCouponCode"] = "SUMMER2017";
            info["revenue"] = "37.39";
            info["tax"] = "2.85";
            info["shipping"] = "5.34";
            // product info
            info["productID"] = "P12345";
            info["productName"] = "Android Warhol T-Shirt";
            info["category"] = "Apparel/T-Shirts";
            info["brand"] = "SDKBox";
            info["productVariant"] = "black";
            info["productCouponCode"] = "APPARELSALE";
            info["price"] = "29.20";
            info["quantity"] = "1"; // int
            // currency code
            // https://support.google.com/analytics/answer/6205902?#supported-currencies
            info["currencyCode"] = "EUR";
            sdkbox::PluginGoogleAnalytics::logECommerce(info);

            // 2. track refund
            // transaction info
            info["action"] = "refund";
            info["transaction"] = "T12345";
            // product info
            info["productID"] = "P12345";
            info["quantity"] = "1";
            sdkbox::PluginGoogleAnalytics::logECommerce(info);
</pre>

```lua
sdkbox.PluginGoogleAnalytics:setDryRun(enable)
```
> While running on dry run, the tracked events won't be sent to the actual
analytics account.

```lua
sdkbox.PluginGoogleAnalytics:enableAdvertisingTracking(enable)
```
> Enable advertising tracking when in google's ad vendors.

```lua
sdkbox.PluginGoogleAnalytics:createTracker(trackerId)
```
> Create a tracker identified by the google analytics tracker id XX-YYYYYYYY-Z.
If the tracker already existed, no new tracker will be created. In any case, the
tracker associated with tracker id will be set as default tracker for  analytics
operations.

```lua
sdkbox.PluginGoogleAnalytics:enableTracker(trackerId)
```
> Enable a tracker identified by a trackerId. If the tracker does not exist,
nothing will happen.

```lua
sdkbox.PluginGoogleAnalytics:enableExceptionReporting(enable)
```
> Enables or disables uncaught exception reporting for a given tracker.


### Listeners

