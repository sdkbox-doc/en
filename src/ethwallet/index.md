[&#171; SDKBOX Home](http://sdkbox.com)

<h1>ETHWallet Plugin</h1>

## Overview

ETHWallet is a js plugin which implement ether pay function. this plugin can make your app support ether pay.(just support `Cocos Creator` js for now)


## Sample Project

[A demo project on github](https://github.com/sdkbox/ETHWallet)

## Integration

you can run follow cmd to integrate `EthWallet`, make sure you have installed `SDKBox Installer`

```bash
$ sdkbox import ethwallet -p `path/to/build/jsb-xxx`
```

## Usage

### Import

there have two way to import `EthWallet` to your project:

* import `ethwallet.js` not as plugin (Default way), so you must invoke `ETHWaller` like follow:

```
const ETHWallet = require('../sdkbox/ethwallet/ethwallet');
const ethwallet = new ETHWallet();
```

* import `ethwallet.js` as plugin, so you can invoke `ETHWallet` like follow:

```
const ethwallet = new ETHWallet();
```

### Initialize

you must set `provider` to init `ETHWallet`. `provider` is a ether node, you can use [Infura](https://infura.io/) or [Etherscan](https://etherscan.io/) or your own self ether node.
```
const PROVIDER_URL = 'https://ropsten.infura.io/L3BRNAgKihyPmcyI1ESe';
ethwallet.init(PROVIDER_URL);
```

### Load Address

create or load a user address.

`EthWallet` will create a new address at first time or user address not exist.

Params:

* password to encry user address which will store local

Return:

* user account, developer should display address to user, so they can send ether to this address. developer can check balance of this address, if > 0, can send user coin or product something. and take care the privete key.

```
const pw = 'password';
const acc = ethwallet.newAccountIf(pw);
```

### Check Balance

```
ethwallet.getBalance(function(result){
    self.log(JSON.stringify(result));
}, this.acc.address);
```


## API

---
`ETHWallet` Initialize

Params:

* `providerURL`, ether node `URL`

```js
ETHWallet.init(providerURL)
```

---
set `ETHWallet` trans `Gas` max limit value, default is `21000`
```js
ETHWallet.setGasLimit(valueInWei)
```

---
create or load `ETHWallet` user pay address

Param:

* `password`， for store user pay address

```js
ETHWallet.newAccountIf(password)
```

---
remit user pay address to developer's address

Params:

* `cb`, result call back
* `address`, developer's address
* `valueInWei`, translate value, default is all balance
* `privateKey`, private key of address which will send ether, default is user's pay address

```js
ETHWallet.remit(cb, address, valueInWei, privateKey)
```

---
check balance of address

Params:

* `cb`, callback
* `address`, check address

```js
ETHWallet.getBalance(cb, address)
```


## Manual integration

cp follow files, which is under pakcage path, to `asset/sdkbox/ethwallet`

> `plugin/lib/a-ethwallet-polyfill-fore-cocos.js`,

> `plugin/lib/a-ethwallet-polyfill-fore-cocos.js.meta`,

> `plugin/lib/ethwallet.js`,

> `plugin/lib/ethwallet.js.meta`


invoke `ETHWallet` in your project, like follow:
```xml
const ETHWallet = require('../sdkbox/ethwallet/ethwallet');
const ethwallet = new ETHWallet();
```


## Note

you can check your transaction by search it on `https://etherscan.io/`.

