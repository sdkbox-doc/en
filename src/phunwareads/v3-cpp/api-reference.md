## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( PhunwareAdsListener * listener ) ;
```
> Set listener to listen for phunware events

```cpp
static PhunwareAdsListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void cache ( const std::string & name ) ;
```
> cache ad by specifying ad name, auto cache default.

```cpp
static bool isAvailable ( const std::string & name ) ;
```
> is the specified ad available?

```cpp
static void show ( const std::string & name ) ;
```
> show ad by specifying ad name.

```cpp
static void hide ( const std::string & name ) ;
```
> hide ad by specifying ad name.

```cpp
static void setUserID ( const std::string & userID ) ;
```
> set user ID for rewarded video.

```cpp
static int getRemainingViews ( const std::string & name ) ;
```
> get remaining views of rewarded video.

```cpp
static void setCustomData ( const std::string & name ,
                            const std::map <std::string ,
                            std::string> & data ) ;
```
> set custom data of rewarded video


### Listeners
```cpp
void adLoaded ( const std::string & name ) 
```
> there is cached content

```cpp
void adFailed ( const std::string & name ,
                int errorCode ,
                const std::string & msg ) 
```
> there is error when cache content

```cpp
void adWillPresent ( const std::string & name ) 
```
> ad will present

```cpp
void adDidPresent ( const std::string & name ) 
```
> ad did present

```cpp
void adWillDissmiss ( const std::string & name ) 
```
> ad will dissmiss

```cpp
void adDidDismiss ( const std::string & name ) 
```
> ad did dismiss

```cpp
void willLeaveApp ( const std::string & name ) 
```
> will leave application

```cpp
void reward ( const std::string & name ,
              float amount ,
              const std::string & currency ,
              const std::map <std::string ,
              std::string> & customData ) 
```
> reward user with specifying ad name


