## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( InMobiListener * listener ) ;
```
> Set listener to listen for inmobi events

```cpp
static InMobiListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static std::string getVersion ( ) ;
```
> Use this to get the version of the SDK.
@return The version of the SDK.

```cpp
static void setLogLevel ( SBIMSDKLogLevel desiredLogLevel ) ;
```
> Set the log level for SDK's logs
@param desiredLogLevel The desired level of logs.

```cpp
static void addIdForType ( const std::string & identifier ,
                           SBIMSDKIdType type ) ;
```
> Register a user specific id with the SDK
@param identifier The user Id.
@param type The user Id type.

```cpp
static void removeIdType ( SBIMSDKIdType type ) ;
```
> Deregister a particular set of Ids
@param type The user Id type.

```cpp
static void setAge ( int age ) ;
```
> Provide the user's age to the SDK for targetting purposes.
@param age The user's age.

```cpp
static void setAreaCode ( const std::string & areaCode ) ;
```
> Provide the user's area code to the SDK for targetting purposes.
@param areaCode The user's area code.

```cpp
static void setAgeGroup ( SBIMSDKAgeGroup ageGroup ) ;
```
> Provide the user's age group to the SDK for targetting purposes.
@param ageGroup The user's age group.

```cpp
static void setYearOfBirth ( int yearOfBirth ) ;
```
> Provide a user's date of birth to the SDK for targetting purposes.
@param dateOfBirth The user's date of birth.

```cpp
static void setEducation ( SBIMSDKEducation education ) ;
```
> Provide the user's education status to the SDK for targetting purposes.
@param education The user's education status.

```cpp
static void setEthnicity ( SBIMSDKEthnicity ethnicity ) ;
```
> Provide the user's ethnicity to the SDK for targetting purposes.
@param ethnicity The user's ethnicity.

```cpp
static void setGender ( SBIMSDKGender gender ) ;
```
> Provide the user's gender to the SDK for targetting purposes.
@param gender The user's gender.

```cpp
static void setHouseholdIncome ( SBIMSDKHouseholdIncome income ) ;
```
> Provide the user's household income to the SDK for targetting purposes.
@param income The user's household income.

```cpp
static void setIncome ( unsigned int income ) ;
```
> Provide the user's income to the SDK for targetting purposes.
@param income The user's income.

```cpp
static void setInterests ( const std::string & interests ) ;
```
> Provide the user's interests to the SDK for targetting purposes.
@param interests The user's interests.

```cpp
static void setLanguage ( const std::string & language ) ;
```
> Provide the user's preferred language to the SDK for targetting purposes.
@param language The user's language.

```cpp
static void setLocation ( const std::string & city ,
                          const std::string & state ,
                          const std::string & country ) ;
```
> Provide the user's location to the SDK for targetting purposes.
@param city The user's city.
@param state The user's state.
@param country The user's country.

```cpp
static void setLocation ( double latitude , double longitude ) ;
```
> Provide the user's location to the SDK for targetting purposes.
@param location: The location of the user

```cpp
static void setNationality ( const std::string & nationality ) ;
```
> Provide the user's nationality to the SDK for targetting purposes.
@param nationality The user's nationality.

```cpp
static void setPostalCode ( const std::string & postalcode ) ;
```
> Provide the user's postal code to the SDK for targetting purposes.
@param postalcode The user's postalcode.

```cpp
static void shouldAutoRefresh ( bool refresh ) ;
```
> Control if the banner should auto-refresh ad content.

```cpp
static void setRefreshInterval ( int interval ) ;
```
> Specify the refresh interval for the banner ad.

```cpp
static void loadBanner ( ) ;
```
> Submit a request to load banner ad content.

```cpp
static void disableHardwareAccelerationForBanner ( ) ;
```
> Turn off hardware acceleration on the underlying views.
vaild on android

```cpp
static void setBannerAnimationType ( SBIMBannerAnimationType animationType ) ;
```
> Set the animation preference on the banner views during ad refresh.

```cpp
static void setBannerExtras ( const std::map <std::string ,
                              std::string> & extras ) ;
