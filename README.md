# devpun

A collection of developer jokes

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

### Options

```
-v, --version      output the version number
-l, --list         List all the jokes
-t, --tag <value>  Filter jokes with tag
-h, --help         output usage information
```

### Examples

```bash
$ cyberpun
$ cyberpun --tag react
$ cyberpun -t javascript
$ cyberpun --list
$ cyberpun -l
$ cyberpun -lt react
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
