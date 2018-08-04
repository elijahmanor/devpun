# devpun

A collection of developer jokes

## Install

```
$ npm install devpun
```

## Usage

```js
const devpun = require("devpun");

// returns a random joke
console.log(devpun.random());

// returns an array of all jokes
console.log(devpun.list());
```

## CLI

```bash
$ devpun [options]
```

### Options

```
-v, --version  output the version number
-l, --list     List all the jokes
-h, --help     output usage information
```

### Examples

```bash
$ devpun
$ devpun --list
$ devpun -l
```