```
> Set any additional custom parameters that will be sent in the ad request.

```cpp
static void setBannerKeywords ( const std::string & keywords ) ;
```
> Set comma delimited keywords for targeting purpose

```cpp
static void loadInterstitial ( ) ;
```
> Submit a request to load interstitial ad content.

```cpp
static bool isInterstitialReady ( ) ;
```
> Returns true if the interstitial was loaded successfully and in ready to be shown.

```cpp
static void showInterstitial ( ) ;
```
> Displays the interstitial on the screen

```cpp
static void showInterstitial ( SBIMInterstitialAnimationType type ) ;
```
> Displays the interstitial on the screen
valid on ios

```cpp
static void showInterstitial ( int enterAnimationResourcedId ,
                               int exitAnimationResourceId ) ;
```
> Displays the interstitial on the screen
valid on android

```cpp
static void disableHardwareAccelerationForInterstitial ( ) ;
```
> Disable hardware acceleration on the underlying views.
valid on android

```cpp
static void setInterstitialExtras ( const std::map <std::string ,
                                    std::string> & extras ) ;
```
> Set any additional custom parameters that will be sent in the ad request.

```cpp
static void setInterstitialKeywords ( const std::string & keywords ) ;
```
> Set comma delimited keywords for targeting purpose


### Listeners
```cpp
void bannerDidFinishLoading ( ) {
```
> Notifies the delegate that the banner has finished loading

```cpp
void bannerDidFailToLoadWithError ( PluginInMobi::SBIMStatusCode code ,
                                    const std::string & description ) {
```
> Notifies the delegate that the banner has failed to load with some error.

```cpp
void bannerDidInteractWithParams ( const std::map <std::string ,
                                   std::string> & params ) {
```
> Notifies the delegate that the banner was interacted with.

```cpp
void userWillLeaveApplicationFromBanner ( ) {
```
> Notifies the delegate that the user would be taken out of the application context.

```cpp
void bannerWillPresentScreen ( ) {
```
> Notifies the delegate that the banner would be presenting a full screen content.

```cpp
void bannerDidPresentScreen ( ) {
```
> Notifies the delegate that the banner has finished presenting screen.

```cpp
void bannerWillDismissScreen ( ) {
```
> Notifies the delegate that the banner will start dismissing the presented screen.

```cpp
void bannerDidDismissScreen ( ) {
```
> Notifies the delegate that the banner has dismissed the presented screen.

```cpp
void bannerRewardActionCompletedWithRewards ( const std::map <std::string ,
                                              std::string> & rewards );
```
> Notifies the delegate that the user has completed the action to be incentivised with.

```cpp
void interstitialDidFinishLoading ( ) {
```
> Notifies the delegate that the interstitial has finished loading

```cpp
void interstitialDidFailToLoadWithError ( PluginInMobi::SBIMStatusCode code ,
                                          const std::string & description ) {
```
> Notifies the delegate that the interstitial has failed to load with some error.

```cpp
void interstitialWillPresent ( ) {
```
> Notifies the delegate that the interstitial would be presented.

```cpp
void interstitialDidPresent ( ) {
```
> Notifies the delegate that the interstitial has been presented.

```cpp
void interstitialDidFailToPresentWithError ( PluginInMobi::SBIMStatusCode code ,
                                             const std::string & description ) {
```
> Notifies the delegate that the interstitial has failed to present with some error.

```cpp
void interstitialWillDismiss ( ) {
```
> Notifies the delegate that the interstitial will be dismissed.

```cpp
void interstitialDidDismiss ( ) {
```
> Notifies the delegate that the interstitial has been dismissed.

```cpp
void interstitialDidInteractWithParams ( const std::map <std::string ,
                                         std::string> & params ) {
```
> Notifies the delegate that the interstitial has been interacted with.

```cpp
void interstitialRewardActionCompletedWithRewards ( const std::map <std::string ,
                                                    std::string> & rewards );
```
> Notifies the delegate that the user has performed the action to be incentivised with.

```cpp
void userWillLeaveApplicationFromInterstitial ( ) {
```
> Notifies the delegate that the user will leave application context.


