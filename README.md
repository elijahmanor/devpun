# devpun

A collection of developer jokes authored by [Elijah Manor](https://elijahmanor.coms) ([@elijahmanor](https://twitter.com/elijahmanor))

## Install

```
$ npm install devpun
```

## Usage

```js
const devpun = require("devpun");

console.log(devpun.random()); // returns a random joke
console.log(devpun.random("react")); // returns a random react joke
console.log(devpun.list()); // returns an array of all jokes
console.log(devpun.list("react")); // returns an array of all react jokes
```

## CLI

```bash
$ devpun [options]
```
or
```bash
$ ./devpun.py [options]
```

### Options

```
-v, --version      output the version number
-l, --list         List all the jokes
-t, --tag <value>  Filter jokes with tag
-h, --help         output usage information
```

### Examples

```bash
$ devpun
$ devpun --tag react
$ devpun -t javascript
$ devpun --list
$ devpun -l
$ devpun -lt react
```

## Tags

- javascript
- react
- java
- c#
- node
- coffeescript
- css
- ember
- backbone
- knockout
