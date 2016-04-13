[&#171; SDKBOX Home](http://sdkbox.com)

<h1>Share Plugin</h1>

##Overview
You can find [more information about this plugin here.](http://www.cocos2d-x.org/sdkbox/share)

##Facebook support
if you want to use Facebook share on SocialShare Plugin, please follow these two steps:

1. run `sdkbox import facebook` under you project root path.
	the command will import facebook to you project. Facebook plugin have some extra steps to integrate, please click [here](http://docs.sdkbox.com/en/plugins/facebook/v3-cpp/#extra-steps)

2. add Facebook to share platforms in `/Resources/sdkbox_config.json`, look like follow:

```

"android": {
        "Facebook": {
            "debug": false
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "nlmUdPNcFGLWhyLu9cD794EDuDrVQnjd0YjTpB6sX8oHIQRrne",
                        "key": "EuovpLL0UhSGB7Jv5eKFJNMqO"
                    }
                },
                "Facebook": {}    //support facebook share
            }
        }
    },
    "ios": {
        "Facebook": {
            "debug": true
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "haVcKarM96Sr4390XLQoHjyRUSyuHdkMX6letcc38h8TOWyiR9",
                        "key": "BUJTV6NEM7BAhhm82B12VbKGy"
                    }
                },
                "Facebook": {}    //support facebook share
            }
        }
    }

```


<<[../shared/guides.md]


##Sample Project

[A demo project on github](https://github.com/sdkbox/sdkbox-sample-share)
