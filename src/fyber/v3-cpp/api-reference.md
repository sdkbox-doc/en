## API Reference

### Methods
```cpp
static void init ( const std::string & userID = "" ) ;
```
> initialize the fyber plugin.

```cpp
static void setListener ( FyberListener * listener ) ;
```
> Set listener to listen for fyber events

```cpp
static FyberListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore.

```cpp
static void showOfferWall ( const std::string & placementId = "" ) ;
```
> Presents the Fyber Mobile OfferWall as a child view controller of your own view controller.

```cpp
static void requestOffers ( const std::string & placementId = "" ) ;
```
> Request the server for rewarded video availability.

```cpp
static void showOffers ( const std::string & placementId = "" ) ;
```
> Show an available rewarded video.

```cpp
static void requestInterstitial ( ) ;
```
> Check if interstitial ads are available

```cpp
static void showInterstitial ( ) ;
```
> Shows an interstitial ad. Check first that one is ready to be shown with requestInterstitial.

```cpp
static void requestDeltaOfCoins ( const std::string & currencyId = "" ) ;
```
> Fetches the amount of a given currency earned since the last time this method was
invoked for the current user ID / app ID combination.

```cpp
static void setAge ( int age ) ;
```
>  Sets the user's age

```cpp
// "2000-02-03"
static void setBirthdate ( const std::string & data ) ;
```
>  Sets the user's date of birth, format (yyyy-MM-dd)

```cpp
// sdkbox::FYB_UserGenderUndefined
// sdkbox::FYB_UserGenderMale
// sdkbox::FYB_UserGenderFemale
// sdkbox::FYB_UserGenderOther
static void setGender ( int gender ) ;
```
>  Sets the user's gender

```cpp
// sdkbox::FYB_UserSexualOrientationUndefined
// sdkbox::FYB_UserSexualOrientationStraight
// sdkbox::FYB_UserSexualOrientationBisexual
// sdkbox::FYB_UserSexualOrientationGay
// sdkbox::FYB_UserSexualOrientationUnknown
static void setSexualOrientation ( int sexualOrientation ) ;
```
>  Sets the user's sexual orientation

```cpp
// sdkbox::FYB_UserEthnicityUndefined
// sdkbox::FYB_UserEthnicityAsian
// sdkbox::FYB_UserEthnicityBlack
// sdkbox::FYB_UserEthnicityHispanic
// sdkbox::FYB_UserEthnicityIndian
// sdkbox::FYB_UserEthnicityMiddleEastern
// sdkbox::FYB_UserEthnicityNativeAmerican
// sdkbox::FYB_UserEthnicityPacificIslander
// sdkbox::FYB_UserEthnicityWhite
// sdkbox::FYB_UserEthnicityOther
static void setEthnicity ( int ethnicity ) ;
```
>  Sets the user's ethnicity

```cpp
static void setLocation ( double latitude , double longitude ) ;
```
>  Set the user's location

```cpp
static void cleanLocation ( ) ;
```
> Clean the user's location

```cpp
// sdkbox::FYB_UserMaritalStatusUndefined
// sdkbox::FYB_UserMartialStatusSingle
// sdkbox::FYB_UserMartialStatusRelationship
// sdkbox::FYB_UserMartialStatusMarried
// sdkbox::FYB_UserMartialStatusDivorced
// sdkbox::FYB_UserMartialStatusEngaged
static void setMaritalStatus ( int status ) ;
```
>  Sets the user's marital status

```cpp
static void setNumberOfChildren ( int numberOfChildren ) ;
```
>  Sets the user's number of children

```cpp
static void setAnnualHouseholdIncome ( int income ) ;
```
>  Sets the user's annual household income

```cpp
// sdkbox::FYB_UserEducationUndefined
// sdkbox::FYB_UserEducationOther
// sdkbox::FYB_UserEducationNone
// sdkbox::FYB_UserEducationHighSchool
// sdkbox::FYB_UserEducationInCollege
// sdkbox::FYB_UserEducationSomeCollege
// sdkbox::FYB_UserEducationAssociates
// sdkbox::FYB_UserEducationBachelors
// sdkbox::FYB_UserEducationMasters
// sdkbox::FYB_UserEducationDoctorate
static void setEducation ( int education ) ;
```
>  Sets the user's educational background

```cpp
static void setZipcode ( const std::string & zipcode ) ;
```
>  Sets the user's zipcode

```cpp
static void setInterests ( const std::vector <std::string> & interests ) ;
```
>  Set the user's list of interests

```cpp
static void setIap ( bool flag ) ;
```
>  Sets if in-app purchases are enabled.

```cpp
static void setIapAmount ( float amount ) ;
```
>  Sets the amount that the user has already spent on in-app purchases

```cpp
static void setNumberOfSessions ( int numberOfSessions ) ;
```
>  Sets the number of sessions

```cpp
static void setPsTime ( double timestamp ) ;
```
>  Sets the time spent on the current session

```cpp
static void setLastSession ( double session ) ;
```
>  Sets the duration of the last session

```cpp
// sdkbox::FYB_UserConnectionTypeUndefined
// sdkbox::FYB_UserConnectionTypeWiFi
// sdkbox::FYB_UserConnectionType3G
// sdkbox::FYB_UserConnectionTypeLTE
// sdkbox::FYB_UserConnectionTypeEdge
static void setConnectionType ( int connectionType ) ;
```
>  Sets the connection type used by the user

```cpp
// predefine values
// sdkbox::FYB_UserDeviceUndefined
// sdkbox::FYB_UserDeviceIPhone
// sdkbox::FYB_UserDeviceIPad
// sdkbox::FYB_UserDeviceIPod
// sdkbox::FYB_UserDeviceAndroid
static void setDevice ( const std::string & device ) ;
```
>  Sets the device used by the user

```cpp
static void setVersion ( const std::string & version ) ;
```
>  Sets the app version

```cpp
static void cleanCustomParameters ( ) ;
```
> Clean custom parameters, iOS only

```cpp
static void addCustomParameters ( const std::string & key ,
                                  const std::string & value ) ;
```
>  Sets custom parameters to be sent along with the standard parameters


### Listeners
```cpp
void onVirtualCurrencyConnectorFailed ( int error ,
                                        const std::string & errorCode ,
                                        const std::string & errorMsg );
```

```cpp
void onVirtualCurrencyConnectorSuccess ( double deltaOfCoins ,
                                         const std::string & currencyId ,
                                         const std::string & currencyName ,
                                         const std::string & transactionId );
```

```cpp
void onCanShowInterstitial ( bool canShowInterstitial );
```

```cpp
void onInterstitialDidShow ( );
```

```cpp
void onInterstitialDismiss ( const std::string & reason );
```

```cpp
void onInterstitialFailed ( );
```

```cpp
void onBrandEngageClientReceiveOffers ( bool areOffersAvailable );
```

```cpp
void onBrandEngageClientChangeStatus ( int status , const std::string & msg );
```

```cpp
void onOfferWallFinish ( int status );
```


