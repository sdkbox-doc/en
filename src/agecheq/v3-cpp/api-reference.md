## API Reference

### Methods
```cpp
static bool init ( ) ;
```
>  initialize the plugin instance.

```cpp
static void setListener ( AgeCheqListener * listener ) ;
```
> Set listener to listen for adcolony events

```cpp
static AgeCheqListener * getListener ( ) ;
```
> Get the listener

```cpp
static void removeListener ( ) ;
```
> Remove the listener, and can't listen to events anymore

```cpp
static void check ( const std::string & ACPin ) ;
```
>  The AgeCheq check method is used to determine the status of a child’s relationship with a particular
 online service. It requires the developer’s unique identifier, the child’s AgeCheq PIN as set up by
 their parent, and the unique identifier of the game or application.

```cpp
static void associateData ( const std::string & ACPin ,
                            const std::string & Data ) ;
```
>  The associateData method allows you to save a string of information linking it to a particular
 AgeCheqPIN for a specific game or app. You’ll want to use that data later if a parent should
 unauthorize your online service.


### Listeners
```cpp
void checkResponse ( const std::string & rtn ,
                     const std::string & rtnmsg ,
                     int apiversion ,
                     int checktype ,
                     bool appauthorized ,
                     bool appblocked ,
                     int parentverified ,
                     bool under13 ,
                     bool under18 ,
                     bool underdevage ,
                     int trials );
```
>  The delegate named checkResponse is triggered once the check command executes. It contains several
 status variables that you can check against.

```cpp
void associateDataResponse ( const std::string & rtn ,
                             const std::string & rtnmsg );
```
>  The delegate named associateDataResponse is triggered once the associateData command executes.


