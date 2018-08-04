const jokes = require("./jokes.json");
const sample = require("lodash.sample");

exports.list = () => jokes.map(j => j.text);
exports.random = () => sample(jokes).text;
