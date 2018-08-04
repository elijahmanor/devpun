#!/usr/bin/env node

const program = require("commander");
const cyberpun = require("./index");

program
  .version("1.2.0", "-v, --version")
  .option("-l, --list", "List all the jokes")
  .option("-t, --tag <value>", "Filter jokes with tag");

program.on("--help", () => {
  console.log("  Examples:");
  console.log("");
  console.log("    $ cyberpun");
  console.log("    $ cyberpun --tag react");
  console.log("    $ cyberpun -t javascript");
  console.log("    $ cyberpun --list");
  console.log("    $ cyberpun -l");
  console.log("    $ cyberpun -lt react");
  console.log("");
});

program.parse(process.argv);

console.log(
  program.list
    ? cyberpun.list(program.tag).join("\n")
    : cyberpun.random(program.tag)
);
