const jokes = require("./jokes.json");
const sample = require("lodash.sample");

const list = tag => {
  const filtered = tag ? jokes.filter(j => j.tags.includes(tag)) : jokes;
  return filtered.map(j => j.text);
};

exports.list = list;
exports.random = tag => {
  const filtered = list(tag);
  return sample(filtered);
};
