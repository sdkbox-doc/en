## API Reference

### Methods
```cpp
static void init ( const std::string & userID = "" ,
                   const char * jsonconfig = 0 ) ;
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

<pre>
@placementId (deprecated)
</pre>

```cpp
static void requestOffers ( const std::string & placementId = "" ) ;
```
> Request the server for rewarded video availability.

```cpp
static void showOffers ( const std::string & placementId = "" ) ;
```
> Show an available rewarded video.

<pre>
@placementId (deprecated)
</pre>

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

<pre>
 @param age Age of the user. Pass `FYBEntryIgnore` if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setBirthdate ( const std::string & data ) ;
```
>  Sets the user's date of birth, format (yyyy-MM-dd)

<pre>
 @param date Date of birth of the user. Pass `""` if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setGender ( int gender ) ;
```
>  Sets the user's gender

<pre>
 @param gender Gender of the user. Pass FYB_UserGenderUndefined if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setSexualOrientation ( int sexualOrientation ) ;
```
>  Sets the user's sexual orientation

<pre>
 @param sexualOrientation Sexual orientation of the user. Pass FYB_UserSexualOrientationUndefined if value needs to be ignored or to be removed, if already exists.
</pre>

```cpp
static void setEthnicity ( int ethnicity ) ;
```
>  Sets the user's ethnicity

<pre>
 @param ethnicity Ethnicity of the user. Pass FYB_UserEthnicityUndefined if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setLocation ( double latitude , double longitude ) ;
```
>  Set the user's location

```cpp
static void cleanLocation ( ) ;
```
> Clean the user's location

```cpp
static void setMaritalStatus ( int status ) ;
```
>  Sets the user's marital status

<pre>
 @param status Marital status of the user. Pass FYB_UserMaritalStatusUndefined if value needs to be ignored or to be removed if already exists
</pre>

```cpp
static void setNumberOfChildren ( int numberOfChildren ) ;
```
>  Sets the user's number of children

<pre>
 @param numberOfChildren The number of children
</pre>

```cpp
static void setAnnualHouseholdIncome ( int income ) ;
```
>  Sets the user's annual household income

<pre>
 @param income Annual household income of the user. Pass `FYB_EntryIgnore` if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setEducation ( int education ) ;
```
>  Sets the user's educational background

<pre>
 @param education Education of the user. Pass FYB_UserEducationUndefined if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setZipcode ( const std::string & zipcode ) ;
```
>  Sets the user's zipcode

<pre>
 @param zipcode Zipcode of the current living place of the user. Pass `""` if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setInterests ( const std::vector <std::string> & interests ) ;
```
>  Set the user's list of interests

<pre>
 @param interests List of interests of the user. Pass `{}` if value needs to be ignored or to be removed, if already exists
</pre>

```cpp
static void setIap ( bool flag ) ;
```
>  Sets if in-app purchases are enabled.

<pre>
 @param flag Sets if in-app purchases are enabled
</pre>

```cpp
static void setIapAmount ( float amount ) ;
```
>  Sets the amount that the user has already spent on in-app purchases

<pre>
 @param amount The amount of money that the user has spent
</pre>

```cpp
static void setNumberOfSessions ( int numberOfSessions ) ;
```
>  Sets the number of sessions

<pre>
 @param numberOfSessions The number of sessions that has already been started
</pre>

```cpp
static void setPsTime ( double timestamp ) ;
```
>  Sets the time spent on the current session

<pre>
 @param timestamp The time spent on the current session
</pre>

```cpp
static void setLastSession ( double session ) ;
```
>  Sets the duration of the last session

<pre>
 @param session The duration of the last session
</pre>

```cpp
static void setConnectionType ( int connectionType ) ;
```
>  Sets the connection type used by the user

<pre>
 @param connectionType The connection type used by the user
</pre>

```cpp
static void setDevice ( const std::string & device ) ;
```
>  Sets the device used by the user

<pre>
 @param device The device used by the user
</pre>

```cpp
static void setVersion ( const std::string & version ) ;
```
>  Sets the app version

<pre>
 @param version The version of the app currently executed
</pre>

```cpp
static void cleanCustomParameters ( ) ;
```
> Clean custom parameters, iOS only

```cpp
static void addCustomParameters ( const std::string & key ,
                                  const std::string & value ) ;
```
>  Sets custom parameters to be sent along with the standard parameters

<pre>
 @param parameters The custom parameters that must be set
</pre>


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


